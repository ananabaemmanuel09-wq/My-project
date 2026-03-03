base_salary = 5000000
allowance = 750000
bpjs_rate = 0.02
tax_rate = 0.05

gross_salary = base_salary + allowance
deductions = gross_salary * (bpjs_rate + tax_rate)
net_salary = gross_salary - deductions

print("Net salary received:", net_salary)