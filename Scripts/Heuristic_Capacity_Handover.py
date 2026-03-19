import numpy as np
import matplotlib.pyplot as plt

# --- Setup ---
towers = np.array([[2, 8], [5, 2], [8, 7], [6, 5]])
num_users = 60  # Increased to 40 so you can actually see congestion (Total Cap is 48)
tower_capacity = 100
tower_colors = ['purple', 'blue', 'green', 'orange']
user_locs = np.random.rand(num_users, 2) * 10

# KPI Trackers
total_handovers = 0
prev_assignments = np.full(num_users, -1)

fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Initialize Visuals
tower_scatter = ax.scatter(towers[:, 0], towers[:, 1], c='black', marker='^', s=300, zorder=5, edgecolors='black', linewidth=2)
user_scatter = ax.scatter([], [], s=30, zorder=4)
lines = [ax.plot([], [], alpha=0.15, linewidth=1)[0] for _ in range(num_users)]

def update_network():
    global user_locs, total_handovers, prev_assignments
    
    # Move users
    user_locs += np.random.normal(0, 0.15, size=(num_users, 2))
    user_locs = np.clip(user_locs, 0, 10)
    
    tower_load = [0] * len(towers)
    current_colors = []
    current_assignments = np.full(num_users, -1)
    distances_sum = 0
    connected_count = 0
    
    for i in range(num_users):
        user = user_locs[i]
        # Calculate distances to all towers
        distances = np.linalg.norm(towers - user, axis=1)
        sorted_indices = np.argsort(distances)
        
        assigned_idx = -1
        for idx in sorted_indices:
            if tower_load[idx] < tower_capacity:
                assigned_idx = idx
                tower_load[idx] += 1
                current_assignments[i] = idx
                distances_sum += distances[idx]
                connected_count += 1
                break
        
        # Update connection lines and user colors
        if assigned_idx != -1:
            lines[i].set_data([user[0], towers[assigned_idx][0]], 
                             [user[1], towers[assigned_idx][1]])
            lines[i].set_color(tower_colors[assigned_idx])
            current_colors.append(tower_colors[assigned_idx])
        else:
            lines[i].set_data([], []) 
            current_colors.append('black') # Congested user

    # --- KPI CALCULATIONS ---
    # 1. Avg Distance (Proxy for RSRP)
    avg_dist = distances_sum / connected_count if connected_count > 0 else 0
    
    # 2. Handover Count (Stability)
    if prev_assignments is not None:
        # Change only if user was connected before and is connected now to a different tower
        handovers = np.sum((current_assignments != prev_assignments) & (prev_assignments != -1) & (current_assignments != -1))
        total_handovers += handovers
    prev_assignments = current_assignments.copy()
    
    # 3. Congestion Rate
    congestion_rate = ((num_users - connected_count) / num_users) * 100

    # Update Visuals
    user_scatter.set_offsets(user_locs)
    user_scatter.set_facecolors(current_colors)
    
    # Tower turns RED if at 100% capacity
    t_edge_colors = ['red' if load >= tower_capacity else 'black' for load in tower_load]
    tower_scatter.set_edgecolors(t_edge_colors)
    
    return avg_dist, total_handovers, congestion_rate

plt.ion()
for step in range(300):
    avg_d, total_h, cong = update_network()
    ax.set_title(f"Heuristic | Avg Dist: {avg_d:.2f} | Total Handovers: {total_h} | Congestion: {cong:.1f}%")
    plt.pause(0.15)

plt.ioff()
plt.show()