#CTI-110
#P4HW1- Score List
#Kristopher Williams
#07/06/2023
#

grade_list = []
num = int(input("How many scores do you want to enter? "))
print()

for i in range (1, num + 1):
        score = float(input(f'Enter Score #{i}: '))
        while score < 0 or score > 100:
            print("Invalid input!")
            score = float(input(f'Enter Score #{i}: '))
        grade_list.append(score)
        
lowest = min(grade_list)
highest = max(grade_list)
sum1 = sum(grade_list)
average = sum(grade_list) / len(grade_list)
print()

print("-"*12,"Results", "-"*12)
print("Lowest Score: ", lowest)
grade_list.remove(lowest)
print("Modified List: ", grade_list)
avg = sum(grade_list)/ len(grade_list)
print("Score Average: ", format(avg, ',.2f'))
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
print("Grade: " f'{letter}')
print('-'*50)

print(input("Press any key to terminate"))
