import sys
from sklearn import svm
from sklearn import cross_validation
from sklearn import datasets

import matplotlib.pyplot as plt

import numpy as np

target = np.load('target.npy')
database = np.load('database.npy')

print database

classifiers = ['rbf', 'linear', 'poly']

def error_with_classifier():
    for c in classifiers:
        clf = svm.SVC(c) 
        cv = cross_validation.ShuffleSplit(n=len(target), n_iter=10,test_size=0.33, random_state=0)
        scores = cross_validation.cross_val_score(clf, np.array(database), np.array(target), cv=cv)
        return (c, scores.mean(), scores.std())



error_with_classifier()

