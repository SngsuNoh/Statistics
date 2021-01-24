from sympy.stats import given, density, Die

## 6개의 면이 있는 주사위 생성
Die6 = Die("Die6", 6)
Die6_dict = density(Die6).dict
print(Die6)
print(Die6_dict)


## 3 초과의 면만 나오는 조건을 가진 주사위 생성
condi = given(Die6, Die6>3)
condi_dict = density(condi).dict
print(condi)
print(condi_dict)