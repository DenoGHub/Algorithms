# Binary search by diagram in /img/Binary_search.png

# Find the value - key in a given array
def binary_search(arr, key):
    store_middle = 0
    length = len(arr)
    while store_middle < length:
        middle = (store_middle + length) // 2
        if arr[middle] == key:
            print(f"Key: {key} is in the {middle} list index")
            break
        else:
            if arr[middle] < key:
                store_middle = middle + 1
            else:
                length = middle - 1
    return key




