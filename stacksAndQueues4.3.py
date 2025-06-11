from collections import deque

arr = [10, 5, 2, 7, 8, 7]
k = 3

q = deque() #stores indices of useful elements

for i in range(len(arr)):
    if q and q[0] < i - k + 1: #Remove indices from the front if they are outside the current window
        q.popleft()

    while q and arr[i] > arr[q[-1]]: #Remove indices from the back while the current element is greater than the elements they point to, because those elements will never be the max if the current one is larger
        q.pop()


    q.append(i) #Add the current index

    if i >= k - 1: #Once the first full window is formed, print the maximum (at the front of the deque)
        print(arr[q[0]])