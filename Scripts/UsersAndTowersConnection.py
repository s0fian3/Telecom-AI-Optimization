from UsersAndTowersMap import *

tower_capacity = 10
tower_load = [0, 0, 0, 0] 
final_assignments = []

for user in user_locations:
    # Get distances to all towers and sort them (closest to farthest)
    distances = np.linalg.norm(towers - user, axis=1)
    sorted_tower_indices = np.argsort(distances) 
    
    assigned = False
    for idx in sorted_tower_indices:
        if tower_load[idx] < tower_capacity:
            final_assignments.append(idx)
            tower_load[idx] += 1
            assigned = True
            break
            
    if not assigned:
        final_assignments.append(-1) 

plt.figure(figsize=(10, 6))
for i, t in enumerate(towers):
    color = 'red' if tower_load[i] >= tower_capacity else 'green'
    plt.scatter(t[0], t[1], c=color, marker='^', s=400, label=f'Tower {i} (Load: {tower_load[i]}/{tower_capacity})')

for i, user in enumerate(user_locations):
    t_idx = final_assignments[i]
    if t_idx != -1:
        plt.scatter(user[0], user[1], alpha=0.8, s=20)
        plt.plot([user[0], towers[t_idx][0]], [user[1], towers[t_idx][1]], alpha=0.1, color='gray')
    else:
        # Mark users who couldn't connect (Dropped calls)
        plt.scatter(user[0], user[1], c='black', marker='x', s=50, label='Dropped' if i==0 else "")

plt.title("Load Balancing & Capacity Constraints\nRed = Full Capacity | Black X = Dropped Call")
plt.legend(loc='upper right', fontsize='small')
plt.show()