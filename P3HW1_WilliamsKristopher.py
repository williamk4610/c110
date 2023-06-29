# This program takes a number grade , determines average and displays letter grade for average.
#6/28/2023
#CTI-110 P3HW1 - Debugging
# Williams Kristopher

# Enter grades for six modules

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1,mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6
avg = sum / 6

print("-"*12,"Results", "-"*12)
print("Lowest Grade: " f'{low:.1f}')
print("Highest Grade: " f'{high:.1f}')
print("Sum of Grades: " f'{sum:.1f}')
print("Average: " f'{avg:.2f}')
print("-"*30)
# determine letter grade for average


if avg >= 90:
    letter = 'A'
elif avg >= 80:
    letter = 'B'
elif avg >= 70:
    letter = 'C'
elif avg >= 60:
    letter = 'D'
else:
    letter = 'F'
print("Your grade is: " f'{letter}')
# TO DO: finish this





