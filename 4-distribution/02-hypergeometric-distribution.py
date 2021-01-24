import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats

# 초기하분포
[M, n, N] = [30,5,10]
stat_hyp = sp.stats.hypergeom(M,n,N)

# 그리기
fig, ax = plt.subplots()
x_axis = np.arange(n + 1) 
plt.bar(x_axis,stat_hyp.pmf(x_axis))


##
plt.show()
fig.savefig("pmf_plot.png")

# 초기하분포 cdf 
x_axis = np.arange(n + 1) 
plt.bar(x_axis,stat_hyp.cdf(x_axis))


##
plt.show()
fig.savefig("cdf_plot.png")

# 랜덤표본 추출
## seed 설정 seed = 0 
np.random.seed(seed=0)

## 랜덤 샘플 추출
random_hyp = np.random.hypergeometric(ngood=5,nbad=25,nsample=10,size=50)
print(random_hyp)
## 평균계산
hyp_mean = np.mean(random_hyp)
print(hyp_mean)
