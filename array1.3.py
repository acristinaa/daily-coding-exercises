arr = [-4, -50, 42, 14, -5, 86]

def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0
    for x in arr: 
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def min_subarray_sum(arr):
    min_ending_here = min_so_far = 0

    for x in arr:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far

print("Given array:", arr)
print("Maximum subarray sum:", max_subarray_sum(arr))
