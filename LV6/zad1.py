from sklearn import datasets, cluster, preprocessing, model_selection
import numpy as np
import matplotlib.pyplot as plt

def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

X = generate_data(500, 1)

kmeans = cluster.KMeans(n_clusters=3, random_state=365, n_init="auto")
kmeans.fit(X);

centers = kmeans.cluster_centers_
# kmeans.predict();

colors = ['red', 'blue', 'green']
labels = kmeans.labels_

plt.figure(figsize=(8, 6))
for i in range(kmeans.n_clusters):
    cluster_points = X[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], color=colors[i])
    
plt.scatter(centers[:, 0], centers[:, 1], c='gray', edgecolors="black")
plt.grid(True)
plt.show()