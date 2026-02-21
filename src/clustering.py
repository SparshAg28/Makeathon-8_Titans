from sklearn.cluster import DBSCAN
import numpy as np

def detect_clusters(df):
    points = df[["x","y","z"]].values
    clustering = DBSCAN(eps=0.5, min_samples=10).fit(points)

    labels = clustering.labels_
    df["cluster"] = labels

    return df