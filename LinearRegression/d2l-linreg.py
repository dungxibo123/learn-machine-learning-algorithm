import numpy as np
import matplotlib.pyplot as plt
import random
def data_generator(n):
    X = []
    Y = []
    angle_const = random.uniform(-3.5,3.7)
    bias = random.uniform(-3.2,3.2)
    for i in range(n):
        noise = random.uniform(-0.02,0.02)
        x = random.uniform(-3,3)
        y = angle_const*x + bias + noise
        X.append([x]); Y.append([y])
    return X,Y

def get_model(X,Y):
    X,Y = np.array(X),np.array(Y)
    X = np.insert(X,0,[1]*X.shape[0],axis=1)
    print(X)
    return np.linalg.inv((X.T@X))@X.T@Y
def predict(W,fea):
    fea = np.array(fea)
    return np.sum(fea@W)

X,Y = data_generator(100)
print(X)
W = get_model(X,Y)
plt.scatter(X,Y)
x_plot = [3,-3]
y_plot = [predict(W,[1.0,3]),predict(W,[1.,-3.])]
plt.plot(x_plot,y_plot)
#plt.plot([0.5,-0,5],[predict(W,[1,0.5]),predict(W,[1,-0.5])])
print(W)
plt.show()
