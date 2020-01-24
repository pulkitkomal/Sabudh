from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

digits = load_digits()
X = digits.data
Y = digits.target
print(X.shape)
print(Y.shape)
plt.imshow(X[1].reshape(8,8),cmap='gray')
plt.show()
print(Y[1])
