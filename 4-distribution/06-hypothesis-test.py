import numpy as np 
import scipy as sp
from scipy import stats

# 모평균 가설검정
## 1) seed 설정 seed = 0
np.random.seed(seed=0)
## 2) 샘플 추출
random_nor = np.random.normal(100,5,10)
print(random_nor)

# 평균 계산
nor_mean = np.mean(random_nor)
print(nor_mean)

## 3) 모평균 가설 검정 함수 정의
def ztest(stat, mu, sigma):
    z = (stat.mean()-mu)/(sigma*np.sqrt(len(stat)))
    return(2*(1-sp.stats.norm.cdf(z)))

## 4) 모평균 가설 검정
mu_test = ztest(random_nor,100,10)
print(mu_test)