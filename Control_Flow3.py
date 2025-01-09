#FizzBuzz Program
'''
Write a Python program that iterates through the numbers 1 to 100 and 
applies specific rules to determine what to print for each number. 
This exercise will help you practice working with loops, conditionals, and basic arithmetic operators.
'''
for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzbuzz)