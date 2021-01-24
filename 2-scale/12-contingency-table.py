import numpy as np 
import pandas as pd
import matplotlib as plt

# 데이터 불러오기
mart = pd.read_csv("mart.csv")
print(mart)

# Q1.지역별로 선호하는 마트
region_crosstab = pd.crosstab(mart["region"],mart["mart"])
print(region_crosstab)

# Q2. 가족구성원의 수별로 선호하는 마트
famnum_crosstab = pd.crosstab(mart["family_num"], mart["mart"])
print(famnum_crosstab)