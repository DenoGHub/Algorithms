import Fibonacci


def test_fib_with_steps():
    tests = [
        [[1, 2], 5, [1, 2, 3, 5, 8]],
        [[0, 1], 5, [0, 1, 1, 2, 3]],
        [[0, 0], 5, [0]],
        [[-1, -1], 5, [0]]
    ]
    for signature, n, expected_result in tests:
        actual_result = Fibonacci.fib_with_steps(signature, n)
        assert actual_result == expected_result


def test_tribonacci():
    tests = [
        [[1, 1, 1], 1, None],
        [[1, 1, 1], 2, None],
        [[1, 1, 1], 3, [1, 1, 1]],
        [[-1, -2, -1], 5, None],
        [[1, 2, 3], 4, [1, 2, 3, 6]]
    ]
    for signature, n, expected_result in tests:
        actual_result = Fibonacci.tribonacci(signature, n)
        assert actual_result == expected_result
