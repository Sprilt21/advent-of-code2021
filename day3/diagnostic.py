def part1():
    f = open("input.txt")

    lines = list(f.readlines())

    gammaFinal = ""
    epsilonFinal = ""

    for i in range(0, len(lines[0])-1):
        numOnes = 0
        numZeros = 0

        for line in lines:
            if line[i] == "1":
                numOnes+=1
            else:
                numZeros+=1
        if numOnes > numZeros:
            gammaFinal += "1"
            epsilonFinal += "0"
        else:
            gammaFinal += "0"
            epsilonFinal += "1"

    print(int(gammaFinal, 2) * int(epsilonFinal, 2))

def part2():
    f = open("input.txt")

    oxyRating = ""
    

    oxyList = list(f.readlines())
    i = 0

    while len(oxyList) != 1:

        temp = []
        moreCommon = "0"
        numOnes = 0
        numZeros = 0
        
        for item in oxyList:
            
            if item[i] == "1":
                numOnes+=1
            else:
                numZeros+=1
        if numOnes >= numZeros:
            moreCommon = "1"

        for item in oxyList:
            if item[i] == moreCommon:
                temp.append(item)

        oxyList = temp
        i+=1
    
    oxyRating = oxyList[0]
    
    scrubRating = ""
    f = open("input.txt")
    scrubList = list(f.readlines())

    j = 0

    while len(scrubList) != 1:
        temp = []
        lessCommon = "1"
        numOnes = 0
        numZeros = 0

        for item in scrubList:
            if item[j] == "1":
                numOnes+=1
            else:
                numZeros+=1
        
        if numOnes >= numZeros:
            lessCommon = "0"

        for item in scrubList:
            if item[j] == lessCommon:
                temp.append(item)
        scrubList = temp;
        j+=1
    
    scrubRating = scrubList[0]

    print(int(oxyRating, 2) * int(scrubRating, 2))

part1()
part2()