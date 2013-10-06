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

data = ContinuousSequence.objects.all()

instances = data[0].instances.all().order_by('datetime')
fftx = fftpack.fft([i.x for i in instances])
ffty = fftpack.fft([i.y for i in instances])
fftz = fftpack.fft([i.z for i in instances])

print fftx[:10]