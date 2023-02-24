"""
File: response_time.py
Author: Kaitlyn DeCola, kmd8594
"""

import pandas as pd
import numpy as np
import datetime as dt
import dateutil

df = pd.read_csv("clean_data.csv", nrows=500000)
NUM_SECONDS_IN_A_MIN = 60

times = []
#df = df.reset_index()  # make sure indexes pair with number of rows
#df = df.rename_axis(None, axis=1)
df.index.name = None
for index, row in df.iterrows():
    #print(index)
    reply_time = str(row["created_at"])
    try:
        reply = dateutil.parser.parse(reply_time)
    except:
        times.append(-1)
        continue
    #print(type(reply_time))
    #print(reply)

    in_response_to = row["in_response_to_tweet_id"]
    try:
        in_response_to = str(int(in_response_to))
    except:
        times.append(-1)
        continue

   # print(in_response_to)
    d = row['tweet_id']
    if in_response_to != -1:
        
        initial_tweet = df.loc[df['tweet_id'] == in_response_to]
        if initial_tweet.empty:
            times.append(-1)
            continue
        initial_time = str(initial_tweet.iloc[0]["created_at"])
       # print(type(initial_time))
        try:
            initial = dateutil.parser.parse(initial_time)
        except:
            times.append(-1)
            continue
        #print(initial_time)
        diff = reply - initial
        mins = diff.total_seconds() / NUM_SECONDS_IN_A_MIN
        times.append(mins)
    else:
        times.append(-1)
df["response_time"] = times
print("To csv")
df.to_csv("response_times_sample.csv", mode='w', columns=['tweet_id', 'author_id', 'in_response_to_tweet_id', 'response_tweet_id',
                                           'text', 'created_at', 'response_time'], index=False)
    