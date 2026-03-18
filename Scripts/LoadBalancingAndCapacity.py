import numpy as np
import matplotlib.pyplot as plt

towers = np.array([[2, 8], [5, 2], [8, 7], [6, 5]])
num_users = 50
tower_capacity = 12 
user_locs = np.random.rand(num_users, 2) * 10

tower_colors = ['purple', 'blue', 'green', 'orange']

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

tower_scatter = ax.scatter(towers[:, 0], towers[:, 1], marker='^', s=300, zorder=5)

user_scatter = ax.scatter([], [], s=30, zorder=4)
lines = [ax.plot([], [], alpha=0.15, linewidth=1)[0] for _ in range(num_users)]

def update_network():
    global user_locs
    user_locs += np.random.normal(0, 0.08, size=(num_users, 2))
    user_locs = np.clip(user_locs, 0, 10)
    
    tower_load = [0] * len(towers)
    current_colors = []
    
    for i in range(num_users):
        user = user_locs[i]
        distances = np.linalg.norm(towers - user, axis=1)
        sorted_indices = np.argsort(distances)
        
        assigned_idx = -1
        for idx in sorted_indices:
            if tower_load[idx] < tower_capacity:
                assigned_idx = idx
                tower_load[idx] += 1
                break
        
        # line and user color
        if assigned_idx != -1:
            lines[i].set_data([user[0], towers[assigned_idx][0]], 
                             [user[1], towers[assigned_idx][1]])
            lines[i].set_color(tower_colors[assigned_idx])
            current_colors.append(tower_colors[assigned_idx])
        else:
            lines[i].set_data([], []) 
            current_colors.append('black') 

    user_scatter.set_offsets(user_locs)
    user_scatter.set_facecolors(current_colors)
    
    t_colors = ['red' if load >= tower_capacity else 'black' for load in tower_load]
    tower_scatter.set_edgecolors(t_colors)

plt.ion()
for step in range(300):
    update_network()
    ax.set_title(f"Dynamic Heuristic Load Balancing - Step {step}")
    plt.pause(0.1)

plt.ioff()
plt.show()