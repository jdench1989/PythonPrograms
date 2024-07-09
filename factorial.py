def factorial(num):
    result = 1
    for number in range(num, 0, -1):
        result = result * number
    return "Factorial of {0} is {1}".format(num, result)


print(factorial(int(input("Enter a number: "))))
