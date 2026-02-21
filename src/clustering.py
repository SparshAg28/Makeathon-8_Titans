from sklearn.cluster import DBSCAN

def detect_clusters(df):
    points = df[["x","y","z"]].values

    clustering = DBSCAN(eps=0.8, min_samples=20).fit(points)
    df["cluster"] = clustering.labels_

    return df