x = 0 
y = 0
arr = [3,7,5,6,9]

def sort(arr):
    x = None
    for i in range(len(arr)): 
        for i in range(len(arr) - 1):  
          if arr[i] >= arr[i+1]:
            x = i 
        if x is not None:
            y = i    
    return x,y

print(sort(arr))
