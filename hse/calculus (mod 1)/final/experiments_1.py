import numpy as np
import pandas as pd

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

w = np.linspace(1, m + 1, 11)
# print(np.sum(X + w[1:], axis=1))
X = pd.concat([pd.Series(1, index=X.index, name='00'), X], axis=1)
y_hat = np.sum(X * w, axis=1)
print(y_hat)
diff = np.sum((datY - y_hat) * X.T, axis=1) * (2 / X.shape[0])
diff = np.array(diff)
print(diff)