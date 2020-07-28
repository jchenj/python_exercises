grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# List -> String
# Given a list, produce an image made of the list elements. By first printing
# first element of all lists, then the second element, through all the internal
# lists

def pic_grid(grid):
 for j in range(len(grid[0])):
     for i in range(len(grid)):
         print(grid[i][j], end="")
     print('')


pic_grid(grid)
