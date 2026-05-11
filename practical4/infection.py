# Pseudocode
# 1. Define initial parameters:
#    - total_students = 91 (the whole class size)
#    - initial_infected = 5 (number of initially infected students)
#    - growth_rate = 0.4 (40% daily growth rate)
#    - day = 1 (start counting from day 1)
# 2. While the number of infected students is less than total_students:
#    a. Print the current number of infected students for this day
#    b. Calculate the new number of infected students: new_infected = infected * (1 + growth_rate)
#    c. Round the new number to the nearest whole number
#    d. If the new number exceeds total_students, set it to total_students
#    e. Increment the day counter
# 3. After the loop ends, print the total number of days taken to infect all students

# Parameters
total_students = 91
infected = 5
growth_rate = 0.4
day = 1

print("Day | Number of infected students")
print("-------------------------------")

# Loop while not all students are infected
while infected < total_students:
    # Print current day's infected count
    print(f"{day:3} | {infected}")
    
    # Calculate next day's infected count
    infected = round(infected * (1 + growth_rate))
    
    # Cap at total students if needed
    if infected > total_students:
        infected = total_students
    
    day += 1

# Print the final day when all are infected
print(f"{day:3} | {infected}")

print(f"\nIt took {day} days for all {total_students} students to become infected.")