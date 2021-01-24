from statistics import variance, stdev
import numpy as np 
import pandas as pd

# body.csv 읽어오기 
body = pd.read_csv("body.csv")

# 상관계수 
corr_body = body.corr()

print(corr_body)