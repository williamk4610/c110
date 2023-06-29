# CTI-110
# P3HW2 - Salary
# Williams Kristopher
# 6/28/2023
#Calculating Employee Salary w/Overtime

name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("-"*30)
print("Employee name:     " f'{name}')
print()
print("Hours Worked" "\t Pay Rate" "         OverTime" "\t OverTime Pay" "\t RegHour Pay" "\t Gross Pay")
print("-"*130)

if hours_worked >= 40:
    overtime = hours_worked - 40
else:
    overtime = 0

overtime_pay = overtime * (pay_rate * 1.5)

reg_pay = (hours_worked - overtime) * pay_rate
tot_pay = reg_pay + overtime_pay

print(f'{hours_worked:<30.1f}' f'{pay_rate:<20.1f}' f'{overtime:<23.1f}' f'{overtime_pay:<27.2f}' f'${reg_pay:<25.2f} 'f'${tot_pay}')



