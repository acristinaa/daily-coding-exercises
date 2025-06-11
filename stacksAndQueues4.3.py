from collections import deque

arr = [10, 5, 2, 7, 8, 7]
k = 3

q = deque() #stores indices of useful elements

for i in range(len(arr)):
    q.append(i)