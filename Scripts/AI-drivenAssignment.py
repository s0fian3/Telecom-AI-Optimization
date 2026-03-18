
# THIS CODE DOES NOT TAKE IN MIND CAPACITY

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

towers = np.array([[2, 8], [5, 2], [8, 7], [6, 5]])
num_users = 30
user_locs = np.random.rand(num_users, 2) * 10
kmeans = KMeans(n_clusters=4, init=towers, n_init=1)

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10); ax.set_ylim(0, 10)

ax.scatter(towers[:, 0], towers[:, 1], c='red', marker='^', s=200, label='Towers', zorder=5)

user_scatter = ax.scatter(user_locs[:, 0], user_locs[:, 1], s=50, cmap='viridis', zorder=4)
lines = [ax.plot([], [], color='gray', alpha=0.2, zorder=1)[0] for _ in range(num_users)]

plt.title("Dynamic AI Distance Handover")

for _ in range(500): 
    user_locs += np.random.normal(0, 0.2, size=(num_users, 2)) 
    user_locs = np.clip(user_locs, 0, 10)
    
    # AI Logic
    kmeans.fit(user_locs)
    assignments = kmeans.labels_
    
    #  Update Dots
    user_scatter.set_offsets(user_locs)
    user_scatter.set_array(assignments) 
    
    # Update Lines
    for i in range(num_users):
        tower_idx = assignments[i]
        # Draw line from user current pos to their assigned tower
        lines[i].set_data([user_locs[i, 0], towers[tower_idx, 0]], 
                         [user_locs[i, 1], towers[tower_idx, 1]])
    
    plt.pause(0.15) 

plt.show()