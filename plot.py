import numpy as np
from matplotlib import pyplot as plt
from django.core.management import setup_environ
from machinelearning import settings
setup_environ(settings)

from data.models import *

#Elk data element is een vector van FFT waarden van coordinaten die hoort bij 1 beweging van 1 individu
data = ContinuousSequence.objects.all()
classes = ['walking', 'falling', 'lying down', 'lying', 'sitting down', 'sitting', 'standing up from lying', 'on all fours', 'sitting on the ground', 'standing up from sitting', 'standing up from sitting on the ground'] 

target = []
database = []
classes_count = [0]*len(classes)

def plot_sequence_instances():
    _dict = {}
    for c in classes:
        _dict[c] = []

    for d in data:
        _dict[d.instances.all()[0].activity].append(len(d.instances.all()))

    p = []
    for c in classes:
        p.append(plt.plot(_dict[c]))
    plt.legend((p[0][0], p[1][0], p[2][0], p[3][0], p[4][0], p[5][0], p[6][0], p[7][0], p[8][0], p[9][0], p[10][0]), ('walking', 'falling', 'lying down', 'lying', 'sitting down', 'sitting', 'standing up from lying', 'on all fours', 'sitting on the ground', 'standing up from sitting', 'standing up from sitting on the ground'))
    plt.title('Number of x,y,z-datapoints per sequence') 
    plt.xlabel('Number of sequences')
    plt.ylabel('Number of instances')
    plt.savefig("sequence_instances.png")
    plt.show()


def plot_instances_class():
    classes_count = [0]*len(classes)
    for d in data:
        for idx in range(len(classes)):
            if d.instances.all()[0].activity == classes[idx]:
                classes_count[idx]+=1
    plt.bar(range(len(classes)), classes_count, width=0.8)
    plt.ylabel('Number of instances')
    plt.title('Number of instances in each class')
    plt.xticks(np.arange(11), ['walking', 'falling', 'lying down', 'lying', 'sitting down', 'sitting', 'standing up from lying', 'on all fours', 'sitting on the ground', 'standing up from sitting', 'standing up from sitting on the ground'], rotation=30)
    plt.savefig("instances_class.png", bbox_inches=5)
    plt.show()


plot_sequence_instances()
plot_instances_class()
