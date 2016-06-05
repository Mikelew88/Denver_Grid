import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics

def import_data():
    df_0 = pd.read_csv('../Google Drive/privy_data/property_listings_dc.csv')
    zones = pd.read_csv('../Google Drive/privy_data/dc_prop_zones.csv')
    df = df_0.merge(zones, how='inner', on='property_id')
    df.dropna(axis=1, how='all', inplace=True)

    X = df[['list_price' \
    , 'above_grade_square_feet', 'total_square_feet', 'finished_square_feet' \
    , 'derived_basement_square_feet', 'car_spaces', 'garages' \
    , 'beds', 'baths', 'zip']]

    X.dropna(subset=['finished_square_feet'], inplace=True)
    X.fillna(0, inplace=True)

    return df, X

def k_means(X):
    kmeans_model = KMeans(n_clusters=16, random_state=1, n_jobs=-1).fit(X)
    labels = kmeans_model.labels_

    print metrics.silhouette_score(X, labels, metric='euclidean')

    return kmeans_model, labels

if __name__ == '__main__':
    df, X = import_data()
    kmeans_model, labels = k_means(X)
