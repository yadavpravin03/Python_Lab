# 1. Calculate Simple Interest
principal= 20
rate=300
time=12
si = (principal* rate * time) / 100
print("Simple Interest =", si)


# 2. Find maximum of 2 numbers
a =10
b =30
print("Maximum =", max(a, b))


# 3. Print numbers 1 to 5
num=[1,2,3,4,5]
print(num)

# 4. Find length of a string
s =("Enter a string: ")
print("Length of string =", len(s))


# 5. Print a welcome message
print("Welcome")


# 6. Print first character of a string
print("First character =", s[0])


# 7. Print last character of a string
print("Last character =", s[-1])


# 8. Check positive or negative number
numbers = [10, -5.5,-100]

for num in numbers:
    if num > 0:
        print(f"The number {num} is positive.")
    elif num < 0:
        print(f"The number {num} is negative.")
    else:
        print(f"The number {num} is zero.")


# 9. Add three numbers
x = 10
y = 20
z = 30
print("Sum =", x + y + z)


# 10. Take input from user and make a task
task = input("Enter your task: ")
print("Your task is:", task)