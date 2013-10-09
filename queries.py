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

#Elk data element is een vector van FFT waarden van coordinaten die hoort bij 1 beweging van 1 individu
data = ContinuousSequence.objects.all()

classes = ['walking', 'falling', 'lying down', 'lying', 'sitting down', 'sitting', 'standing up from lying', 'on all fours', 'sitting on the ground', 'standing up from sitting', 'standing up from sitting on the ground'] 

target = []
for d in data:
    for c in classes:
        if d.instances.all()[0].activity == c:
            try:
                target.append(classes.index(c))
            except:            
                continue
print len(target)

#knn.fit(database, target)

'''
x = np.fromstring(data[112].input_x, sep=',')
y = np.fromstring(data[112].input_y, sep=',')
z = np.fromstring(data[112].input_z, sep=',')

#print len(x)
#De eerste helft is reeel, tweede helft is imaginair.
#Cluster 11 classes with KNN
#Train classifer on FFT features from every class



out = get_largest_std([x,y,z])
plt.plot(out)
#plt.show()
'''
