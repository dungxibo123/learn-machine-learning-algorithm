from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import sklearn as sk


#sigmoid function
def sigmoid(x):
    '''
    @param x: is heuristic matrix
    '''
    return 1 / (1 + np.exp(-x))
# load data from csv file
data = pd.read_csv('dataset.csv').values

N, d = data.shape
x = data[:, 0:d-1].reshape(-1,d-1)
y = data[:,2].reshape(-1,1)
print(x,y, sep='\n')
#Draw data figure by scatter in matplotlib

plt.scatter(x[:10,0], x[:10,1], c = 'blue', edgecolors='none', label='cho vay')
plt.scatter(x[10:, 0], x[10:, 1], c='red',edgecolor='none',label='tu choi vay')
#plt.show()
x = np.hstack((np.ones((N,1)),x))
numsOfIteration = 3000
cost = np.zeros((numsOfIteration,1))
lr = 0.015
w = np.array([0.,0.1,0.1]).reshape(-1,1)
for i in range(numsOfIteration):
    y_predict = sigmoid(np.dot(x,w))
    cost[i] = -np.sum(np.multiply(y, np.log(y_predict)) + np.multiply(1-y, np.log(1-y_predict)))
    w = w - lr * np.dot(x.T, y_predict - y)
    print('Cost evalutate as {} time(s) is: {}'.format(i + 1,cost[i]))

t = 0.5
plt.plot((4,10),(-(w[0] + 4*w[1] + np.log(1/t - 1))/w[2], -(w[0] + 10*w[1] + np.log(1/t - 1))/w[2]),'g')
plt.show()
