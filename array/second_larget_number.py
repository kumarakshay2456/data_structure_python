"""
Find the second-Largest number in array
"""


def second_largest(array: []):
    first_number, second_number = -1, - 1
    for num in array:
        if num > first_number:
            second_number = first_number
            first_number = num
        else:
            if num >= second_number and num != first_number:
                second_number = num

    return second_number


if __name__ == "__main__":
    print("Hello")
    print(second_largest([23, 45, 21, 90, 89, 95, 96]))
