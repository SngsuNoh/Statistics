import numpy as np 
import scipy as sp
from scipy import stats

# 이항 검정
## 1) seed 설정 seed = 0
np.random.seed(seed=0)
## 2) 샘플 추출
random_ber = np.random.binomial(n=1,p=0.5,size=50)
print(random_ber)

n_ber = np.count_nonzero(random_ber)
print(n_ber)

## 3) 가설 검정
binom_test = sp.stats.binom_test(n_ber,50)
print(binom_test)
