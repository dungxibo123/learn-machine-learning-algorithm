from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import math, random
from scipy.spatial.distance import cdist

#def lostFunction(features = None, labels = None, centers = None):
#    cost = 0
#    for i in range(features.shape[0]):
#        label = np.argmin(labels[i])
#        flag = (features[i] - centers[i])
#        flag = flag**2
#        cost += flag.sum()
#    return cost
def Normalization(features):
    _max = np.empty((1,features.shape[1]))
    for i in range(features.shape[1]):
        _max[0,i] = max(abs(features[:,i].max()), abs(features[:,i].min()))
    for i in range(features.shape[0]):
        features[:,i] = features[:,i] / _max[0,i]
    return features, _max



def has_coverged(centers, n_centers):
    return set(tuple(a) for a in centers) == set(tuple(a) for a in n_centers)

def assign_label(features,centers):
    D = cdist(features, centers)
    return np.argmin(D,axis = 1)
def update_centers(features,labels, centers,k):
    centers = np.zeros(k, features.shape[1])
    for q in range(k):
        xq = features[labels == q, :]
        centers[q, :] = np.mean(xq, axis = 0)
    return centers
def kmeans(features = None, k = 0):
    #features, _ = Normalization(features)

    n = features.shape[1]
    centers = np.random.rand(features.shape[0],k)

    center_list = [centers]
    while True:
        label_list = [assign_label(features,center_list[-1])]
        new_centers = update_centers(features,labels,center_list[-1],k)
        if has_coverged(center_list[-1], new_centers):
            break
        centers.append(new_centers)
        it += 1
    return center_list,label_list,it



def plot(features, labels):
    k = np.amax(label) + 1

    x0 = X[label == 0, :]
    x1 = X[label == 1, :]
    x2 = X[label == 2 :]

    plt.plot(x0[:,0], x0[:,1], 'b^')
    plt.plot(x1[:,1], x1[:,1], 'go')
    plt.plot(x2[:,1], x2[:,1], 'rs')
    plt.show()
means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

X = np.concatenate((X0, X1, X2), axis = 0)
K = 3

original_label = np.asarray([0]*N + [1]*N + [2]*N).T
centers, labels, it = kmeans(features = X,k = K )
