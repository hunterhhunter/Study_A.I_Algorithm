n, a, b = map(int, input().split())
s = []
soli = []
def find_gcd(a, b):
    while (b!=0):
        a, b = b, a%b
    return a

for i in range((2*n)):
    s.append(a+(b*i))
s.sort()
front = len(s)//2-1
back = len(s)//2
while True:
    if len(s) == 0 or front == 0:
        break
    if back == len(s)-1:
        front -= 1
        if front <= -1:
            front = 0
        back = front + 1
    if find_gcd(s[front], s[back]) == 1:
        soli.append((s[front], s[back]))
        s.pop(front)
        s.pop(back-1)
        front = len(s) // 2 - 1
        back = len(s) // 2
    else:
        back += 1


if len(soli) >= n:
    print('Yes')
    for x, y in soli:
        print(x, y)
else:
    print('No')