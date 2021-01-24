from itertools import product
from itertools import combinations_with_replacement as cwr

# 중복조합

re_com = list(cwr(["a","b","c","d","e"],3))
re_com_num = len(re_com)

print(re_com)
print(re_com_num)