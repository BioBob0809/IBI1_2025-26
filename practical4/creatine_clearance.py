# --------------------------
# PSEUDOCODE (as comments)
# --------------------------
# 1. Get user input:
#    - age (in years): integer
#    - weight (in kg): integer
#    - gender: string ("male" or "female")
#    - concentration (µmol/l): integer
# 2. Validate input ranges:
#    - age < 100
#    - 20 < weight < 80
#    - 0 < concentration < 100
#    - gender is either "male" or "female"
# 3. If all inputs are valid:
#    a. Calculate CrCl using Cockcroft-Gault equation:
#       - For male: CrCl = ((140 - age) * weight) / (72 * concentration)
#       - For female: CrCl = ((140 - age) * weight * 0.85) / (72 * concentration)
#    b. Print the calculated CrCl value
# 4. If any input is invalid:
#    a. Print an error message indicating which input is out of range

age = int(input("Please enter your age (years): "))
weight = int(input("Please enter your weight (kg): "))
gender = input("Please enter your gender (male/female): ")
concentration = int(input("Please enter your Cr concentration (µmol/l): "))
if age < 100 and 20 < weight < 80 and 0 < concentration < 100 and gender == "male" or gender == "female":
    if gender == "male":
        CrCl = ((140-age)*weight)/(72*concentration)
    else:
        CrCl = ((140-age)*weight*0.85)/(72*concentration) 
    print (f"Your creatine clearance rate is{CrCl}")
else:
    print ("Sorry, your input data is invalid. Cannot calculate creatine clearance rate.")

# RESULT
# Please enter your age (years): 18
# Please enter your weight (kg): 70
# Please enter your gender (male/female): male
# Please enter your Cr concentration (µmol/l): 80
# Your creatine clearance rate is1.4826388888888888

