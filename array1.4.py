arr = [3, 0, -6, 4, 9, 6, 1]

def smaller_elements(arr):
    result = []
    for i in range(len(arr)):
        count = 0
        right = arr[i+1:]
        for num in right:
            if num < arr[i]:
                count += 1
        result.append(count)
    return result

print(smaller_elements(arr))
