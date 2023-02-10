import os.path
from collections import OrderedDict

import numpy
import matplotlib.pyplot as plt
import pandas as pd

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def plot_outliers(data):
    print("Finding Outliers in the data....");

    # Calculate missing data
    numpyFields = ['tweet_id', 'inbound', 'in_response_to_tweet_id']  # numpy floats
    nonNumpyFields = ['author_id', 'created_at', 'text']  # python classes
    columns = numpyFields + nonNumpyFields + ['response_tweet_id']  # re-order by type

    #created at date outliers
    created_at_avg = 0

    #avg length of response_tweet_id array which is the all the responses to a tweet
    length_tweet_response = []
    col_response = data['response_tweet_id'].values
    for idx in range(len(col_response)):
        if type(col_response[idx]) == float:
            print(isinstance(col_response[idx],float))
            print(col_response[idx])
        if col_response[idx] != -1:
            temp_array = col_response[idx].replace("[", "").replace("]", "").split(",")
            if temp_array[0] != "":
                length_tweet_response.append(len(temp_array))

    print("Average Length of Response Tweet Chain:", sum(length_tweet_response) / len(col_response))
    print("Minimum Length of Response Tweet Chain:", min(length_tweet_response))
    print("Maximum Length of Response Tweet Chain:", max(length_tweet_response))

    print("Plotting Response Tweet Chain Length....")

    totalCountDict = {}
    for temp in length_tweet_response:
        if temp in totalCountDict:
            totalCountDict[temp] = totalCountDict[temp] + 1
        else:
            totalCountDict[temp] = 0

    sortedDict = OrderedDict(sorted(totalCountDict.items()))
    
    plt.bar(sortedDict.keys(), sortedDict.values(), align='center', alpha=0.5)
    plt.ylabel('Length of Response Chain')
    plt.title('Count or Response Chain Length')

    plt.show()


    #avg length of text in the tweet