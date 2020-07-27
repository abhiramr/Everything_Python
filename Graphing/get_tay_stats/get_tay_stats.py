'''Graphing Folklore but parameterized'''

import time
from datetime import datetime
import pandas as pd
from matplotlib import pyplot
import seaborn as sns
import requests
import os
import json
import random

class Taylor:
    '''Class for Taylor Stats Fetching and Graphing'''

    def __init__(self, taylor_video_list):
        self.taytay = taylor_video_list
        if os.path.exists('../../Data/Graphing/taystats.json'):
            with open("../../Data/Graphing/taystats.json", "r") as read_file:
                self.tay_local = json.load(read_file)
            
        else:
            self.tay_local = None

    def compute_stats(self):
        '''
        Gets stats using Youtube API and creates a dataframe with stats
        '''
        tay_stats = {}
        
        if self.tay_local is not None:
            local_ids = {}
            for k, v in self.tay_local.items():
                local_ids[v["items"][0]["id"]]= k
        
        for i in self.taytay:
            cur_local = False
            # Check if i is present in local. If not, fetch.
            if self.tay_local is not None:
                if i in local_ids.keys():
                    title = local_ids[i]
                    print("Processing {}".format(title))
                    tay_stats[title] = self.tay_local[title]
                    cur_local = True

            if not cur_local:
                _r = requests.get("https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={}&key=<getYoutubeAPIDevKey>".format(i))
                title = _r.json()['items'][0]['snippet']['title']
                print("Processing {}".format(title))
                tay_stats[title] = _r.json()
                time.sleep(5)

        tay_nums = {}
        for k, _v in tay_stats.items():
            if "–" in k:
                title = k.split("– ")[1].split(" (")[0].capitalize()
            else:
                title = k.split("- ")[1].split(" (")[0].capitalize()
            tay_nums[title] = _v["items"][0]["statistics"]

        _df = pd.DataFrame(tay_nums).transpose()

        df_views = pd.DataFrame(_df["viewCount"]).sort_values(by="viewCount", ascending=False)
        df_likes = pd.DataFrame(_df["likeCount"]).sort_values(by="likeCount", ascending=False)
        df_dislikes = pd.DataFrame(_df["dislikeCount"]).\
                     sort_values(by="dislikeCount", ascending=False)
        df_comments = pd.DataFrame(_df["commentCount"]).\
                    sort_values(by="commentCount", ascending=False)

        df_views["viewCount"] = df_views.astype("int")
        df_likes["likeCount"] = df_likes.astype("int")
        df_dislikes["dislikeCount"] = df_dislikes.astype("int")
        df_comments["commentCount"] = df_comments.astype("int")

        def perc_calc(row):
            row["percent_likes"] = (row["likeCount"]/(row["likeCount"]+row["dislikeCount"]))*100
            row["percent_dislikes"] = (row["dislikeCount"]/(row["likeCount"]+row["dislikeCount"]))*100
            return row

        df_conc = pd.concat([df_views, df_likes, df_dislikes, df_comments], axis=1)
        df_conc_perc = df_conc.apply(perc_calc,axis = 1)

        return df_conc_perc

    def plot_graph(self):
        '''
        Creates a heatmap from dataframe obtained in previous method
        '''
        df_conc_perc = self.compute_stats()
        df_conc = df_conc_perc[["viewCount","likeCount","dislikeCount","commentCount"]]

        df_conc = df_conc.astype({"viewCount": int, "likeCount": int, "dislikeCount":int, "commentCount":int})

        pyplot.figure(figsize=(36, 12))

        color_palettes = ["coolwarm","YlGnBu","Greens"]
        color_picked = color_palettes[random.randint(0,len(color_palettes)-1)]
        sns.set(font_scale=1.6)
        _ax = sns.heatmap(df_conc, annot=True, fmt="d", linewidths=1.5, cmap=color_picked)
        time_ = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        pyplot.savefig("../../Data/Outputs/Graphing/output_tay_{}.png".format(time_))
        print("Output saved at ../../Data/Outputs/Graphing/output_tay_{}.png".format(time_))
        
        most_viewed = df_conc[df_conc.viewCount == df_conc["viewCount"].max()].index[0]
        most_viewed_count = df_conc["viewCount"].max()
        most_liked = df_conc_perc[df_conc_perc.percent_likes == df_conc_perc["percent_likes"].max()].index[0]
        most_liked_perc = df_conc_perc["percent_likes"].max()
        most_disliked = df_conc_perc[df_conc_perc.percent_dislikes == df_conc_perc["percent_dislikes"].max()].index[0]
        most_disliked_perc = df_conc_perc["percent_dislikes"].max()
        print("\nMost viewed video from Folktales was {} with {} views.".format(most_viewed,most_viewed_count))
        print("Most liked video from Folktales was {} with {:.2f}% likes.".format(most_liked,most_liked_perc))
        print("Most disliked video from Folktales was {} with {:.2f}% dislikes.".format(most_disliked,most_disliked_perc))



if __name__ == "__main__":
    # Video ids for Videos from Taylor's latest Album
    TAY_LIST = ["KsZ6tROaVOQ", "K-a8s8OLBSE", "2s5xdY6MCeI", "osdoLjUNFnA", \
          "OWbDJFtHl3w", "KaM1bCuG4xo", "pEY-GPsru_E", "nn_0zPAfyo8",\
          "9bdLTPNrlEg", "MLV2SJKWk4M", "OuFnpmGwg5k", "6DP4q_1EgQQ",\
         "DUnDkI7l9LQ", "6TAPqXkZW_I", "HpxX4ZE4KWE", "ryLGxpjwAhM", "zLSUp53y-HQ"]

    Taylor(TAY_LIST).plot_graph()
