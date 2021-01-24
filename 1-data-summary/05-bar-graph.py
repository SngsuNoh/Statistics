
import matplotlib.pyplot as plt

# 술자리 참석 상대도수 데이터 
labels = ['A', 'B', 'C', 'D', 'E']
ratio = [33,25,17,17,8]
    
#막대 그래프
fig, ax = plt.subplots()

plt.bar(labels, ratio)


##
plt.show()
fig.savefig("bar_plot.png")