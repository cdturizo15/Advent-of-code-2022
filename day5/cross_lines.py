import numpy as np

class Plane:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.plane = np.zeros((self.x, self.y))
        self.line_counter = 0
    
    def count_lines_overlap(self):
        count = 0
        for i in range(self.x):
            for j in range(self.y):
                if self.plane[i,j] > 1:
                    count += 1
        return count
    
    def add_line(self, line):
        point1 = line[0]
        point2 = line[1]
        if point1[0] == point2[0]:
            self.line_counter += 1
            limit = max(point1[1], point2[1])
            begin = min(point1[1], point2[1])
            for i in range(begin, limit+1):
                self.plane[i,point1[0]] += 1
        elif point1[1] == point2[1]:
            self.line_counter += 1
            limit = max(point1[0], point2[0])
            begin = min(point1[0], point2[0])
            for i in range(begin, limit+1):
                self.plane[point1[1],i] += 1
        else: #with diagonals lines
            begin_y = min(point1[0], point2[0])
            end_y = max(point1[0], point2[0])
            begin_x = min(point1[1], point2[1])
            end_x = max(point1[1], point2[1])
            if point1[0] < point2[0]:
                if point1[1] < point2[1]:
                    j = begin_y
                    for i in range(begin_x, end_x+1):
                        self.plane[i, j] += 1
                        j += 1
                else:
                    j = end_y
                    for i in range(begin_x, end_x+1):
                        self.plane[i, j] += 1
                        j -= 1
            else:
                if point1[1] < point2[1]:
                    j = end_y
                    for i in range(begin_x, end_x+1):
                        self.plane[i,j] += 1
                        j -= 1
                else:
                    j = begin_y 
                    for i in range(begin_x, end_x+1):
                        self.plane[i, j] += 1
                        j += 1
    def print_plane(self):
        print(self.plane)

def get_max_y(data):
    max_x = 0
    for coords in data:
        point1 = coords[0]
        point2 = coords[1]
        if point1[0] > max_x:
            max_x = point1[0]
        if point2[0] > max_x:
            max_x = point2[0]
    return max_x
def get_max_x(data):
    max_y = 0
    for coords in data:
        point1 = coords[0]
        point2 = coords[1]
        if point1[1] > max_y:
            max_y = point1[1]
        if point2[1] > max_y:
            max_y = point2[1]
    return max_y
data = []
with open('data.txt') as f:
    for line in f:
        line = line. rstrip('\n')
        line = line.split('->')
        line[0] = line[0].split(',')
        line[0] = [int(x) for x in line[0]]
        line[1] = line[1].split(',')
        line[1] = [int(x) for x in line[1]]
        data.append(line)


max_x = get_max_x(data)
max_y = get_max_y(data)
print(max_x, max_y)
#print(data)
board = Plane(max_x+1, max_y+1)
for coords in data:
    board.add_line(coords)  
number_of_dots = board.count_lines_overlap()
print(number_of_dots)
board.print_plane()

