from sklearn.decomposition import PCA
import numpy as np

database = np.load('database.npy')

pca = PCA(n_components=30)
pca.fit(database)
return pca.explained_variance_ratio_

