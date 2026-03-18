# Cell Tower Load Optimization Lab

![AI](Screenshot_2026-03-18_21_51_34.png)
![Heuristic](Screenshot_2026-03-18_21_50_50.png)

**Objective:** Simulating user distribution to understand Handover and Load Balancing.

**Tools:** Python, NumPy, Matplotlib, Scikit-learn, Virtual Environments.

**Features:** 
- Implemented Distance-Based Cell Association
- Calculated "Average Connection Distance" as a proxy for signal quality
- Load Balancing & Congestion Management.

**Logic:**
1. Implemented a capacity and distance-constrained assignment algorithm.
2. Then Modified it to be AI-driven. The AI ensures there are a minimum of handovers to optimize the network by calculating the centroid of the clusters on each frame.