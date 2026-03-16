from TowersAndUsersMap import *

assignments = [] # To store which tower each user belongs to
total_distance = 0

for user in user_locations:
    distances = np.linalg.norm(towers-user, axis=1)
    
    # Find the index of the closest tower (0, 1, or 2)
    min = np.argmin(distances)
    closest_tower_idx = min
    assignments.append(closest_tower_idx)
    total_distance += distances[closest_tower_idx]
    

avg_distance = total_distance / num_users


# Visualization 
plt.figure(figsize=(10, 6))
colors = ['red', 'green', 'purple', 'black']

# Plot Towers
for i, t in enumerate(towers):
    plt.scatter(t[0], t[1], c=colors[i], marker='^', s=300, label=f'Tower {i}')

# Plot Users and Draw Lines to their assigned tower
for i, user in enumerate(user_locations):
    t_idx = assignments[i]
    plt.scatter(user[0], user[1], c=colors[t_idx], alpha=0.5, s=20)
    plt.plot([user[0], towers[t_idx][0]], [user[1], towers[t_idx][1]], c=colors[t_idx], alpha=0.1, linestyle='--')

plt.title(f"User-to-Tower Association\nAvg Connection Distance: {avg_distance:.2f}km")
plt.legend()
plt.show()



