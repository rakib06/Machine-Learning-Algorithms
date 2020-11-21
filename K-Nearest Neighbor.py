import numpy as np

class KNearestNeighbor():
    def __init__(self, k):
        self.k = k

    def train(self, x, y):
        self.X_train = x
        self.Y_train = y

    def predict(self, X_test):
        distances = self.compute_distance(X_test)

    def compute_distance(self):
        pass

    def predict_labels(self, distance):
        pass


