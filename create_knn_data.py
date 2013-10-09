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
real = []
imag = []

for d in data:
    x = np.fromstring(d.input_x, sep=',')
    y = np.fromstring(d.input_y, sep=',')
    z = np.fromstring(d.input_z, sep=',')
    out = get_largest_std([x,y,z])
    for c in classes:
        if d.instances.all()[0].activity == c:
                target.append(classes.index(c))
                real.append(out[:len(out)/2])
                imag.append(out[len(out)/2:])

np.save('target.npy',target)
np.save('real.npy', database)
np.save('imag.npy', imag)