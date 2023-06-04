n, r, c = map(int, input().split())
lis = [[0]*(2**n) for _ in range(2**n)]
#2*2 좌표찍기
i = 0
z = i+4
f = 1
def recul2_2(x, y):
    global i
    global z
    if i == z:
        return
    lis[x][y] = i
    if x == r and y == c:
        return
    i += 1
    if i % 4 == 1:
        y += 1
    if i % 4 == 2:
        x, y = x+1, y-1
    if i % 4 == 3:
        y += 1
    recul2_2(x, y)

def go_to_side(x, y):
    global f
    return x, y+2*f
def go_down(x, y):
    global f
    return x+2*f, y-2*f

def recul4_4(x, y):
    global z
    x_s, y_s = x, y
    recul2_2(x, y)
    for g in range(3):
        if g % 2 == 1:
            x, y = go_down(x, y)
        else:
            x, y = go_to_side(x, y)
        z = i+4
        recul2_2(x, y)
    else:
        return x_s, y_s

def recul8_8(x, y):
    global f
    global z
    x, y = recul4_4(x, y)
    for g in range(3):
        if g % 2 == 1:
            x, y = go_down(x, y)
        else:
            x, y = go_to_side(x, y)
        z = i + 4
        f += 1
        recul4_4(x, y)


recul8_8(0, 0)
for i in lis:
    print(i)
print(lis[r][c])
