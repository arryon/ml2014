from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)

from data.models import *

import numpy as np
import neurolab as nl

#Elk data element is een vector van FFT waarden van coordinaten die hoort bij 1 beweging van 1 individu
data = ContinuousSequence.objects.all()
classes = ['walking', 'falling', 'lying down', 'lying', 'sitting down', 'sitting', 'standing up from lying', 'on all fours', 'sitting on the ground', 'standing up from sitting', 'standing up from sitting on the ground'] 

targets = []
database = []

for idx, d in zip(range(len(data)), data):
    print idx
    x = np.array([i.x for i in d.instances.all().order_by('tag','datetime','milliseconds')])
    y = np.array([i.y for i in d.instances.all().order_by('tag','datetime','milliseconds')])
    z = np.array([i.z for i in d.instances.all().order_by('tag','datetime','milliseconds')])

    fftx = np.fft.rfft(x,40)
    ffty = np.fft.rfft(y,40)
    fftz = np.fft.rfft(z,40)

    fftx = np.concatenate((np.real(fftx),np.imag(fftx)))
    ffty = np.concatenate((np.real(ffty),np.imag(ffty)))
    fftz = np.concatenate((np.real(fftz),np.imag(fftz)))

    features = []
    target = []
    #calculate features first
    for f in [fftx,ffty,fftz]:
        #mean feature is DC component
        features.append(f[0])
        #energy = sum of all other values
        features.append(sum(f[1:]**2)/len(f[1:]))
        #standard deviation
        features.append(np.std(f[1:]))
        #variance
        features.append(np.var(f[1:]))
        #min
        #features.append(min(f))
        #max
        #features.append(max(f))
        #rms
        #features.append(np.sqrt(sum(f[1:]**2)/len(f[1:])))
    for f in [x,y,z]:
        #energy = sum of all other values
        features.append(sum(f[1:]**2)/len(f[1:]))
        #standard deviation
        features.append(np.std(f[1:]))
        #variance
        features.append(np.var(f[1:]))
        #min
        features.append(min(f))
        #max
        features.append(max(f))
        #rms
        features.append(np.sqrt(sum(f[1:]**2)/len(f[1:])))      

    #create target list of 11 classes
    for c in classes:
        if d.instances.all()[0].activity == c:
            target.append(classes.index(c))
        else:
            target.append(0)

    targets.append(target)
    database.append(features)

# Create network with 2 layers:4 neurons in input layer(Competitive)
# and 2 neurons in output layer(liner)
# Aantal input features is aantal input neurons
net = nl.net.newlvq(nl.tool.minmax(database), 10, [1./11.]*11)
# Train network
error = net.train(database, target, epochs=1000, goal=-1)

# Plot result
import pylab as pl
xx, yy = np.meshgrid(np.arange(-3, 3.4, 0.2), np.arange(-3, 3.4, 0.2))
xx.shape = xx.size, 1
yy.shape = yy.size, 1
i = np.concatenate((xx, yy), axis=1)
o = net.sim(i)
grid1 = i[o[:, 0]>0]
grid2 = i[o[:, 1]>0]

class1 = input[target[:, 0]>0]
class2 = input[target[:, 1]>0]

pl.plot(class1[:,0], class1[:,1], 'bo', class2[:,0], class2[:,1], 'go')
pl.plot(grid1[:,0], grid1[:,1], 'b.', grid2[:,0], grid2[:,1], 'gx')
pl.axis([-3.2, 3.2, -3, 3])
pl.xlabel('Input[:, 0]')
pl.ylabel('Input[:, 1]')
pl.legend(['class 1', 'class 2', 'detected class 1', 'detected class 2'])
pl.show()