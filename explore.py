"""
File: explore.py
Author: Savannah Alfaro, sea2985
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# remove columns of cleaned data
df = pd.read_csv("clean_data.csv")
df.to_csv("explore.csv", mode='w', columns=['tweet_id', 'author_id', 'created_at', 'text', 'response_tweet_id',
                                            'in_response_to_tweet_id'], index=False)

# split created_at into multiple columns
df = pd.read_csv("explore.csv")
df[["day", "month", "date", "time", "timezone", "year"]] = df["created_at"].str.split(' ', expand=True)
df.to_csv("explore.csv", mode='w', columns=['tweet_id', 'author_id', 'response_tweet_id', 'in_response_to_tweet_id',
                                            'day', 'month', 'date', 'time', 'text'], index=False)

# read in csv file
# df = pd.read_csv("explore.csv")

# top 20 tweet authors
# df['author_id'].value_counts()[:20].plot(title='Top 20 Tweet Authors', kind='bar', xlabel='Company', ylabel='Count')

# number of tweets per day
# df['day'].value_counts().plot(title='Number of Tweets per Day', kind='bar', xlabel='Day of the Week', ylabel='Count')

# number of tweets per hour df["time"] = pd.to_datetime(df["time"], format='%H:%M:%S') df.groupby(df[
# "time"].dt.hour)["tweet_id"].count().plot(title='Number of Tweets per Hour', kind='bar', xlabel='Hour', ylabel='Count')

# plot the graph
# plt.tight_layout()
# plt.show()
# plt.savefig('untitled.png')
