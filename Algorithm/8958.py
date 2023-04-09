inp = int(input())

for i in range(inp):
    lis = input()
    score = 0
    sumscore = 0
    for a in lis:
        if a == 'O':
            score += 1
        else:
            score = 0
        sumscore += score
    print(sumscore)