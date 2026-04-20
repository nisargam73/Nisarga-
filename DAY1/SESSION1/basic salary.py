
basic = float(input("Enter basic salary: "))

hra = 0.20 * basic
da = 0.50 * basic
gross = basic + hra + da

pf = 0.12 * basic
tax = 0.10 * gross
total_deductions = pf + tax

net_salary = gross - total_deductions
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)
print("PF:", pf)
print("Tax:", tax)
print("Total Deductions:", total_deductions)
print("Net Salary:", net_salary)