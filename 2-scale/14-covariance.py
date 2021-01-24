from statistics import variance, stdev
import numpy as np 
import pandas as pd

# body.csv 읽어오기 
body = pd.read_csv("body.csv")

# 공분산
cov_body = body.cov()

print(cov_body)