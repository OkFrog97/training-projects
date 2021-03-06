'''
Task from hakkerrank.com
'''

def countingValleys(s):
    way = []
    seaLevel = 0
    valleys = 0
    for i in s:
        if i == "U":
            seaLevel+=1
            way.append(seaLevel)
        elif i == "D":
            seaLevel-=1
            way.append(seaLevel)
    
    for i in range(len(way)):
        if way[i] == 0 and way[i-1] == -1:
            valleys +=1    
    return valleys

def tests():
    s1 = ["D","D","U","U","U","U","D","D"]
    s2 = ["U","D","D","D","U","D","U","U"]    
    print ('{} should be 1.'.format(countingValleys(s1)))
    print ('{} should be 1.'.format(countingValleys(s2)))

def main ():
    tests ()


if __name__ == "__main__":
    main()