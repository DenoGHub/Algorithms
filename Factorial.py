# Factorial with recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        res = n * factorial(n - 1)
        return res


print(f"Result: 6! = {factorial(6)}")
