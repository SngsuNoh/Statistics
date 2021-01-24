import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

# 정규분포
stat_nor = sp.stats.norm(0,1)

# 정규분포 pdf 그리기
fig, ax = plt.subplots()
x_axis = np.linspace(-3, 3, 100)
plt.bar(x_axis,stat_nor.pdf(x_axis))


##
plt.show()
fig.savefig("pdf_plot.png")

# 정규분포 cdf
x_axis = np.linspace(-3, 3, 100)
plt.bar(x_axis,stat_nor.cdf(x_axis))


##
plt.show()
fig.savefig("cdf_plot.png")

# 정규분포 샘플링
## seed 설정
np.random.seed(seed=0)

## 샘플 추출
random_nor = np.random.normal(0,1,100)
print(random_nor) 

## 평균 계산
nor_mean = np.mean(random_nor)
print(nor_mean)