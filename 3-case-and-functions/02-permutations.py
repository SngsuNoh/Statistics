from itertools import permutations 
from itertools import combinations

# 순열 : 6명 학생 중 2명에게 순위별 상품을 주는 경우의 수 
rank_per = list(permutations(["가", "나", "다", "라", "마", "바"],2))
rank_per_num = len(rank_per)

print(rank_per)
print(rank_per_num)