# 7.) Understanding Assignments and Comparisons



# Task 1: Value Swapping: Swapped the values of val_1 and val_2


val_1 = 4
val_2 = 8

val_1, val_2 = val_2, val_1

assert val_1 == 8 and val_2 == 4

print("swapped values:")
print("val_1 =", val_1)
print("val_2 =", val_2)



# Task 2: Perfect Square Checker: Determine if given number is a perfect square


import math

def is_perfect_square(num):
    return math.isqrt(num)**2 == num

numbers = (1, 4, 9, 16, 19, 35)

for num in numbers:
    if is_perfect_square(num):
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is not a perfect square")



