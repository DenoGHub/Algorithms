# Converts a decimal number to binary
def decimal_to_binary(n):
    binary_from_integer = ""
    while n != 0:
        if n % 2 == 0:
            n = n / 2
            binary_from_integer += "0"
        else:
            binary_from_integer += "1"
            n -= 1
            n = n / 2
    return binary_from_integer[::-1]


print(decimal_to_binary(236))

