#Day 1 - Sonar Sweep

def part1():
    numLarger = 0

    f = open("input.txt")

    oldLine =  next(f);
    for line in f:
        if int(line) > int(oldLine):
            numLarger+=1
        oldLine = int(line)
    print(numLarger)

def part2():
    numLarger = 0

    f = open("input.txt")
    
    lines = list(map(int,f.readlines()))

    for i in range(1, len(lines)-2):
        if sum(lines[i:i+3]) > sum(lines[i-1: i+2]):
            numLarger+=1
    print(numLarger)
        
part1()
part2()   
