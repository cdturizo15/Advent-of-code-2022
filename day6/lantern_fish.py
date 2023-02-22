
def pass_days_slow(fish, no_days):
    for day in range(no_days):
        for i in range(len(fish)):
            if fish[i] != 0:
                fish[i] -= 1
            else:
                fish.append(8)
                fish[i] = 6
    return fish

def pass_days_fast(fish, no_days):
    fish_dict = {}
    for state in fish:
        if state in fish_dict:
            fish_dict[state] += 1
        else:
            fish_dict[state] = 1
    print(fish_dict)
    for day in range(no_days):
        update_fish_dict = {}
        for state, count in fish_dict.items():
            if state == 0:
                if 6 in update_fish_dict:
                    update_fish_dict[6] += count
                else:
                    update_fish_dict[6] = count
                if 8 in update_fish_dict:
                    update_fish_dict[8] += count
                else:
                    update_fish_dict[8] = count
            else:
                if state-1 in update_fish_dict:
                    update_fish_dict[state-1] += count           
                else:
                    update_fish_dict[state-1] = count

        fish_dict = update_fish_dict
        #print(fish_dict.values())

    return (sum(fish_dict.values()))

    


fish = []
with open('data.txt') as f:
    for line in f:
        for char in line:
            if char != ",":
                fish.append(int(char))
new_fish = pass_days_fast(fish, 256)
print(new_fish)
