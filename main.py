import Bubble_sort_algorithm
import Binary_search_algorithm
import Search_most_repeating_element
import Fibonacci

if __name__ == "__main__":
    Bubble_sort_algorithm.bubble_sort([-5, 4, 3, -2, 1])
    Binary_search_algorithm.binary_search([2, 3, 5, 8, 14, 12], 8)
    Search_most_repeating_element.most_visited_user(['car', 'Tim', 'car', 'John', 'pets', 'pets', 'car'])
    Fibonacci.fib_with_steps([5, 6], 10)
    Fibonacci.tribonacci([1, 2, 3], 10)
