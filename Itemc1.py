# Inputs of variables
import string


name = input("Please, enter your name: ")
age = int(input("Enter your age: "))

# calculate of age
next_year_age = age + 1
next_year_age_str = str(next_year_age)

# displaying the greetings
print(f"Hello, {name}! Next year, you will be {next_year_age_str} years old.")  
