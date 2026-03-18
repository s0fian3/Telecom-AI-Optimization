from sklearn.cluster import KMeans
from UserAndTowerConnection import *
from UsersAndTowersMap import *
from LoadBalancingAndCapacity import *

kmeans = KMeans(n_clusters=4, init=towers, n_init=1) 

kmeans.fit(user_locations)

ai_assignments = kmeans.predict(user_locations)

plt.figure(figsize=(10, 6))
plt.scatter(user_locations[:, 0], user_locations[:, 1], c=ai_assignments, cmap='viridis', alpha=0.6)
plt.scatter(towers[:, 0], towers[:, 1], c='red', marker='^', s=200, label='Towers')
plt.title("AI-Driven User Clustering (K-Means)")
plt.show()