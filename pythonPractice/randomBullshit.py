import math
import random
def celsiusToFarenheit():
    celsius = float(input("Please put in a temperature in celsius "))
    farenehit = (celsius * 9/5) +32
    print(farenehit)

# Ask the user for two numbers, and print the sum of those numbers squared.
def squareNumbers():
    x = int(input("First number please "))
    y = int(input("Second number please "))
    z = x+y
    print(z * z)

def accessList():
    strings = ["Colder","Warmer", "Hello, world!", "Too far!"]
    print(strings[2])
# Given the following code, add the first and fifth elements together. Do not hard code, it should work for any two numbers.
def addWithin():
    nums = [5, 6, -10, 9, -11, 7]
    z= nums[0] + nums[4]
    # Lists are indexed at zero. The "first" element is at index 0.
    print(z) # Technically, it didn't ask us to do anything besides adding -  the assigning and printing is just to test it


n = ["word", "phrase", 8, ("beam")]
for item in n:
    print(type(item))
    print(item)