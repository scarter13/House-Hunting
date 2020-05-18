hours_worked = float (input("Enter Hours Worked: "))
hourly_rate = float (input("Enter Hourly Rate: "))
#if you worked more than 40
if hours_worked > 40:
    overtime = hours_worked - 40
    wages = (40* hourly_rate + overtime * hourly_rate * 1.5)
else:
    wages = hours_worked * hourly_rate

print ("Total: $", wages)