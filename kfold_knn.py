from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation
from sklearn import datasets

import matplotlib.pyplot as plt

import numpy as np

target = np.load('target.npy')
database = np.load('database.npy')

print target.shape
print database.shape

def error_with_k(k):
    knn = KNeighborsClassifier(k) 
    #knn.fit(database, target)

    cv = cross_validation.ShuffleSplit(n=len(target), n_iter=10,test_size=0.33, random_state=0)
    scores = cross_validation.cross_val_score(knn, np.array(database), np.array(target), cv=cv)
    return (k, scores.mean(), scores.std())


means = []
stds = []

n_k = 20

for k in range(1,n_k+1):
    k, mean, std = error_with_k(k)
    means.append(mean)
    stds.append(std)
    print "k={0}, accuracy={1}%, std={2}%".format(k, round(mean*1000)/10,round(std*1000)/10)

print "Max: k={0}, accuracy={1}%, std={2}%".format(means.index(max(means))+1, max(means), stds[means.index(max(means))])

plt.plot(means,label="mean accuracy")
plt.plot(stds,label="std. deviation")
plt.title("K-nearest neighbors accuracy")
plt.xlabel("# of k")
plt.ylabel("percentage")
plt.legend(loc=7)
plt.xticks(range(0,n_k))
plt.grid()
plt.show()

