#Day 2 - Dive
def part1():
    horz = 0
    depth = 0

    f = open("input.txt")

    for line in f:
        command, num = line.split(" ")
        num = int(num)
        if command == "forward":
            horz+=num
        elif command == "down":
            depth+=num
        else:
            depth-=num
    
    print(horz*depth)

def part2():
    horz = 0
    depth = 0
    aim = 0

    f = open("input.txt")

    for line in f:
        command, num = line.split(" ")
        num = int(num)
        if command == "forward":
            horz+=num
            depth += aim*num
        elif command == "down":
            aim+=num
        else:
            aim-=num
    
    print(horz*depth)

part1()
part2()