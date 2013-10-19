import numpy as np
import neurolab as nl
from decimal import *
getcontext().prec = 1

input = np.load('lvq_input.npy')
target= np.load('lvq_target.npy')

train_input = input[:700]
train_target = target[:700]

# Create network with 2 layers:4 neurons in input layer(Competitive)
# and 2 neurons in output layer(liner)
# Aantal input features is aantal input neurons
net = nl.net.newlvq(nl.tool.minmax(input), 13, [1./11.]*11)
# Train network
error = net.train(input, target, epochs=1000, goal=-1)

test_input = input[700:]

o = net.sim(test_input)

np.save('output_lvq.npy',o)
