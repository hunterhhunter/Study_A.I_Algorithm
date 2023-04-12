lis = [list(map(int, input().split())) for _ in range(3)]
x = [r[0] for r in lis]
y = [r[1] for r in lis]
for a in x:
    if x.count(a) == 1:
        x_x = a
for a in y:
    if y.count(a) == 1:
        y_y = a
print(x_x, y_y)