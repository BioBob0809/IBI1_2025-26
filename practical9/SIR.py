import numpy as np
import matplotlib.pyplot as plt

# Define model parameters
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

# Initialize SIR variables
S = [N - 1]
I = [1]
R = [0]

# Run the simulation
for t in range(time_steps):
    current_S = S[-1]
    current_I = I[-1]
    current_R = R[-1]

    # Calculate new infections and recoveries
    infection_prob = beta * (current_I / N)
    new_infected = np.random.binomial(current_S, infection_prob)
    new_recovered = np.random.binomial(current_I, gamma)

    # Update the counts
    next_S = current_S - new_infected
    next_I = current_I + new_infected - new_recovered
    next_R = current_R + new_recovered

    S.append(next_S)
    I.append(next_I)
    R.append(next_R)

# Plot the results
plt.figure(figsize=(8, 5), dpi=120)
plt.plot(S, label='Susceptible', color='blue')
plt.plot(I, label='Infected', color='red')
plt.plot(R, label='Recovered', color='green')

plt.xlabel('Time Step')
plt.ylabel('Number of Individuals')
plt.title('Stochastic SIR Model Simulation')
plt.legend()
plt.grid(alpha=0.3)

plt.savefig('SIR_simulation.png', bbox_inches='tight')
plt.show()