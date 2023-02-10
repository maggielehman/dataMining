import math
import os.path

import numpy
import matplotlib.pyplot as plt
import pandas as pd

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


# Displays a bar chart of missing data in each column for twitter support
def plot_missing_data(data):
    print("Plotting Missing data....");

    # Calculate missing data
    numpyFields = ['tweet_id', 'inbound', 'in_response_to_tweet_id'] # numpy floats
    nonNumpyFields = ['author_id', 'created_at', 'text'] # python classes
    columns = numpyFields + nonNumpyFields + ['response_tweet_id'] # re-order by type
    missing = []

    # count nan objects
    y_pos = np.arange(len(columns))
    for col in numpyFields:
        c = 0
        ar = data[col].values
        for el in ar:
            if numpy.isnan(el):
                c += 1
        missing.append(c)

    # count null objects
    for col in nonNumpyFields:
        c = 0
        ar = data[col].values
        for el in ar:
            if el is None or el == '':
                c += 1
        missing.append(c)

    # count float (means Null in this edge case) objects
    floatColumn = 'response_tweet_id';
    c = 0
    ar = data[floatColumn].values
    for el in ar:
        if isinstance(el, float):
            c += 1
    missing.append(c)

    # plot missing data
    plt.bar(y_pos, missing, align='center', alpha=0.5)
    plt.xticks(y_pos, columns)
    plt.ylabel('Missing Data Count')
    plt.title('Missing Data in Column')

    plt.show()



# Cleans the data and writes it to a csv for future use, if file already exists it doesn't do anything
def clean_data(data):
    if not os.path.exists('clean_data.csv'):
        # clean data
        ar = data['response_tweet_id'].values
        for idx in range(len(ar)):
            if isinstance(ar[idx],float) or ar[idx] == '' or ar[idx] is None:
                data['response_tweet_id'].values[idx] = -1

        ar = data['in_response_to_tweet_id'].values
        for idx in range(len(ar)):
            if numpy.isnan(ar[idx]):
                data['in_response_to_tweet_id'].values[idx] = -1

        clean_data = {}
        for col in data.columns:
            clean_data[col] = data[col].values

        df = pd.DataFrame(clean_data)
        df.to_csv("clean_data.csv")
        print("Cleaning complete")
    else:
        print("Clean data csv already exists :)")

