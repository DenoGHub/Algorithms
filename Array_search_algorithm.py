# Function searches for the smallest value in the given array using recursion
def array_search(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        first = arr[0]
        new_arr = arr[1::]
        recursion = array_search(new_arr)
        if first < recursion:
            return first
        else:
            return recursion


array = [0, 1, 2, 3, -80, 5]
function_call = array_search(array)
print(f"Array: {array} min value: {function_call}")

