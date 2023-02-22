bingo_cards = []
bingo_card = []
numbers = []
def verify_win(bingo_card,numbers):
    marked_numbers = []
    result_row = verify_win_row(bingo_card,numbers)
    result_column = verify_win_column(bingo_card,numbers)
    if result_row[0] < result_column[0]:
        result = result_row
        numbers_index = numbers.index(str(result[2]))
        bingo_numbers = []
        for row in result[3]:
            row = row[0].split(" ")
            for number in row:
                if number != "":
                    bingo_numbers.append(int(number))
        for i in range(numbers_index+1):
            if int(numbers[i]) in bingo_numbers:
                marked_numbers.append(int(numbers[i]))
        result[1] = sum(bingo_numbers)-sum(marked_numbers)
        return result
    else:
        result = result_column
        bingo_numbers = []
        numbers_index = numbers.index(str(result[2]))
        for row in result[3]:
            row = row[0].split(" ")
            for number in row:
                if number != "":
                    bingo_numbers.append(int(number))
        for i in range(numbers_index+1):
            if int(numbers[i]) in bingo_numbers:
                marked_numbers.append(int(numbers[i]))
        result[1] = sum(bingo_numbers)-sum(marked_numbers)
        return result

def verify_win_row(bingo_card,numbers):
    best_index = 10000
    for row in bingo_card:
        winning_numbers = []
        winning_numbers_index = []
        line = row[0].split(" ")
        for number in line:
            if number in numbers:
                winning_numbers.append(int(number))  
                winning_numbers_index.append(numbers.index(number))  
        if len(winning_numbers) == 5:
            last_number = max(winning_numbers_index)
            if int(last_number)<best_index:
                best_row = winning_numbers_index.copy()
                best_index = int(last_number)      
    result = [max(best_row),0,int(numbers[max(best_row)]),bingo_card]
    return result
def verify_win_column(bingo_card,numbers):
    best_index = 1000000
    for column in range(len(bingo_card)):
        winning_numbers = []
        winning_numbers_index = []
        for row in bingo_card:
            row = row[0].split(" ")
            while("" in row):
                row.remove("")
            if row[column] in numbers:
                winning_numbers.append(int(row[column]))
                number_index = numbers.index(row[column])
                winning_numbers_index.append(number_index)
            if len(winning_numbers) == 5:
                last_number = max(winning_numbers_index)
                if(int(last_number)<best_index):
                    best_column = winning_numbers_index.copy()
                    best_index = int(last_number)
    result = [max(best_column),0,int(numbers[max(best_column)]),bingo_card]
    return result

with open('numbers.txt') as f:
    for line in f:
        line = line. rstrip(',')
        numbers.append(line)
with open('data.txt') as f:
    for line in f:
        line = line. lstrip(' ')
        line = line.split('\n')
        if "" in line:
            line.remove("")
        if line[0] != '':
            bingo_card.append(line)
        if len(bingo_card) == 5:
            bingo_cards.append(bingo_card)
            bingo_card = []

numbers = numbers[0].split(",")
best = [0]
worst = [0,0]
for bingo_card in bingo_cards:
    first_win = verify_win(bingo_card,numbers)
    if best[0]<first_win[0]: #change for best or worst win
        best = first_win 

print(best)
print(best[1]*best[2])





