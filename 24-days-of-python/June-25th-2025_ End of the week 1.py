# 1. What are the four main data types in Python: Floats, Integers, Boolean, Strings.
# 2. What does range(5) return?:
for i in range(5):
    print(i)
    # output:
    # 0
    # 1
    # 2
    # 3
    # 4

# 3. Write a function that calculates the square of any number:
number = int(input("Enter the the number needed to be square: "))

def square(number):
    return number*number
print(square(number))

# 4. What is the output of:
x = 5

if x == 5:
    print("True")
else:
    print("False") 

# Write a loop that counts from 1 to 10 and prints only even numbers:    

for i in range(1, 11): # 1 to 10
    if i % 2 == 0:     # % means "modulus" = remainder
        print(i)
