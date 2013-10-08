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

data = ContinuousSequence.objects.all()

x = np.fromstring(data[0].input_x, sep=',')
y = np.fromstring(data[0].input_x, sep=',')
z = np.fromstring(data[0].input_z, sep=',')

out = get_largest_std([x,y,z])
plt.plot(out)
plt.show()

	



