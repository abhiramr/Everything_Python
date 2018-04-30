import os
import re
import pandas as pd
import requests
df = pd.DataFrame()
global counter
counter =0

def name_clean(movie):
    new_movie = []
    for i in re.split('[ \.]',movie):
        match = re.search(r'\d\d', i)
        if match:
            break
        else:
            new_movie.append(i)
    return(' '.join(new_movie))

def get_movies():
    directory_list = list()
    for root, dirs, files in os.walk("/media/abhi/My Passport - C/Movies/", topdown=False):
        for name in files:
            if (name.endswith("avi") or name.endswith("mp4") or name.endswith("mkv")) and (os.path.getsize(os.path.join(root, name))/(10**6))>100.0:
                directory_list.append((name_clean(name)).replace('.',' '))
    print("Number of movies = ",len(directory_list))
    return directory_list
    
movie_dict={}
def get_movie_details(names):
    req = "http://www.omdbapi.com/?t='"+names+"'&apikey=<api-key>"
    r = requests.get(req)
    if r.json()['Response']=="True":
        movie_dict[names]=[names,r.json()['imdbRating'],r.json()['Metascore']]
        
movie_list = get_movies()
for i in movie_list:
    get_movie_details(i)
for i in movie_dict.values():
    df = df.append(pd.Series(i, index=['Movie_Name','IMDB_Rating','MetaCritic']),ignore_index=True)
df.to_csv('./movies.csv')
