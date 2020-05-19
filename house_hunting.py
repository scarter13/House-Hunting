# Write your code here
annual_salary = float (input ("Enter your Annual Salary: "))
portion_saved = float (input ("Enter the percent of your salary to save, as a decimal: "))
r = input ("Enter the expected rate of annual return [0.04]: ")
if r == "":
    r = .04
else: 
    r = float(r)
total_cost = float (input ("Enter the cost of your dream home: "))
portion_down_payment = input ("Enter the percent of your home's cost to save as a down payment [0.25]: ")
if portion_down_payment == "":
    portion_down_payment = .25
else: 
    portion_down_payment = float(portion_down_payment)
current_savings = 0
down_payment = (total_cost * portion_down_payment)
monthly_income = (annual_salary / 12)
monthly_saved = (monthly_income * portion_saved)
i = 0

while current_savings < down_payment:
    current_savings = (current_savings + monthly_saved) + ((current_savings * r) / 12)
    i = i + 1
print ("Number of months: ", i)

