import sys
import csv
import datetime

sys.path.append('/home/arryon/repos/machinelearning')

from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)

from data.models import Instance