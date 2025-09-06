"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

user_age = int(input("\nPlease enter your age: "))

maximum_rate = 220 - user_age
upper_range = maximum_rate * 0.85
lower_range = maximum_rate * 0.65

print(f"\nWhen you exercise to strengthen your heart, you should keep your heart rate between {lower_range:.0f} and {upper_range:.0f}   beats per minute.\n")
