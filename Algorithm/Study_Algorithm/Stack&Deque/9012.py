def is_gwal(paren):
    lis = []
    for i in paren:
        if i == "(":
            lis.append(i)
        else:
            if len(lis) > 0:
                lis.pop(-1)
            else:
                return "NO"
    if len(lis) == 0:
        return "YES"
    else:
        return "NO"

inp = int(input())

for _ in range(inp):
    moon = input()
    print(is_gwal(moon))