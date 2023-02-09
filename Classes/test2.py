inversions = 0

puzzle = [7, 9, 3, 6, 5, 2, 8, 4, 1]

inversions = 0
for i in range(len(puzzle)):
    for j in range(i + 1, len(puzzle)):
        if puzzle[i] > puzzle[j]:
            inversions += 1
print(inversions)
