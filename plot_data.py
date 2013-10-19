import matplotlib.pyplot as plt

import numpy as np

target = np.load('target.npy')
database = np.load('database.npy')

f1 = database[:,0]
f2 = database[:,1]
f3 = database[:,2]

plt.plot(f1,f2,'ro',f1,f3,'bo',f2,f3,'go')
plt.show()