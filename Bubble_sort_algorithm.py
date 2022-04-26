def bubble_sort(lst):
    swaps = 0
    iter_ = 0
    for i in range(len(lst)-1):
        swaps_pass = 0
        for j in range(len(lst)-i-1):
            iter_ += 1
            if lst[j] > lst[j+1]:
                swaps += 1
                swaps_pass += 1
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if swaps_pass == 0:
            break
    return lst



