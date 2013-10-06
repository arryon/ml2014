import sys
import csv
import datetime

sys.path.append('/home/arryon/repos/ml')

from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)

from data.models import Instance, ContinuousSequence

data = Instance.objects.all()

activity = None

sequence = ContinuousSequence()
sequence.save()

#iterate over data
for d in data:
	if None == activity:
		activity = d.activity

	#if activity changes, save old and create new sequence
	if not d.activity == activity:
		sequence.save()
		sequence = ContinuousSequence()
		activity = d.activity
		sequence.save()

	#add instance to sequence
	sequence.instances.add(d)
