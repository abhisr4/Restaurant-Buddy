import numpy as np
import pandas as pd
import json

df=pd.read_csv("data/finalProcessedData.csv")
rating=df['rating']
vote=df['voteCount']
cusine=df['cusine']
cost=df['cost']
time=df['timing']

addressDict={}
rating=np.asarray(time)
for i in range(len(time)):
    addressDict[i]=time[i]

import json
with open('time.json', 'w') as fp:
    json.dump(addressDict, fp)