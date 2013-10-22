import sys
from sklearn import svm
from sklearn import cross_validation
from sklearn import datasets
from sklearn import grid_search
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

import numpy as np

target = np.load('target.npy')
database = np.load('database.npy')

class_count = [0]*11

for idx in range(len(database)):
    class_count[target[idx]] += 1

class_weight_dict = {}
class_weights = np.array(class_count).astype(float)/sum(class_count)
for idx in range(len(class_count)):
    class_weight_dict[idx]=class_weights[idx]




def error_with_weights():
    clf = svm.SVC(kernel='linear', class_weight='auto')
#    clf.fit(database, target, class_weight=class_weight_dict)
    cv = cross_validation.ShuffleSplit(n=len(target), n_iter=10,test_size=0.1, random_state=0)
    scores = cross_validation.cross_val_score(clf, np.array(database), np.array(target), cv=cv)
    print (scores.mean(), scores.std())

'''
data = list()
for d in database:
    new = [float(e) for e in d]
    data.append(new)

newtarget = list()
for t in target:
    newtarget.append(int(t))

classifiers = ['linear','rbf','sigmoid','poly']

def error_with_classifier():
    for c in classifiers:
        clf = svm.SVC(kernel=c) 
            
        cv = cross_validation.ShuffleSplit(n=len(newtarget), n_iter=10,test_size=0.1, random_state=0)
        param_grid = [
          {'C': [1, 10, 100, 1000], 'kernel': ['linear'], 'degree':[2,3,4,5]}
         ]
        out = grid_search.GridSearchCV(clf, param_grid=param_grid, cv=cv)
        
        #scores = cross_validation.cross_val_score(clf, np.array(data), np.array(newtarget), cv=cv)
        #print (c, scores.mean(), scores.std())

error_with_classifier()

'''

error_with_weights()
