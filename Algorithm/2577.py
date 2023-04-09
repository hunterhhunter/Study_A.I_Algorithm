sim = 1
for _ in range(3):
    sim *= int(input())
su = str(sim)
for x in range(10):
    print(su.count(str(x)))