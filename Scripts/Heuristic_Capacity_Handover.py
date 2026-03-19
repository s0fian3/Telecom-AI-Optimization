import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

towers = np.array([[2, 8], [5, 2], [8, 7], [6, 5]])
num_users = 60 
tower_capacity = 12   
MAX_RANGE = 3   
tower_colors = ['purple', 'blue', 'green', 'orange']
user_locs = np.random.rand(num_users, 2) * 10

# KPI Trackers
total_handovers = 0
prev_assignments = np.full(num_users, -1)

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

for i, pos in enumerate(towers):
    circle = Circle((pos[0], pos[1]), MAX_RANGE, color=tower_colors[i], alpha=0.05, zorder=1)
    ax.add_patch(circle)

tower_scatter = ax.scatter(towers[:, 0], towers[:, 1], c='black', marker='^', s=300, zorder=5, edgecolors='black', linewidth=2, label="Cell Towers")
user_scatter = ax.scatter([], [], s=35, zorder=4, linewidth=0.5)
lines = [ax.plot([], [], alpha=0.2, linewidth=1)[0] for _ in range(num_users)]
ax.legend(loc='upper right')

def update_network(_):
    global user_locs, total_handovers, prev_assignments
    
    user_locs += np.random.normal(0, 0.3, size=(num_users, 2))
    user_locs = np.clip(user_locs, 0, 40)
    
    tower_load = [0] * len(towers)
    current_colors = []
    current_assignments = np.full(num_users, -1)
    distances_sum = 0
    connected_count = 0
    
    for i in range(num_users):
        user = user_locs[i]
        distances = np.linalg.norm(towers - user, axis=1)
        sorted_indices = np.argsort(distances)
        
        assigned_idx = -1
        for idx in sorted_indices:
            # CHECK: is it in range? AND is there room?
            if distances[idx] < MAX_RANGE and tower_load[idx] < tower_capacity:
                assigned_idx = idx
                tower_load[idx] += 1
                current_assignments[i] = idx
                distances_sum += distances[idx]
                connected_count += 1
                break
        
        if assigned_idx != -1:
            lines[i].set_data([user[0], towers[assigned_idx][0]], 
                             [user[1], towers[assigned_idx][1]])
            lines[i].set_color(tower_colors[assigned_idx])
            current_colors.append(tower_colors[assigned_idx])
        else:
            lines[i].set_data([], []) 
            current_colors.append('black') 

    #  KPI CALCULATIONS  
    # Avg Distance
    avg_dist = distances_sum / connected_count if connected_count > 0 else 0
    
    # Handover Count (Only if switching between two valid towers)
    handovers = np.sum((current_assignments != prev_assignments) & (prev_assignments != -1) & (current_assignments != -1))
    total_handovers += handovers
    prev_assignments = current_assignments.copy()
    
    # Congestion Rate (Users in "Black" / Total Users)
    congestion_rate = ((num_users - connected_count) / num_users) * 100

    user_scatter.set_offsets(user_locs)
    user_scatter.set_facecolors(current_colors)
    
    # congested towers in RED
    t_edge_colors = ['red' if load >= tower_capacity else 'black' for load in tower_load]
    tower_scatter.set_edgecolors(t_edge_colors)
    
    return avg_dist, total_handovers, congestion_rate

plt.ion()
for step in range(100):
    avg_d, total_h, cong = update_network(step)
    ax.set_title(f"Cell Network SIM | Step: {step} | Avg Dist: {avg_d:.2f} Km | Handovers: {total_h} | Congestion: {cong:.1f}%", fontsize=11)
    plt.pause(0.3)

plt.ioff()
plt.show()