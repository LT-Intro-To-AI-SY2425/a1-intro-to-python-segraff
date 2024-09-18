
def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(is_even_or_odd(4))
print(is_even_or_odd(9))

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

print(calculate_average([10,20,30,40]))

user_input = input("Enter a word or phrase: ")
normalized_input = ''.join(char.lower() for char in user_input if char.isalnum())
is_palindrome = normalized_input == normalized_input[::-1]
if is_palindrome:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')

user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in user_input:
    if char in vowels:
        count += 1
print(f'The number of vowels in the string is: {count}')

user_input = input()
