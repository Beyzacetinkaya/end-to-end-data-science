import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
df = pd.read_csv("model_data.csv").drop('target', axis=1)
pca = PCA(n_components=2)
reduced = pca.fit_transform(df)
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(reduced)
plt.scatter(reduced[:, 0], reduced[:, 1], c=clusters, cmap='viridis')
plt.title("K-Means Clusters")
plt.show()