crabs = []

with open('data.txt') as f:
    for line in f:
        line = line.split(',')
        crabs = list(map(int, line))

def how_much_fuel1(crabs,position):
    fuel = list(map(lambda x: abs(x-position), crabs))
    total_fuel = sum(fuel)
    return total_fuel

def how_much_fuel2(crabs,position):
    fuel = []
    for crab in crabs:
        distance = abs(crab-position)
        fuel_consumed = ((distance+1)*distance)/(2)
        fuel.append(fuel_consumed)
    total_fuel = int(sum(fuel))
    return total_fuel
def best_spot(crabs):
    best_spot = 0
    best_fuel = 1000000000
    for position in range(max(crabs)):
        fuel = how_much_fuel2(crabs, position)
        if fuel < best_fuel:
            best_fuel = fuel
            best_spot = position
    return best_spot, best_fuel

position = best_spot(crabs)
print(position)