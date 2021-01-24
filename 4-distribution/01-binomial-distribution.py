import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

# 이항분포 생성
n, p = 10, 0.3
stat_bin = sp.stats.binom(n,p)

# 그리기
fig, ax = plt.subplots()
x_axis = np.arange(n + 1) 
plt.bar(x_axis, stat_bin.pmf(x_axis))

##
plt.show()
fig.savefig("pmf_plot.png")

# 이항분포cdf
x_axis = np.arange(n + 1) 
plt.bar(x_axis, stat_bin.cdf(x_axis))

##
plt.show()
fig.savefig("cdf_plot.png")

# 랜덤표본 추출
## seed 설정 seed = 0 
np.random.seed(seed=0)

## 랜덤 샘플 추출
random_bin = np.random.binomial(n=10,p=0.3,size=50)
print(random_bin)
## 평균계산
bin_mean = np.mean(random_bin)
print(bin_mean)