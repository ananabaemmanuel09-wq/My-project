import math

length = float(input("Enter room length (m): "))
width = float(input("Enter room width (m): "))
height = float(input("Enter room height (m): "))

wall_area = 2 * (length * height) + 2 * (width * height)
paint_coverage = 10

cans_needed = math.ceil(wall_area / paint_coverage)

print("Total wall area:", wall_area)
print("Paint cans needed:", cans_needed)