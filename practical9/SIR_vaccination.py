import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Model parameters
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
vaccination_rates = np.arange(0, 101, 10)

plt.figure(figsize=(8, 5), dpi=120)
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

for idx, v_rate in enumerate(vaccination_rates):
    vaccinated = int(N * v_rate / 100)
    # Ensure initial_S is not negative
    initial_S = max(N - 1 - vaccinated, 0)
    initial_I = 1
    initial_R = 0

    S = [initial_S]
    I = [initial_I]
    R = [initial_R]

    for t in range(time_steps):
        current_S = S[-1]
        current_I = I[-1]
        current_R = R[-1]

        infection_prob = beta * (current_I / N) if N > 0 else 0
        new_infected = np.random.binomial(current_S, infection_prob) if current_S > 0 else 0
        new_recovered = np.random.binomial(current_I, gamma) if current_I > 0 else 0

        next_S = max(current_S - new_infected, 0)
        next_I = max(current_I + new_infected - new_recovered, 0)
        next_R = max(current_R + new_recovered, 0)

        S.append(next_S)
        I.append(next_I)
        R.append(next_R)

    plt.plot(I, color=colors[idx], label=f'{v_rate}%')

plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model with different vaccination rates')
plt.legend(title='Vaccination rate')
plt.grid(alpha=0.3)

plt.savefig('SIR_vaccination_plot.png', bbox_inches='tight')
plt.show()