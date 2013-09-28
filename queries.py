import sys
import csv
import datetime

sys.path.append('/home/arryon/repos/machinelearning')

from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)
from matplotlib import pyplot as plt
from data.models import Instance, find_tag
import numpy as np

#http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans
from sklearn.cluster import KMeans

kmeans = KMeans(8)
KMeans.fit(X[,y])
KMeans.predict()

data = Instance.objects.filter(person='A', sequence=1, activity='standing up from lying', tag=find_tag('ankle left'))
data2 = Instance.objects.filter(person='A', sequence=2, activity='standing up from lying', tag='020-000-032-221')

x = [d.x for d in data]
y = [d.y for d in data]
z = [d.z for d in data]

x2 = [d.x for d in data2]
y2 = [d.y for d in data2]
z2 = [d.z for d in data2]

print np.var(x), np.var(y), np.var(z)
print np.var(x2), np.var(y2), np.var(z2)


#lengte sequences checken
#hoogste variteit checken voor coordinaat dimensie  

plt.figure(1)
plt.plot(x)
plt.plot(y)
plt.plot(z)

plt.figure(2)
plt.plot(x2)
plt.plot(y2)
plt.plot(z2)
#plt.show()


print "A has {0} data points".format(len(person1))
