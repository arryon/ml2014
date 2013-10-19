import sys
import csv
import datetime

import matplotlib.pyplot as plt
import numpy as np
from data.utils import get_largest_std

from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)

from data.models import *

from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

import cPickle
import os
import glob

from sklearn import cross_validation
from sklearn import datasets

#Elk data element is een vector van FFT waarden van coordinaten die hoort bij 1 beweging van 1 individu
data = ContinuousSequence.objects.all()

classes = ['walking', 'falling', 'lying down', 'lying', 'sitting down', 'sitting', 'standing up from lying', 'on all fours', 'sitting on the ground', 'standing up from sitting', 'standing up from sitting on the ground'] 

x = np.fromstring(data[2].input_x, sep=',')
y = np.fromstring(data[2].input_y, sep=',')
z = np.fromstring(data[2].input_z, sep=',')
out = get_largest_std([x,y,z])
out_first_half = out[0:len(out)/2]
out_second_half = out[len(out)/2:]

target = []
database = []
'''
for d in data:
    x = np.fromstring(d.input_x, sep=',')
    y = np.fromstring(d.input_y, sep=',')
    z = np.fromstring(d.input_z, sep=',')
    out = get_largest_std([x,y,z])
    for c in classes:
        if d.instances.all()[0].activity == c:
                target.append(classes.index(c))
                database.append(out)
'''

target = np.load('target.npy')
database = np.load('database.npy')

k = 1 
#knn = KNeighborsClassifier(k)
clf = svm.SVC(kernel='linear')
'''
if glob.glob(os.path.join('', 'knn.pkl'):
    with open('my_dumped_classifier.pkl', 'rb') as fid:
        knn = cPickle.load(fid)    
else:
    knn = KNeighborsClassifier(k)

with open('my_dumped_classifier.pkl', 'wb') as fid:
            cPickle.dump(knn, fid) 
'''

#Data moet in het formaat elk element in 
#knn.fit(database, target)
clf.fit(database, target)
#dec = clf.decision_function([[1]])
#print dec.shape[1]
error = 0


cv = cross_validation.ShuffleSplit(n=len(target), n_iter=10,test_size=0.4, random_state=0)
#scores = cross_validation.cross_val_score(knn, np.array(database), np.array(target), cv=cv)
scores = cross_validation.cross_val_score(clf, np.array(database), np.array(target), cv=cv)
print("k = %i Accuracy: %0.2f (+/- %0.2f)" % (k, scores.mean(), scores.std() * 2))


print "The length of data is : ", len(data)
for idx in range(len(data)):
    result = clf.predict(np.fromstring(data[idx].input_x, sep=','))

    if data[idx].instances.all()[0].activity == classes[result[0]]:
        error = error + 0 
    else:
        error = error + 1

print "The error is: ", error
#error = error + 0 if data[element].instances.all()[0].activity == classes[result[0]] else error = error + 1


#De eerste helft is reeel, tweede helft is imaginair.
#Cluster 11 classes with KNN
#Train classifer on FFT features from every class


plt.plot(out)
#plt.show()
