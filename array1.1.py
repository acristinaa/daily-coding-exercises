n = [1,2,3,4,5]

def product(n):
    x = []
    for i in range(len(n)):
        x.append(1)
        for j in range(len(n)):
            if i != j:
                x[i] = n[j] * x[i]
    return x            


print(product(n))