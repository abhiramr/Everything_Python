import random
import sys
import pandas as pd
from random import shuffle

df = pd.read_csv("./data/santa_names.csv")
names = df["Names"].tolist()
names_copy = df["Names"].tolist()
shuffle(names)
shuffle(names_copy)
length = len(names)
# print(length)
print("Santa-Santee")
print("------------")
for i in range(0,len(names)):
    print("{}-{}".format(names[i],names_copy[i]))
