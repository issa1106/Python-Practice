# 非監督式學習 分群演算法
# 分群演算法的績效可以使用 Silhouette 係數或 WSS / BSS
from sklearn import cluster, datasets, metrics
import matplotlib.pyplot as plt

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# KMean演算法
kmeans_fit = cluster.KMeans(n_clusters=3).fit(iris_X)
cluster_labels = kmeans_fit.labels_
print("分群結果:")
print(cluster_labels)
print("真實品種:")
print(iris_y)

# 精確度 績效silhouette_score
silhoutte_avg = metrics.silhouette_score(iris_X, cluster_labels)
print(silhoutte_avg)

# 增加分群數看看效果
silhouttes = []
ks = range(2, 10)
for k in ks:
	Kmeans_fit = cluster.KMeans(n_clusters=k).fit(iris_X)
	cluster_labels = Kmeans_fit.labels_
	silhoutte_avg = metrics.silhouette_score(iris_X, cluster_labels)
	silhouttes.append(silhoutte_avg)

print(silhouttes)
plt.bar(ks, silhouttes)
plt.show()

# Hierarchical Clustering 分類
hclust = cluster.AgglomerativeClustering(linkage='ward',
	affinity="euclidean", n_clusters=3)
hclust.fit(iris_X)
cluster_Agg_labels = hclust.labels_
print(cluster_Agg_labels)

silhoutte_hclust_avg = metrics.silhouette_score(iris_X, cluster_Agg_labels)
print(silhoutte_hclust_avg)
