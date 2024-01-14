import pytest


# def triangle(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print("*", end=" ")
#         print()
#
#
# triangle(5)


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
    print(n)


print(factorial(1))
