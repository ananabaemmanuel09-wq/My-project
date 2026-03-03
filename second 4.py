distance = float(input("Enter travel distance (km): "))
km_per_liter = 40
fuel_price = 13000

liters_needed = distance / km_per_liter
total_cost = liters_needed * fuel_price

print("Total fuel cost:", total_cost)