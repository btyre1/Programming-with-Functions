from datetime import datetime

def main():
    
    gender = input("\nPlease enter your gender (M or F): ").upper()
    birth_str = input("\nEnter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("\nEnter your weight in U.S. pounds: "))
    inches = float(input("\nEnter your height in U.S. inches: "))

    age = compute_age(birth_str)
    weight = kg_from_lb(pounds)
    height = cm_from_in(inches)
    bmi = body_mass_index(weight, height)
    bmr = basal_metabolic_rate(gender, weight, height, age)

    print(f"\nAge (years): {age}")
    print(f"\nWeight (kg): {weight:.2f}")
    print(f"\nHeight (cm): {height:.1f}")
    print(f"\nBody mass index: {bmi:.1f}")
    print(f"\nBasal metabolic rate (kcal/day): {bmr:.0f}\n")

    pass

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year

    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = pounds * 0.45359237

    return kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = inches * 2.54

    return cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / (height ** 2)

    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == "F":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    elif gender == "M":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

    return bmr

main()
