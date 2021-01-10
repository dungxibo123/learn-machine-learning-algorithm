import numpy as np
import matplotlib.pyplot as plt


means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

# each column is a datapoint
X = np.concatenate((X0, X1, X2), axis = 0).T
# extended data
X = np.concatenate((np.ones((1, 3*N)), X), axis = 0)
C = 3
plt.plot(X0[:,0],X0[:,1],'ro')
plt.plot(X1[:,0],X1[:,1],'gs')
plt.plot(X2[:,0],X2[:,1],'b^')
plt.show()

Y = np.asarray([0]*N + [1]*N + [2]*N).T

def loss(W,X,Y):
    pass

def sgd(W,X,Y,lr=0.001):
    pass

def predict(W,X):
    return W.T@X

def predict_classes(W,X):
    return np.argmax(predict(W,X))
