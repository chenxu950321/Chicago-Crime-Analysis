import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics

csvReader = open("/Users/apple/Downloads/THEFT_cleaned.csv", "r")
reader = csv.reader(csvReader)

y_num=1466908
X = []
for item in reader:
    tmp = [float(item[0]),float(item[1])]
    X.append(tmp)
X = np.array(X)
print(type(X[0,0]))

y = np.zeros(y_num)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.plot(X[:,0],X[:,1])
# plt.xlim((-3, 3))
# plt.ylim((-3, 3))
# my_x_ticks = np.arange(-3, 3, 0.5)
# my_y_ticks = np.arange(-3, 3, 0.5)
# plt.xticks(my_x_ticks)
# plt.yticks(my_y_ticks)

plt.scatter(X[:, 0], X[:, 1], c=y, marker=".")
# plt.xlim(0.5, 1.1)
# plt.ylim(-1, -0.4)
# plt.xlim(-1, -0.4)
# plt.ylim(0.5, 1.1)
# plt.show()



# find best k
# nlist = range(8,100)
# max = 0
# max_score = 0
# # max = 99
# # max_score = 562699.3775056591
# for index, k in enumerate(nlist):
#     y_pred = KMeans(n_clusters=k, random_state=9).fit_predict(X)
#     # plt.scatter(X[:, 0], X[:, 1], c=y_pred)
#     # plt.show()
#     # print(k, metrics.calinski_harabasz_score(X, y_pred))
#
#     score = metrics.calinski_harabasz_score(X, y_pred)
#     if max_score < score:
#         max_score = score
#         max = k
#     print('Stll running... k=', k, ' score= ', score)
#
# print('Best K and socre:')
# print(max, max_score)

y_pred = KMeans(n_clusters=99, random_state=9).fit_predict(X)
print("finished")
print(metrics.calinski_harabasz_score(X, y_pred))
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()

# print(y_pred.shape)

csvReader.close()

csvWriter = open("/Users/apple/Downloads/rst_THEFT.csv", "w")
reader_w = csv.writer(csvWriter)

i = 0
while i<y_num:
    tmp = [X[i,0], X[i,1], y_pred[i]]
    reader_w.writerow(tmp)
    i += 1


csvWriter.close()