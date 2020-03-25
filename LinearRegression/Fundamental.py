import numpy as np
def predict(X,theta):
    return X@theta
def computeCostFunction(X,y,theta):
    predicted = predict(X,theta)
    sqr = (predicted - y)**2
    sum = np.sum(sqr)
    m = np.size()
    J = (1/(2*m))*sum
    return J
def computeCostFunctionVec(X,y,theta):
    error = predict(theta,X) - y
    m = np.size(y)
    J = (1/(2*m))*np.tranpose(error)@error
    return J
