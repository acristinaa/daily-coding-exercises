def reverse(items):
    reversed_list = []
    for i in range(len(items)-1, -1, -1): #Going backwards
        reversed_list.append(items[i])
    return reversed_list


items = [1, 2, 5, 2, 3, 8, 1]
print(reverse(items))