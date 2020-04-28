from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
import math
import matplotlib as mpl


DATASET = 'crime_H.csv'
PREDICT = 'predict.csv'
# Set number of days to plot
Day = 30
Hour = 24


dataframe = read_csv(DATASET, usecols=['Type'])
predframe = read_csv(PREDICT, usecols=['Predict'])


# Concatenate known data and predicted data
dataset = dataframe.values
predict = predframe.values
print(dataset.shape, predict.shape)
dataset = np.concatenate((dataset, predict), axis = 0)
print(dataset.shape)
#print(dataframe['Type'].shape, dataset.shape)
#dataset = dataset[:math.floor(dataset.shape[0]/24)*24]


# day, hour and crime numbers will be plotted on X, Y and Z axes
day = []
hour = []
for i in range(Day):
	for j in range(Hour):
		day.append(i+1)
		hour.append(j)

day = np.array(day)
hour = np.array(hour)
crimes = dataset[dataset.shape[0]-Day*Hour: dataset.shape[0], 0]

#print(day.shape, hour.shape, crimes.shape)

fig = plt.figure(figsize=(25,14))
ax = fig.gca(projection='3d')

#plt.xlabel('Day')
#plt.ylabel('Hour')

# Set x_tick according to number of days
#x_tick = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
x_tick = ['A month ago', '2 weeks ago', 'Now']
plt.xticks(np.linspace(0, Day, len(x_tick)), x_tick)
y_tick = ['0:00', '6:00', '12:00', '18:00', '24:00']
plt.yticks(np.linspace(0, Hour, len(y_tick)), y_tick)
#plt.title('crimes = f(day, hour)')

# 3D plot and scale figure
surf = ax.plot_trisurf(day, hour, crimes, cmap='rainbow', linewidth=0.01)
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1, 0.8, 0.8, 1]))

# Hidden z axis
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])

fig.colorbar(surf, shrink=0.3, aspect=10)
#cbaxes = fig.add_axes([0.8, 0.2, 0.012, 0.3])
#cb = plt.colorbar(surf, cax = cbaxes)

# Recent data in front
ax.view_init(45, -45)

#plt.savefig('vis.png', dpi = 300, bbox_inches='tight')
plt.show()

