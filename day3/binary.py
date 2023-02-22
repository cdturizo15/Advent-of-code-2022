data = []
oxygen = ""
CO2 = ""
gamma = ""
epsilon = ""
def count_bits(n):
    one = n.count('1')
    zeros = n.count('0')
    if one > zeros:
        return "1"
    else:
        return "0"

def filter_gamma(counter,data,n):
    if len(data)==1:
        return data
    else:
        new_data = []
        one = counter[n].count('1')
        zeros = counter[n].count('0')
        if one >= zeros:
            for bits in data:
                if bits[n] == "1":
                    new_data.append(bits)
            count_bits = count_bits_list(new_data)
            return filter_gamma(count_bits,new_data,n+1)
        else:
            for bits in data:
                if bits[n] == "0":
                    new_data.append(bits)
            count_bits = count_bits_list(new_data)
            return filter_gamma(count_bits,new_data,n+1)

def filter_epsilon(counter,data,n):
    if len(data)==1:
        return data
    else:
        new_data = []
        one = counter[n].count('1')
        zeros = counter[n].count('0')
        if one >= zeros:
            for bits in data:
                if bits[n] == "0":
                    new_data.append(bits)
            count_bits = count_bits_list(new_data)
            return filter_epsilon(count_bits,new_data,n+1)
        else:
            for bits in data:
                if bits[n] == "1":
                    new_data.append(bits)
            count_bits = count_bits_list(new_data)
            return filter_epsilon(count_bits,new_data,n+1)
            
def count_bits_list(data):
    gamma_counts = [(lambda x: "")(x) for x in range(12)]
    for bits in data:
        for bit in range(len(bits)):
            gamma_counts[bit] += bits[bit]
    return gamma_counts

def epsilon_gamma(n):
    if n == "1":
        return "0"
    else:
        return "1"

with open('data.txt') as f:
    for line in f:
        line = line. rstrip('\n')
        data.append(line)

gamma_data = count_bits_list(data)
print(gamma_data)
oxygen = filter_gamma(gamma_data,data,0)
CO2 = filter_epsilon(gamma_data,data,0)
oxygen_generator = int(oxygen[0], 2)* int(CO2[0], 2)
print(oxygen_generator)



""" for position in gamma_counts:
    gamma += count_bits(position)
    epsilon += epsilon_gamma(count_bits(position))
print(gamma)
print(epsilon)
power = int(gamma,2)*int(epsilon,2)
print(power) """

    

