import sys
import csv
import datetime

sys.path.append('/home/arryon/repos/machinelearning')

from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)

from data.models import Instance, find_tag

person1 = Instance.objects.filter(person='A')

print "A has {0} data points".format(len(person1))