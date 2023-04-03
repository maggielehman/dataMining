import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def clean_data(df):
    # drop all rows that have a negative response time
    df.drop(df[(df['response_time'] == -1)].index, inplace=True)

    # add text_length column
    df["text_length"] = df["text"].str.len()

    # split created_at into multiple columns
    df[["day", "month", "date", "time", "timezone", "year"]] = df["created_at"].str.split(' ', expand=True)
    df.to_csv("cleaned_response_times.csv", mode='w', columns=['tweet_id', 'author_id', 'response_tweet_id',
                                                               'in_response_to_tweet_id', 'response_time', 'day',
                                                               'month', 'date', 'time', 'text_length', 'text'], index=False)


def normalize_data(df):
    my_data = []

    # normalize response time
    updated_response_time = []
    miny = min(df['response_time'])
    maxy = max(df['response_time'])
    for x in range(len(df['response_time'])):
        updated_response_time.append((df['response_time'][x] - miny) / (maxy - miny))
    my_data.append(updated_response_time)

    # normalize text length
    updated_text_length = []
    miny = min(df['text_length'])
    maxy = max(df['text_length'])
    for x in range(len(df['text_length'])):
        updated_text_length.append((df['text_length'][x] - miny) / (maxy - miny))
    my_data.append(updated_text_length)

    return np.array(my_data)


def k_means(my_data):
    # cluster the data
    k = 4
    kmeans_cluster = KMeans(init="random", n_clusters=k, n_init=4, random_state=0)
    kmeans_cluster.fit(my_data)
    centroids = kmeans_cluster.cluster_centers_
    label = kmeans_cluster.fit_predict(my_data)
    unique_labels = np.unique(label)

    # plot the clusters
    plt.figure(figsize=(8, 8))
    for i in unique_labels:
        plt.scatter(my_data[label == i, 0], my_data[label == i, 1], label=i)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=169, linewidths=1, color='k', zorder=4)
    plt.legend()

    # plt.show()
    plt.savefig('plot.png')


def main():
    # read the response time dataframe
    df = pd.read_csv('response_times.csv')

    # clean the data
    clean_data(df)

    # read the cleaned response time dataframe
    df = pd.read_csv('cleaned_response_times.csv')

    # normalize the data
    my_data = normalize_data(df)
    print(my_data)

    # # cluster the data
    # k_means(my_data)


if __name__ == '__main__':
    main()
