total_bill = 347500
tax_rate = 0.10
people = 4

total_after_tax = total_bill + (total_bill * tax_rate)
per_person = total_after_tax / people

print("Total after tax:", total_after_tax)
print("Each person pays:", per_person)