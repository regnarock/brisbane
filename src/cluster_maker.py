import numpy as np
from sklearn.cluster import KMeans
from typing import List, Dict


def makeCluster(stations: List[Dict], cluster_on: str, cluster_number: int):
    if cluster_on == 'position':
        x = [(station['latitude'], station['longitude']) for station in stations]
    else:
        raise RuntimeError('Unsupported cluster_on option {}'.format(cluster_on))

    estimator = KMeans(n_clusters=cluster_number)
    estimator.fit(x)

    return {'cluster {}'.format(i + 1): [stations[j]['name'] for j in np.where(estimator.labels_ == i)[0]] for i in range(estimator.n_clusters)}

