from gettext import find


data = []
inputs = []
outputs = []

with open('data.txt', 'r') as f:
    for line in f:
        line = line.split(' ')
        inputs.append(line[0:10])
        outputs.append(line[11:])

def find_unique_digits(digit):
    if len(digit) == 2:
        return 1
    elif len(digit) == 3:
        return 7
    elif len(digit) == 4:
        return 4
    elif len(digit) == 7:
        return 8
    else:
        return 0


    
    