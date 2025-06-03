sentence = "thisisazigzag"
k = 4

grid = [[' ' for _ in range(len(sentence))] for _ in range(k)] #Create grid with spaces

current_row = 0
going_down = True

for col, c in enumerate(sentence): #Place each character in the grid
    grid[current_row][col] = c

    if going_down:
        current_row += 1
        if current_row == k:  #hit bottom
            current_row = k - 2
            going_down = False
    else:
        current_row -= 1
        if current_row == -1:  #hit top
            current_row = 1
            going_down = True

for row in grid:
    print(''.join(row))
