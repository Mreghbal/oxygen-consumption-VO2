# Constants
MALE_CONSTANT = 3.5
FEMALE_CONSTANT = 1.833

def calculate_vo2(weight, age, gender):
    # Calculate VO2 based on gender
    if gender.lower() == 'male':
        constant = MALE_CONSTANT
    elif gender.lower() == 'female':
        constant = FEMALE_CONSTANT
    else:
        raise ValueError("Invalid gender provided.")

    # Calculate VO2
    vo2 = weight * constant

    # Adjust VO2 based on age
    adjusted_vo2 = vo2 - (0.035 * age)

    return adjusted_vo2

# Test the function
weight = float(input("Enter weight (in kg): "))
age = int(input("Enter age: "))
gender = input("Enter gender (Male/Female): ")

result = calculate_vo2(weight, age, gender)
print("VO2:", result)
