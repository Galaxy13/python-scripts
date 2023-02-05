import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

datX=np.load('x_train.npy')
datY=np.log(np.load('y_train.npy'))
datX=pd.DataFrame(datX, columns=datX.dtype.names)

to_drop = ['date',
           'sqft_lot',
           'waterfront',
           'yr_built',
           'yr_renovated',
           'zipcode']
X=datX[['bedrooms',
       'bathrooms',
        'sqft_living',
        'floors',
        'condition',
        'grade',
        'sqft_above',
        'sqft_basement',
        'long',
        'lat']]
N=X.shape[0]
m=X.shape[1]

X = pd.concat([pd.Series(1, index=X.index, name='00'), X], axis=1)

def loss(w, X, y):
    lossValue = np.sum((X.dot(w) - y) ** 2) / N
    return lossValue

def grad(w_k, X, y):
    loss_n = X.dot(w_k) - y
    lossGradient_n = X.T.dot(loss_n) / N
    return np.array(lossGradient_n)


def gradDescent(w_init, alpha, X, y, maxiter=1500, eps=1e-2):
    losses = []
    weights = [w_init]

    w_k = weights[-1]

    # your code goes here
    for d in range(maxiter):
        w_k = w_k - alpha * grad(w_k, X, y)
        lossValue_k = loss(w_k, X, y)
        w_k_length = np.linalg.norm(w_k)
        if w_k_length < eps:
            break
        weights.append(w_k)
        losses.append(lossValue_k)

    return weights, losses

plt.figure(figsize=(8,8))
# print(X.loc[23])

def norm(X):
    # your code goes here
    for row_index in range(N):
        dataset = X.loc[row_index]
        X.loc[row_index] = (dataset - min(dataset)) / (max(dataset) - min(dataset))
    return X

# print(norm(X))

def loss_n(w, X, y, a, b):
    val_X = X.dot(w)
    return np.sum(np.piecewise([val_X, y], [err := y - val_X > 0, err <= 0],
                               [lambda err: a * err ** 2, lambda err: b * err ** 2])) / X.shape[0]

w_init = np.linspace(0, 1, 11)
# print(loss_n(w_init, X, datY, 1, 2))
#

def new_grad(w_k, X, y, a, b):
    # your code goes here
    val_X = X.dot(w_k)
    loss = y - val_X
    loss_with_ab = np.where(loss < 0, loss * a, loss * b)
    lossGradient = X.T.dot(loss_with_ab) / (2 * N)
    return lossGradient

gradient = new_grad(w_init, X, datY, 1, 2)
print(loss_n(w_init, X, datY, 1, 5))
print(gradient)
# plt.plot(range(len(losses)), losses)
# plt.xlabel('Number of Iterations')
# plt.ylabel('Losses')
# plt.legend()
# plt.show()

