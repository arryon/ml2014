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
database = []

for d in data:
	x = np.fromstring(d.input_x, sep=',')
	y = np.fromstring(d.input_y, sep=',')
	z = np.fromstring(d.input_z, sep=',')

	for c in classes:
		if d.instances.all()[0].activity == c:
			features = []
			for f in [x,y,z]:
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
			x = np.array([i.x for i in d.instances.all().order_by('datetime')])
			y = np.array([i.y for i in d.instances.all().order_by('datetime')])
			z = np.array([i.z for i in d.instances.all().order_by('datetime')])
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

			target.append(classes.index(c))
			database.append(features)

np.save('target.npy',target)
np.save('database.npy', database)