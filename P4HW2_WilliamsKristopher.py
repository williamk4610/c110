# CTI-110
# P4HW2 - Salary Calculator
# Williams Kristopher
# 07/06/2023
#Calculating Employee Salary and overall payments overtime
#

emp_tot = []                        
over_tot = []                                   ##For tables to be created
reg_tot = []
gross_tot = []

                                                        ##Begin loop

while True:
	employee_name = input(str(f'Enter employees name or "Done" to terminate: '))
	if employee_name.lower() != 'done':
		emp_tot.append(employee_name)
		hours_worked = float(input(f'How many hours did {employee_name} work? '))
		pay_rate = float(input(f'what is {employee_name}\'s pay rate?'))
		
		print("-"*30)
		print("Employee name:     " f'{employee_name}')
		print()
		print("Hours Worked" "\t Pay Rate" "         OverTime" "\t OverTime Pay" "\t RegHour Pay" "\t Gross Pay")
		print("-"*130)
	
		if hours_worked >= 40:
				overtime = hours_worked - 40
		else:
				overtime = 0

		overtime_pay = overtime * (pay_rate * 1.5)
		over_tot.append(overtime_pay)

		reg_pay = (hours_worked - overtime) * pay_rate
		reg_tot.append(reg_pay)
		tot_pay = reg_pay + overtime_pay
		gross_tot.append(tot_pay)
   
		print(f'{hours_worked:<30.1f}' f'{pay_rate:<20.1f}' f'{overtime:<23.1f}' f'{overtime_pay:<27.2f}' f'${reg_pay:<25.2f} 'f'${tot_pay}')
		print()
	else:                               #prints totals of everything
		print()

		overall_emp = len(emp_tot)
		overall_overtime = sum(over_tot)
		overall_reg = sum(reg_tot)
		overall_gross = sum(gross_tot)
		
		print("Total number of employees entered: ", f'{overall_emp}')
		print("Total amount paid for overtime: ", f'${overall_overtime:.2f}')
		print("Total amount paid for regular hours: ", f'${overall_reg:.2f}')
		print("Total amount paid in gross: ", f'${overall_gross:.2f}')
		
		break            #Ends the loop

print()
print(input("Press any key to exit: ")) #Prevents program from closing
			
