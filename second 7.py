import math

people = int(input("Enter number of people: "))
daily_need_per_person = 2.5
gallon_size = 19
gallon_price = 19000

weekly_need = people * daily_need_per_person * 7
gallons_needed = math.ceil(weekly_need / gallon_size)
total_budget = gallons_needed * gallon_price

print("Weekly water requirement (liters):", weekly_need)
print("Gallons needed:", gallons_needed)
print("Total budget:", total_budget)