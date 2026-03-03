hourly_rate = float(input("Enter hourly rate: "))
hours = float(input("Enter total hours worked: "))
minutes = float(input("Enter additional minutes: "))

decimal_hours = hours + (minutes / 60)
total_payment = decimal_hours * hourly_rate

print("Total payment:", total_payment)