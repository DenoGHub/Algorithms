# Generates fibonacci sequence
def fibonacci(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case


arr = []
for i in range(15):
    arr.append(fibonacci(i))
# print(arr)


# ----------------------------------------------------------------------------------------------------------------------
# Generates fibonacci sequence
# From which two numbers to begin the sequence - signature, The length of the sequence - n
def fib_with_steps(signature: list, n: int):
    for index, value in enumerate(signature):
        index += 1
        next_sequence = value + signature[index]
        if next_sequence <= 0:
            return [0]
        signature.append(next_sequence)
        if len(signature) >= n:
            break
    return signature


# ----------------------------------------------------------------------------------------------------------------------
# Generates tribonacci sequence
# From which two numbers to begin the sequence - signature, The length of the sequence - n
def tribonacci(signature, n):
    if n <= 2:
        return None
    elif n == 3:
        return signature
    elif isinstance(n, list):
        return n
    if n > 3:
        for index, value in enumerate(signature):
            if value < 0:
                return None
            index += 1
            index2 = index + 1
            next_sequence = value + signature[index] + signature[index2]
            signature.append(next_sequence)
            if len(signature) >= n:
                break
        return signature





