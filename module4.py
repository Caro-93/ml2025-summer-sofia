# The program asks the user for input N (positive integer) and reads it

N = int(input("Enter a positive integer number."))

# Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

numbers_list = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers_list.append(num)

# In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.

X = int(input("Enter an integer X: "))
if X in numbers_list:
    print(numbers_list.index(X) + 1)
else:
    print(-1)
