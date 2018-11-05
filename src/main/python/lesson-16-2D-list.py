grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(grid)

def print_array(number_grid):
    for i in range(len(number_grid)):
        for j in range(len(number_grid[i])):
            print(number_grid[i][j])

print(print_array(grid))