matrix = [
    [2,5,1,0,2],
    [3,4,2,1,0],
    [3,4,5,0,2],
    [2,1,2,1,0],
    [2,0,0,3,4]
]
matrix2 = [
    [3,2,1,4,5],
    [0,0,2,2,3],
    [1,1,3,5,2],
    [0,0,2,0,0],
    [1,1,0,2,0]
]

result = []

for k in range(5):
    baris = []
    for j in range(5):
        total = 0
        for z in range(5):
            total += matrix[k][z] * matrix2[z][j]
        baris.append(total)
    result.append(baris)

for row in result:
    print(row)            