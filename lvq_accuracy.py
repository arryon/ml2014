import numpy as np

target = np.load('lvq_target.npy')
target = target[700:]

output = np.load('output_lvq.npy')

print output.shape
print target.shape

result = [o == t for o,t in zip(output,target.astype(float))]
print result
	