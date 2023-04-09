inp = int(input())
count = 1
b = 1
while inp > b:
    b += count * 6
    count += 1
print(count)

inp = int(input())
count = 0
su1, su2 = 0, 1
while True:
    if inp in range(su1, su2+1):
        break
    count += 1
    su1 = su2
    su2 = su1 + count * 6
print(count+1)