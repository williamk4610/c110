''' Type your code here. '''
mpg = float(input())
dollars_per_gallon = float(input())

dollars_20_miles = 20 * dollars_per_gallon / mpg
dollars_75_miles = 75 * dollars_per_gallon / mpg
dollars_500_miles = 500 * dollars_per_gallon / mpg

print(f'{dollars_20_miles:.2f} {dollars_75_miles:.2f} {dollars_500_miles:.2f}')