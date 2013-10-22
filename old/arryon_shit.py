import sys
import csv
import datetime

import matplotlib.pyplot as plt
import scipy.fftpack as fftpack
import numpy as np
from data.utils import get_largest_std

from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)

from data.models import *

data = Instance.objects.filter(person='A', sequence=1)

plot_all_stances(data)

tags = get_tag_arrays(walking)
largest = [get_largest_std(get_x_y_z(tag)) for tag in tags]

result = get_largest_std(largest)

plt.plot(result)

plt.show()