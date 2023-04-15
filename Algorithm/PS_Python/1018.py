a, b = map(int, input().split())
lis = [list(input()) for _ in range(b)]
fi, se = 'WBWBWBWB', 'BWBWBWBW'
one = [list(fi) if i % 2 == 0 else list(se) for i in range(8)]
two = [list(se) if i % 2 == 0 else list(fi) for i in range(8)]

