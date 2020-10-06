import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import random as rd

'''
Perceptron with SGD optimization
'''

#Reading txt file
feature = np.loadtxt('DATA.txt', delimiter = ',')
#check
#print(feature)


#neccessary parameter
expected_label = feature[:, -1]
feature = feature[:,:-1]
training_missclassify = []
#check
#print(expected_label, feature, sep ='\n')

#enhance col for feature

feature = np.hstack((np.ones((feature.shape[0],1)),feature))
#check
print(feature)

w = [rd.uniform(0,3),rd.uniform(0,3), rd.uniform(0,3)]
w = np.array(w)
for i in range(feature.shape[0]):
    if np.sum(x.T@w) / np.sum(w[1:]**2) * expected_label > 0: training_label.append(1)
    else: training_missclassify.append(-1)
corverged = -1
while corverged != 0:
    rng = np.random.default_rng()
    rng.shuffle(arr, axis = 0)
    for i in range(feature.shape[0]):


