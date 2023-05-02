def is_gwal(moon):
    lis = []
    for x in moon:
        if x in "([":
            lis.append(x)
        else:
            if x == ")":
                if len(lis) > 0 and lis[-1] == '(':
                    lis.pop(-1)
                else:
                    lis.append(x)
                    break
            else:
                if len(lis) > 0 and lis[-1] == '[':
                    lis.pop(-1)
                else:
                    lis.append(x)
                    break
    if len(lis) == 0:
        return "yes"
    else:
        return "no"
while True:
    inp = input()
    if inp == '.':
        break
    moo = ''
    for i in inp:
        if i in '()[]':
            moo += i
    print(is_gwal(moo))