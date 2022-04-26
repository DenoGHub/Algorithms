import Bubble_sort_algorithm
import Binary_search_algorithm
import Binary_conversion
import Array_search_algorithm
import Merge_sort_algorithm
import Stack


def test_bubble_sort():
    tests = [
        [[-5, 4, 3, -2, 1], [-5, -2, 1, 3, 4]],
        [[0, 4.3, 3, -2, 1], [-2, 0, 1, 3, 4.3]],
        [[6.3, 6.2, 6.1, -6.5, 0], [-6.5, 0, 6.1, 6.2, 6.3]]
    ]
    for lst, expected_result in tests:
        actual_result = Bubble_sort_algorithm.bubble_sort(lst)
        assert actual_result == expected_result

# Feilina bet kokiu atveju, blogai uzrasyta gal sitie testai
def test_binary_search():
    tests = [
        [[2, 3, 5, 8, 10, 12], 12, 12],
        [[2, 3, 100, 8, 10, 12], 100, 100],
        [[-5, 1.1, 101.18, -58, 10], 1.1, 1.1]
    ]

    for arr, key, expected_result in tests:
        actual_result = Binary_search_algorithm.binary_search(arr, key)
        assert actual_result == expected_result


def test_decimal_to_binary():
    tests = [
        [236, "11101100"],
        [1234, "10011010010"]
    ]
    for n, expected_result in tests:
        actual_result = Binary_conversion.decimal_to_binary(n)
        assert actual_result == expected_result


def test_array_search():
    tests = [
        [[0, 1, 2, 3, -80, 5], -80],
        [[-1, 0], -1],
        [[1.1, 1.2, -1.5, 5.8], -1.5]
    ]
    for arr, expected_result in tests:
        actual_result = Array_search_algorithm.array_search(arr)
        assert actual_result == expected_result


def test_merge_sort():
    tests = [
        [[5, 56, 89, 10, 25, 38, -5], [-5, 5, 10, 25, 38, 56, 89]],
        [[-8, 50, 5], [-8, 5, 50]],
        [[-1.5, 1.1, 1, 0.9], [-1.5, 0.9, 1, 1.1]]
    ]
    for arr, expected_result in tests:
        actual_result = Merge_sort_algorithm.merge_sort(arr)
        assert actual_result == expected_result

def test_inspect_syntax():
    tests = [
        ['(())', True],
        ['((())', False],
        ['(()))', False],  # This test fails
        ['((()))', True]
    ]
    for to_check, expected_result in tests:
        actual_result = Stack.inspect_syntax(to_check)
        assert actual_result == expected_result

