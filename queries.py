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

d = data[0]

fft_real = get_largest_std(get_fft_real(d.instances.all()))
fft_imag = get_largest_std(get_fft_imag(d.instances.all()))

plt.plot(fft_real)
plt.plot(fft_imag)

plt.show()

