import numpy as np
from Fundamental import *

A = np.loadtxt('da.txt',delimiter = ',')

X = A[:,:2]
Y = A[:,2:]

needPredict = np.array([1,2032,7])
# X = np.append([[1]]*np.size(X,0),X,1) #check
# m = np.size(X,0) #check
# n = np.size(X,1)
#
# alpha = 0.003
# # theta = GradientDescent(X,Y,alpha = 0.03, iter = 500)
# # print(theta)
# [theta,J_hist] = GradientDescent(X,Y,alpha)
#theta = np.array([[0]]*n)

[theta, Jhist] = GradientDescent(X,Y)



t = predict(needPredict,theta)
print(t)
