import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

# 균일분포
stat_uni = sp.stats.uniform()

# 그리기
fig, ax = plt.subplots()
x_axis = np.linspace(0, 1, 100)
plt.bar(x_axis,stat_uni.pdf(x_axis))


##
plt.show()
fig.savefig("pdf_plot.png")

# cdf 그리기 
x_axis = np.linspace(0, 1, 100) 
plt.bar(x_axis,stat_uni.cdf(x_axis))


##
plt.show()
fig.savefig("cdf_plot.png")

# 균일분포 샘플링
## seed 설정
np.random.seed(seed=0)

## 샘플 추출
random_uni = np.random.uniform(0,1,100)
print(random_uni) 

## 평균 계산
uni_mean = np.mean(random_uni)
print(uni_mean)
