n = list(map(int, input().split(", ")))
matrix = []
for _ in range(n[0]):
    matrix.append(list(map(int, (i for i in input()))))
special_index = list(map(int, input().split(", ")))
repeats = special_index.pop()
special_cell_counter = 0
if matrix[special_index[1]][special_index[0]] == 1:
    special_cell_counter = 1


def green_neighbours(grid, index):
    count = 0
    h = index[0]
    w = index[1]
    if h - 1 >= 0:
        if w - 1 >= 0:
            if grid[h-1][w-1] == 1:
                count += 1
        if w + 1 < len(grid):
            if grid[h - 1][w + 1] == 1:
                count += 1
        if grid[h - 1][w] == 1:
            count += 1
    if h + 1 < len(grid):
        if w - 1 >= 0:
            if grid[h + 1][w - 1] == 1:
                count += 1
        if w + 1 < len(grid):
            if grid[h + 1][w + 1] == 1:
                count += 1
        if grid[h + 1][w] == 1:
            count += 1
    if w - 1 >= 0:
        if grid[h][w-1] == 1:
            count += 1
    if w + 1 < len(grid):
        if grid[h][w+1] == 1:
            count += 1
    return count


def condition_01(grid, index):
    count = green_neighbours(grid=grid, index=index)
    needed_neighbours = [3, 6]
    if count in needed_neighbours:
        return "Yes"
    else:
        return "No"


def condition_03(grid, index):
    count = green_neighbours(grid=grid, index=index)
    needed_neighbours = [0, 1, 4, 5, 7, 8]
    if count in needed_neighbours:
        return "Yes"
    else:
        return "No"


for _ in range(repeats):
    new_matrix = [[] for _ in range(n[0])]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                check = condition_01(grid=matrix, index=[i, j])
                if check == "Yes":
                    new_matrix[i].append(1)
                elif check == "No":
                    new_matrix[i].append(0)
            elif matrix[i][j] == 1:
                check = condition_03(grid=matrix, index=[i, j])
                if check == "Yes":
                    new_matrix[i].append(0)
                elif check == "No":
                    new_matrix[i].append(1)
    matrix = new_matrix
    if matrix[special_index[1]][special_index[0]] == 1:
        special_cell_counter += 1
    print(matrix)
print(special_cell_counter)
