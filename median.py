"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(list):
    list.sort()
    if (len(list)%2 == 1):
        print(list[int((len(list)-1)/2)])
    else:
        num1 = list[int(len(list)/2)]
        num2 = list[int(len(list)/2 - 1)]
        print((num1+num2)/2)
while True:
    try:
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

median(numbers)


