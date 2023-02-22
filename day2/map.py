data = []
coords = [0,0,0]
with open('map.txt') as f:
    for line in f:
        line = line. rstrip('\n')
        data.append(line)

for move in data:
    nextMove = move.split(' ')
    if nextMove[0] == 'up':
        coords[2] -= int(nextMove[1])

    if nextMove[0] == 'down':
        coords[2] += int(nextMove[1])

    if nextMove[0] == 'forward':
        coords[0] += int(nextMove[1])
        coords[1] += (int(nextMove[1])*coords[2])

print(coords)
print(coords[0]*coords[1])
    