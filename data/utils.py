import numpy as np

def get_largest_std(nested_list):
	tuples = [(np.std(a),idx) for idx,a in zip(range(len(nested_list)),nested_list)]

	_max = max(tuples)

	return nested_list[_max[1]]

	