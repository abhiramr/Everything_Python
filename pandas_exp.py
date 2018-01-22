#To line profile use - 
#kernprof -l pandas_exp.py
#python -m line_profiler pandas_exp.py.lprof

import pandas as pd
import numpy as np
import io
import requests
import os
import errno

output_file = "./cache/data_1.csv"

@profile
def return_data():
    get_data_url = "https://tinyurl.com/getdata-csv"
        
    if not os.path.exists(os.path.dirname(output_file)):
        try:
            r = requests.get(get_data_url).content
            os.makedirs(os.path.dirname(output_file))
            csv_content = pd.read_csv(io.StringIO(r.decode('utf-8'),dtype={ 
                    "timestamp": np.int64,
                    "usermac": str,
                    "level": np.int64, 
                    "lat": np.float64,
                    "lng": np.float64,
                    "station1": str, 
                    "strength1": np.int64,
                },low_memory=False))
            csv_content.to_csv(output_file)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    else:
        csv_content = pd.read_csv(output_file,dtype={ 
                    "timestamp": np.int64,
                    "usermac": str,
                    "level": np.int64, 
                    "lat": np.float64,
                    "lng": np.float64,
                    "station1": str, 
                    "strength1": np.int64,
                },low_memory=False)

    csv_content.columns=["index","timestamp", 
                          "usermac", 
                          "level", 
                          "lat", "lng",
                          "station1", "strength1",
                          "station2", "strength2",
                          "station3", "strength3",
                          "station4", "strength4",
                          "station5", "strength5",
                          "station6", "strength6",
                          "station7", "strength7",
                          "station8", "strength8",
                          "station9", "strength9",
                          "station10", "strength10"
                      ]

    print(csv_content.head())
#    print(csv_content.info())

return_data()
