# PSEUDOCODE (as comments)
# 1. Get user input:
#    - age (in years): integer
#    - weight (in kg): integer
#    - gender: string ("male" or "female")
#    - concentration (µmol/l): integer
# 2. Validate input ranges:
#    - age must be between 1 and 100
#    - weight must be between 1 and 200 kg
#    - concentration must be between 1 and 1000 µmol/l
#    - gender must be either "male" or "female"
# 3. If all inputs are valid:
#    a. Calculate CrCl using Cockcroft-Gault equation:
#       - For male: CrCl = ((140 - age) * weight) / (72 * concentration)
#       - For female: CrCl = ((140 - age) * weight * 0.85) / (72 * concentration)
#    b. Print the calculated CrCl value
# 4. If any input is invalid:
#    a. Print a specific error message indicating which input is out of range

# Get user input
age = int(input("Please enter your age (years): "))
weight = int(input("Please enter your weight (kg): "))
gender = input("Please enter your gender (male/female): ").strip().lower()
concentration = int(input("Please enter your Cr concentration (µmol/l): "))

# Initialize validation flags and error message
valid = True
error_message = ""

# Validate each input individually for clear feedback
if not (1 <= age <= 100):
    valid = False
    error_message += "Age must be between 1 and 100.\n"
if not (1 <= weight <= 200):
    valid = False
    error_message += "Weight must be between 1 and 200 kg.\n"
if not (1 <= concentration <= 1000):
    valid = False
    error_message += "Concentration must be between 1 and 1000 µmol/l.\n"
if gender not in ["male", "female"]:
    valid = False
    error_message += "Gender must be 'male' or 'female'.\n"

# If all inputs are valid, calculate and print the result
if valid:
    if gender == "male":
        crcl = ((140 - age) * weight) / (72 * concentration)
    else:  # female
        crcl = ((140 - age) * weight * 0.85) / (72 * concentration)
    print(f"Your creatine clearance rate is: {crcl:.2f} mL/min")
else:
    # Print specific error messages
    print("Invalid input detected:")
    print(error_message)

