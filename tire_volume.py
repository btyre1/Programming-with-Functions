import math
from datetime import datetime

w = int(input("\nEnter the width of the tire in mm (ex 205): "))
a = int(input("\nEnter the aspect ratio of the tire (ex 60): "))
d = int(input("\nEnter the diameter of the wheel in inches (ex 15): "))

volume = ((math.pi * w * w * a) * ((w * a) + 2540 * d)) / 10000000000
rounded_volume = round(volume, 2) 

print(f"\nThe approximate voume is {rounded_volume} liters.\n")

buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()

current_date_and_time = datetime.now().date()

with open('volumes.txt', 'at') as file:
    if buy_tires == "yes":
        phone_number = input("Please enter your phone number: ").strip()
        file.write(f"{current_date_and_time}, {w}, {a}, {d}, {rounded_volume}, {phone_number}\n")
    else:
        file.write(f"{current_date_and_time}, {w}, {a}, {d}, {rounded_volume}\n")

print("\nData has been appended to volumes.txt.\n")
