from statistics import variance, stdev
import numpy as np

coffee = np.array([202,177,121,148,89,121,137,158])

#분산 계산
cf_var = variance(coffee)
print("Simple Variance :", round(cf_var,2))