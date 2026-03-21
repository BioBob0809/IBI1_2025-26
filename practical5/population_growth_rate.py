UK_20 = 66.7
UK_24 = 69.2
China_20 = 1426
China_24 = 1410
Italy_20 = 59.4
Italy_24 = 58.9
Brazil_20 = 208.6
Brazil_24 = 212.0
USA_20 = 331.6
USA_24 = 340.1
pre_UK = (UK_24-UK_20)/UK_20*100
print (f"The percent change of UK is {pre_UK:.2f}%")
pre_China = (China_24-China_20)/China_20*100
print (f"The percent change of China is {pre_China:.2f}%")
pre_Italy = (Italy_24-Italy_20)/Italy_20*100
print (f"The percent change of Italy is {pre_Italy:.2f}%")
pre_Brazil = (Brazil_24-Brazil_20)/Brazil_20*100
print (f"The percent change of Brazil is {pre_Brazil:.2f}%")
pre_USA = (USA_24-USA_20)/USA_20*100
print (f"The percent change of USA is {pre_USA:.2f}%")

changes = [("UK", pre_UK),("China", pre_China),("Italy", pre_Italy),("Brazil", pre_Brazil),("USA", pre_USA)]
sorted_changes = sorted(changes, key=lambda x: x[1], reverse=True)
print("Population changes in descending order:")
for country, change in sorted_changes:
    print(f"{country}: {change:.2f}%")
largest_increase = sorted_changes [0][0]
largest_decrease = sorted_changes [-1][0]
print (f"The country with the largest increase in population is {largest_increase}.")
print (f"The country with the largest decrease in population is {largest_decrease}.")

import numpy as np
import matplotlib.pyplot as plt
population_changes = {"UK":pre_UK, "China":pre_China, "Italy":pre_Italy, "Brazil":pre_Brazil, "USA":pre_USA}
country = list(population_changes.keys())
percent_change = list (population_changes.values())
plt.xlabel ("Countries")
plt.ylabel ("Percent Changes / %")
plt.title ("5 Countries' Population Growth Rate from 2020 to 2024")
bars = plt.bar(x=country, height=percent_change)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.2f}%",
        ha='center',
        va='bottom' if height > 0 else 'top'
    )
plt.axhline(y=0, color='black', linewidth=0.8)
plt.tight_layout()

plt.show ()






  