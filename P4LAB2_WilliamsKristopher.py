x = int(input())
y = int(input())
if y >= x:
    for t in range(x, y+1, 5):
        print(t, end = ' ')
    print()
else:
    print("Second integer can\'t be less than the first.")