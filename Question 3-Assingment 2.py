#3. List comprehensions
#A list comprehension is a short way to create a list in Python. It combines a loop and, optionally, a condition into one line.

#general syntax

#new_list = [expression for item in iterable if condition]

#Generate odd numbers from 1 to 50 that are divisible by 3.

odd_multiples_of_three = [number for number in range(1, 51)
                          if number % 2 != 0 and number % 3 == 0]

print(odd_multiples_of_three)

#Output

output_list = [number for number in range(1, 51)]

#Explanation:
#- range(1, 51) produces numbers from 1 to 50.
#- number % 2 != 0 checks whether a number is odd.
#- number % 3 == 0 checks whether it is divisible by 3.