# table of

# base = int(input("enter any number: ")) 

# for i in range(1, 11):
#     result = base * i
#     print(f"{base} x {i} = {result}")


  
#   WAP to print the sum of the 2 numbers entered by the user

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"The sum of two nnumber is : {sum}")


# WAP  to find remainder when a number is divided by z
number = int(input("Enter the number: "))
z = int(input("Enter the value of z (divisor): "))
remainder = number % z
print("The remainder when", number, "is divided by", z, "is:", remainder)

# check the type of the variable assigned using input() function
var = input("Enter a value: ")
print("The type of the variable is:", type(var))

# use comparision operators to find out whether a given variable A is greater than 'b' or not take a =34 and b=80
a=34
b=80
if(a>b):
  print("a is greater b")

else:
  print("b is greater than a ")
# write a python program to find the avg of the two number input by the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
average = (num1 + num2) / 2
print(f"The average of {num1} and {num2} is: {average}")

# sq of the number entered by the user
num = int(input("Enter a number to find its square: "))
square = num ** 2
print(f"The square of {num} is: {square}")

# WAP  to display a user entered name followed by good afternoon using input() function
name = input("Enter your name: ")
print(f"Good Afternoon {name}!")

# write a program to fill in a letter templete given below with name and date       
name = input("Enter your name: ")
date = input("Enter the date (DD/MM/YYYY): ")   
