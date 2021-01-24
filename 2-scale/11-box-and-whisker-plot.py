import numpy as np
import matplotlib.pyplot as plt

#카페인 함유량
coffee = np.array([202,177,121,148,89,121,137,158])

#상자그림
fig, ax = plt.subplots()
plt.boxplot(coffee)


##
plt.show()
fig.savefig("box_plot.png")