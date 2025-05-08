numbers = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10] 
# Please help me to make program to: 
# a. Calculate the sum of all the numbers from the list "numbers". 
# b. Find the maximum and minimum numbers from the list "numbers". 
# c. Remove duplicates from the list "numbers". 
# d. Find the position a given number in the list "numbers". 
# e. Reverse the order of elements in the list "numbers". 

def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print("Sum of numbers:", sum_of_numbers(numbers))

def max_of_numbers(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number
print("Maximum number:", max_of_numbers(numbers))

def min_of_numbers(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number
print("Minimum number:", min_of_numbers(numbers))

def remove_duplicates(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers
print("List without duplicates:", remove_duplicates(numbers))

def find_position(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1
print("Position of 6:", find_position(numbers, 6))
print("Position of 11:", find_position(numbers, 11))

def reverse_list(numbers):
    reversed_list = []
    for number in numbers:
        reversed_list.insert(0, number)
    return reversed_list
print("Reversed list:", reverse_list(numbers))
# Compare this snippet from Quizz/qs3.py:   
# import random
