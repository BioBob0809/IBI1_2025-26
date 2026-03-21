heart_rates = [72,60,126,85,90,59,76,131,88,121,64]
count = 0
for i in heart_rates:
    count += 1
print (f"There are {count} patients in dataset")
average_heart_rate = sum(heart_rates)/len(heart_rates)
print (f"The mean heart rate is {average_heart_rate}")

count_low = 0
count_normal = 0
count_high = 0
for i in heart_rates:
    if i < 60:
        count_low += 1
    elif 60 <= i <= 120:
        count_normal += 1
    else:
        count_high += 1
print (f"{count_low} patients' heart rates are low. {count_normal} patients' heart rates are normal. {count_high} patients' heart rates are high. ")
if count_low > count_normal and count_low > count_high:
    print ("The cotegory that contains the most patients are low category.")
elif count_normal > count_low and count_normal > count_high:
    print ("The cotegory that contains the most patients are normal category.")           
else:
    print ("The cotegory that contains the most patients are high category.") 

import matplotlib.pyplot as plt
categories = ["Low(<60 bpm)","Normal(60-120 bpm)","High(>120 bpm)"]
count = [count_low,count_normal,count_high]
plt.pie (count,labels=categories,autopct='%1.1f%%',startangle = 90)
plt.title("Distribution of Resting Heart Rate Categories")
plt.axis('equal')
plt.show ()


