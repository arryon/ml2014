import sys
import csv
import datetime

import matplotlib.pyplot as plt

from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)

from data.models import Instance, find_tag

data = Instance.objects.filter(person='A', sequence=1, tag=find_tag('ankle left'),activity='walking').order_by('datetime')

x = [d.x for d in data]
y = [d.y for d in data]
z = [d.z for d in data]

plt.plot(x)
plt.plot(y)
plt.plot(z)
plt.show()