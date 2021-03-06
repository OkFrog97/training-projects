def checker():
    import math
    
    n = 10000000
    
    solution = {
    'math.log(math.log(n, 2))':math.log(math.log(n, 2)),
    'math.sqrt(math.log(n, 4))':math.sqrt(math.log(n, 4)),
    'math.log(n, 3)':math.log(n, 3),
    'math.log(n, 2) ** 2':math.log(n, 2) ** 2,
    'math.sqrt(n)':math.sqrt(n),
    'n / math.log(n, 5)':n / math.log(n, 5),
    'math.log(math.factorial(n),2)':math.log(math.factorial(n),2),
    '3 ** math.log(n, 2)':3 ** math.log(n, 2),
    'n ** 2':n ** 2,
    '7 ** (math.log(n, 2))':7 ** (math.log(n, 2)),
    'math.log(n, 2) ** (math.log(n, 2))':math.log(n, 2) ** (math.log(n, 2))
    }
    '''
    'n ** (math.log(n, 2))':n ** (math.log(n, 2)),
    'n ** (math.sqrt(n))':n ** (math.sqrt(n)),
    '2 ** n':2 ** n,
    '4 ** n':4 ** n,
    '2 ** (3 * n)':2 ** (3 * n),
    'math.factorial(n)':math.factorial(n),
    '''
    
    
    for i in sorted(solution.items(), key= lambda x : x[1]):
        print (i)

if __name__ == '__main__':
    checker()
