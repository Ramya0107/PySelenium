import webbrowser

import pytest


# def triangle(n):
#     for i in range(0, n):
#         for j in range(0, i + 1):
#             print("*", end=" ")
#         print()
#
#
# triangle(5)


# def factorial(n):
#     return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
#     print(n)
#
#
# print(factorial(1))


# import keyword
#
# print(keyword.kwlist)
#
# a = True
# b = True
#
# print(a and b)
# print(a or b)
# print(not a)

# num = input("Enter a number:")
#
# if int(num) % 2 == 0:
#     print("you entered a even number")
# else:
#     print("you entered a odd number")

# print(list(range(10)))
# print(list(range(5,10)))
# print(list(range(1,10,2)))
# print(list(range(0,10,2)))
# print(list(range(10,1,-1)))
# print(list(range(1,10,-1)))

# from selenium.webdriver.chrome.service import Service
#
# browser_path = Service("")
# driver = webbrowser.Chrome(browser_path)

def palindrome():
    actual_text = input("Enter a word: ")
    palindrome_text = actual_text[::-1]
    print(palindrome_text)
    print("This is palindrome" if (actual_text == palindrome_text) else "This is not a palindrome")


palindrome()


def fibo():
    a = 0
    b = 1
    n = 10
    for i in range(n):
        print(a)
        a, b = b, a + b


fibo()

