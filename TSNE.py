import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt

Group1_data = [ ] # Load your Group 1 data here
Group2_data = [ ] # Load your Group 2 data here

temp_data = []
temp_data.append(Group1_data)
temp_data.append(Group2_data)
data = sum(temp_data, [])

# tsne_1d = TSNE(n_components=1, random_state=0)
# tsne_2d = TSNE(n_components=2, random_state=0)
tsne_3d = TSNE(n_components=3, random_state=0)

# data_1d = tsne_1d.fit_transform(data)
# data_2d = tsne_2d.fit_transform(data)
data_3d = tsne_3d.fit_transform(data)

pivot = len(Group2_data)

# 1D result
# zeros = [0]*len(data_1d)
# plt.scatter(data_1d[0:pivot], zeros[0:pivot], c='r', label="Old adult", marker='^')
# plt.scatter(data_1d[pivot:], zeros[pivot:], c='b', label="Stroke")
# plt.legend(loc='upper right')
# plt.show()

# 2D result
# plt.scatter(data_2d[0:pivot,0], data_2d[0:pivot,1], c='r', label="Old adult", marker='^')
# plt.scatter(data_2d[pivot:,0], data_2d[pivot:,1], c='b', label="Stroke")
# plt.legend(loc='upper right')
# plt.show()

# 3D result
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(data_3d[0:pivot,0], data_3d[0:pivot,1], data_3d[0:pivot,2], c='r', label="Old adult", marker='^')
ax.scatter(data_3d[pivot:,0], data_3d[pivot:,1], data_3d[pivot:,2], c='b', label="Stroke")
plt.legend(loc='upper right')
plt.show()
