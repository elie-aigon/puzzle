# import random

# buff = 1
# board = []
# game_size = 3
# for x in range(game_size):
#     col = []
#     for y in range(game_size):
#         col.append(buff)
#         buff += game_size
#     board.append(col)
#     buff = buff - (game_size * game_size - 1)
# liste = []
# for x in range(game_size):
#     for element in board[x]:
#         liste.append(element)

# print(liste)
# random.shuffle(liste)
# print(liste)
# new_board = []
# sub = []
# count = 0
# for element in liste:
#     sub.append(element)
#     count += 1
#     if count % 3 == 0:
#         new_board.append(sub)
#         sub = []
# print(new_board)

import random

def is_solvable(puzzle, size):
    inversions = 0
    for i in range(size**2 - 1):
        for j in range(i+1, size**2):
            if puzzle[j] and puzzle[i] and puzzle[i] > puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

def generate_solvable_puzzle(size):
    puzzle = [i for i in range(1, size**2)] + [0]
    while True:
        random.shuffle(puzzle)
        if is_solvable(puzzle, size):
            return puzzle

size = 2
puzzle = generate_solvable_puzzle(size)
puzzle_grid = [[puzzle[i + j * size] for i in range(size)] for j in range(size)]
print(puzzle_grid)


self.board = [[board[x +  y* game_size] for x in range(game_size)] for y in range(game_size)]