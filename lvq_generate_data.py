from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)

from data.models import *

import numpy as np

#Elk data element is een vector van FFT waarden van coordinaten die hoort bij 1 beweging van 1 individu
data = ContinuousSequence.objects.all()
classes = ['walking', 'falling', 'lying down', 'lying', 'sitting down', 'sitting', 'standing up from lying', 'on all fours', 'sitting on the ground', 'standing up from sitting', 'standing up from sitting on the ground'] 

#data = data[:10]

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
        features.append(min(f))
        #max
        features.append(max(f))
        #rms
        features.append(np.sqrt(sum(f[1:]**2)/len(f[1:])))
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
            target.append(1)
        else:
            target.append(0)

    print target

    targets.append(target)
    database.append(features)

print targets

np.save('lvq_target.npy', targets)
np.save('lvq_input.npy', database)