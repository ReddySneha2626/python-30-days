name = input("Enter your name: ")
print(f"Hello, {name}!")
age = input("Enter your age: ")
print(type(age))   
# <class 'str'>  even if you typed 25! Input() alwaya gives you a string
#a = input("First number: ")    # user types 5
#b = input("Second number: ")   # user types 3
#print(a + b)                   # prints 53, not 8! 😮
#round() function is used to round a floating-point number to a specified number of decimal places. It takes two arguments: the number to be rounded and the number of decimal places to round to. The result is a new floating-point number that is rounded to the specified precision.
#pass_rate = 87.666666
#print(round(pass_rate, 2))    # 87.67
a=input("enter your name along with city")
print(f"{a} is learning python in banglore")
x= int(input("Enter first number: "))
y= int(input("Enter second number: "))
print(x + y)
print(x-y)
print(x*y)
print(x/y)
print(round(5/3, 2))   # 1.67
total_tests = int(input("Total number of tests: "))
passed_tests = int(input("Number of passed tests: "))
failed_tests = total_tests - passed_tests
print(failed_tests)
pass_percentage = (passed_tests / total_tests) *100
print(round(pass_percentage, 2))
# if pass_percentage >= 90:
#     print(True)
# else:
#     print(False)
is_release_ready = pass_percentage >= 90
print(f"Is release ready : {is_release_ready}")
