from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation
from sklearn import datasets

import numpy as np

target = np.load('target.npy')
database = np.load('database.npy')

def error_with_k(k):
    knn = KNeighborsClassifier(k) 
    #knn.fit(database, target)

    cv = cross_validation.ShuffleSplit(n=len(target), n_iter=10,test_size=0.4, random_state=0)
    scores = cross_validation.cross_val_score(knn, np.array(database), np.array(target), cv=cv)
    return (k, scores.mean(), scores.std() * 2)

for k in range(10)[1:]:
    k, mean, std = error_with_k(k)
    print "{0}, {1}, {2}".format(k, mean,std)
