import Oger
import mdp
import numpy as np
import matplotlib.pyplot as plt

resnode = Oger.nodes.ReservoirNode(output_dim = 12)
flow = resnode
database = np.load('database.npy')

flow.train(database)

gridsearch_parameters = {resnode:{'input_scaling': mdp.numx.arange(0.1, 0.5, 0.1)}}

opt = Oger.evaluation.Optimizer(gridsearch_parameters, Oger.utils.nrmse)
opt.grid_search(data, flow, cross_validate_function=Oger.evaluation.n_fold_random, n_folds=5)

print opt