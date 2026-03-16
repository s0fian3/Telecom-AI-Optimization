import numpy as np
import matplotlib.pyplot as plt

map_size = 10 #100 Km²

towers = np.array([
    [2, 8],  # Tower A 
    [5, 2],  # Tower B 
    [8, 7],   # Tower C 
    [6, 5]
])
num_users = 50
user_locations = np.random.rand(num_users, 2)*map_size

plt.figure(figsize=(10, 6))
plt.scatter(towers[:, 0], towers[:, 1], c='red', marker='^', s=300, label='5G Towers')
plt.scatter(user_locations[:, 0], user_locations[:, 1], c='blue', alpha=0.5, label='Users (Phones)')
plt.title("Simulating a Network Topology")
plt.legend()
# plt.grid(True)
plt.show()

