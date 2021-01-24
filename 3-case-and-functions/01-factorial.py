# ! 함수 정의 
def fac(n): 
    if n==0: return 1
    elif n==1: return 1
    else: return n*fac(n-1)
    
print(fac(4))