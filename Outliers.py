from datetime import datetime
from time import strptime
import os.path
from collections import OrderedDict

import numpy
import matplotlib.pyplot as plt

plt.rcdefaults()


def plot_outliers(data):
    print("Finding Outliers in the data....")

    # Calculate missing data
    numpyFields = ['tweet_id', 'inbound', 'in_response_to_tweet_id']  # numpy floats
    nonNumpyFields = ['author_id', 'created_at', 'text']  # python classes
    columns = numpyFields + nonNumpyFields + ['response_tweet_id']  # re-order by type

    # created at date outliers
    created_at = []
    col_response = data['created_at'].values
    for idx in range(len(col_response)):
        if col_response[idx] != -1 and type(col_response[idx]) != float:
            temp = col_response[idx][4:].split(" ")
            time = temp[2].split(":")
            created = datetime(int(temp[4]), int(strptime(temp[0], '%b').tm_mon), int(temp[1]), int(time[0]),
                               int(time[1]), int(time[2]))
            created_at.append(col_response[idx])
        else:
            created_at.append("NA")

    #for k in created_at:
    #    print(k)

    print("Earliest Tweet:", min(created_at))
    print("Latest Tweet:", max(created_at))


    # avg length of response_tweet_id array which is the all the responses to a tweet
    length_tweet_response = []
    col_response = data['response_tweet_id'].values
    for idx in range(len(col_response)):
        if col_response[idx] != -1 and type(col_response[idx]) != float:
            temp_array = col_response[idx].replace("[", "").replace("]", "").split(",")
            if temp_array[0] != "":
                length_tweet_response.append(len(temp_array))
        else:
            length_tweet_response.append(0)

    print("Average Length of Response Tweet Chain:", sum(length_tweet_response) / len(col_response))
    print("Minimum Length of Response Tweet Chain:", min(length_tweet_response))
    print("Maximum Length of Response Tweet Chain:", max(length_tweet_response))

    print("Plotting Response Tweet Chain Length....")

    totalCountDict = {}
    for temp in length_tweet_response:
        if temp in totalCountDict:
            totalCountDict[temp] = totalCountDict[temp] + 1
        else:
            totalCountDict[temp] = 1

    sortedDict = OrderedDict(sorted(totalCountDict.items()))

    # for k in sortedDict.keys():
    #    print(k, "\t", sortedDict[k])

    # avg length of text in the tweet
    length_of_text = []
    col_response = data['text'].values
    for idx in range(len(col_response)):
        if col_response[idx] != -1 and type(col_response[idx]) != float:
            length_of_text.append(len(col_response[idx]))
        else:
            length_of_text.append(0)

    print("Average Length of Text:", sum(length_of_text) / len(col_response))
    print("Minimum Length of Text:", min(length_of_text))
    print("Maximum Length of Text:", max(length_of_text))

    totalCountDict = {}
    for temp in length_of_text:
        if temp in totalCountDict:
            totalCountDict[temp] = totalCountDict[temp] + 1
        else:
            totalCountDict[temp] = 1

    sortedDict = OrderedDict(sorted(totalCountDict.items()))

    # for k in sortedDict.keys():
    #    print(k, "\t", sortedDict[k])
