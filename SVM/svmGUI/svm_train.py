"""
=========
SVM Train
=========

Trains an SVM model using some fixed parameters.
You can edit the configuration part of this file to
change the parameter values.
"""
from __future__ import division, print_function

# Author: Alvaro Barbero
#
# License: Free BSD
#

import sys
from sklearn import svm
from scipy import io

### CONFIG: edit here to change model parameters ###

# Type of kernel. Kernels available: "linear", "poly", "rbf"
kernel = "linear"
# C regularization parameter
C = 10
# RBF kernel width 
gamma = 0.01
# Polynomial kernel degree
degree = 3
# Polynomial kernel zero coefficient
coef0 = 0
# Name of the dataset file to load
data_file = "data/thyroid.mat"

### CONFIG END ###

def main(argv):
    # Load dataset
    data = io.loadmat(data_file)
    # Train model
    model = train(data['X'], data['y'])
    
    # Compute accuracy over test set
    acc = accuracy(model, data['Xtest'], data['ytest'])
    
    # Print accuracy result
    print("Accuracy:", acc)

# Trains an SVM model with the given data and the configuration parameters
def train(X, y):
    # Create SVM model
    model = svm.SVC(kernel=kernel, C=C, gamma=gamma, coef0=coef0, degree=degree)
    # Train model
    model.fit(X, y.ravel())
    # Return trained model
    return model
    
# Returns the accuracy of the model for some given data
def accuracy(model, X, y):
    return model.score(X, y) * 100
    
if __name__ == "__main__":
    main(sys.argv)
