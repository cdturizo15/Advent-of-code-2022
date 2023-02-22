data = []
info = []
prev = [0,0,0]
with open('measurements.txt') as f:
    for line in f:
        line = line. rstrip('\n')
        data.append(line)

for index in range(len(data)-2):
    new = [int(data[index]),int(data[index+1]),int(data[index+2])]
    sum_new = sum(new)
    if(sum_new>sum(prev)):
        if(sum(prev)==0):
            info.append("nan")
            prev = new
        else:
            info.append("increased")
            prev = new
    elif(sum_new==sum(prev)):
        info.append("no change")
        prev = new
    else:
        info.append("decreased")
        prev = new

print(info)
print(info.count("increased"))