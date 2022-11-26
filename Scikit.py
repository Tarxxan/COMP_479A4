import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np


class Scikit:

    def __init__(self):
        self.labels = None
        self.x_tfidf = None
        self.title = []
        self.vectorizer = TfidfVectorizer(
            max_df=0.8,
            min_df=2,
            stop_words="english",
        )
        self.kmeans = None

    def vectorize(self, dataset):
        self.x_tfidf = self.vectorizer.fit_transform(dataset)
        print(f"n_samples: {self.x_tfidf.shape[0]}, n_features: {self.x_tfidf.shape[1]}")

    # iterate thorugh all files in HTML directory and put words into a list
    def createModelData(self):
        dataset = []
        if os.getcwd != "HTML_FILES":
            # Change this later so it will work on any computer
            os.chdir("C:/Users/christian.henneveld/PycharmProjects/479A4/HTML_FILES")
        for file in os.listdir(os.getcwd()):
            if file.endswith(".txt"):
                with open(file, "r") as f:
                    self.title.append(file)
                    dataset.append(f.read())
        return dataset

    def createKMeansClustering(self, true_k):

        self.kmeans = KMeans(n_clusters=true_k,max_iter=20,n_init=5)
        self.kmeans.fit(self.x_tfidf)
        self.labels = self.kmeans.labels_

        conU = pd.DataFrame(list(zip(self.title, self.labels)), columns=['title', 'cluster'])
        print(conU.sort_values(by=['cluster']))



