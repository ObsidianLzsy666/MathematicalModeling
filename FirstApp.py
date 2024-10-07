import pulp

# Create a LP Minimization problem
Lp_prob = pulp.LpProblem('Problem', pulp.LpMinimize)

# Create problem Variables
x = pulp.LpVariable("x", lowBound = 0) # Create a variable x >= 0
y = pulp.LpVariable("y", lowBound = 0) # Create a variable y >= 0

# Objective Function
Lp_prob += 3 * x + 5 * y

# Constraints:
Lp_prob += 2 * x + 3 * y >= 12
Lp_prob += -x + y <= 3
Lp_prob += x >= 4
Lp_prob += y <= 3

# Display the problem
print(Lp_prob)
