import pandas as pd 
import numpy as np

# drink 데이터
drink = pd.read_csv("drink.csv")


#상대도수 계산
drink_relfreq = drink[drink["Attend"]==1]["Name"].value_counts(normalize=True)


print("상대도수 계산")
print(drink_relfreq)