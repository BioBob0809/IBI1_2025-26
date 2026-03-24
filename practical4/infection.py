# --------------------------
# PSEUDOCODE
# --------------------------
# 1. Define initial parameters:
#    - total_students = 91 (the whole class size)
#    - a = the number of initiative infected students that is inputed 
#    - growth_rate = 0.4 (40% daily growth rate)
#    - day = 1 (start counting from day 1)
# 2. While the number of infected students is less than total_students:
#    a. Print the current number of infected students for this day
#    b. Calculate the new number of infected students: new_infected = infected * (1 + growth_rate)
#    c. Round the new number to the nearest whole number (since we can't have partial people)
#    d. If the new number exceeds total_students, set it to total_students (to cap at full class)
#    e. Increment the day counter
# 3. After the loop ends, print the total number of days taken to infect all students
# --------------------------

a = int(input("The number of initiative infected students is："))
growth_rate = 0.4
day = 1
while a <= 91:
    pri_a = a
    a = a*(1+growth_rate)
    a = round (a)
    if a > 91:
        print ("Number of infected students：", 91-pri_a,)
    else:
        print ("Number of infected students：",a-a/1.4, )
    day +=1
print (f"It took {day} days for all 91 students to become infected.7")


# Result:

# The number of initiative infected students is：5
# Number of infected students： 2.0
# Number of infected students： 2.8571428571428568
# Number of infected students： 4.0
# Number of infected students： 5.7142857142857135
# Number of infected students： 8.0
# Number of infected students： 11.142857142857142
# Number of infected students： 15.714285714285715
# Number of infected students： 22.0
# Number of infected students： 14
# It took 10 days for all 91 students to become infected.