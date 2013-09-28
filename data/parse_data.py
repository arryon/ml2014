import sys
import csv
import datetime

sys.path.append('/home/arryon/repos/machinelearning')

from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)

from data.models import Instance

with open('dataset.txt') as csv_file:
	reader = csv.reader(csv_file, delimiter=',')
	for row in reader:
		instance = Instance()
		p_id = row[0]
		instance.person = p_id[0]
		instance.sequence = p_id[1:]
		instance.tag = row[1]
		instance.x = row[4]
		instance.y = row[5]
		instance.z = row[6]
		instance.activity = row[7]

		#convert time to python datetime
		t = row[3]
		instance.datetime = datetime.datetime(int(t[6:10]),int(t[3:5]),int(t[0:2]),int(t[11:13]),int(t[14:16]),int(t[17:19]),int(t[20:]+'00'))
		instance.save()

