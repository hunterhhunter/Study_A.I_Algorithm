import sys

inp = int(input())
lis = set(sys.stdin.readline().rstrip() for _ in range(inp))
lis = sorted(lis)
lis = sorted(lis, key=lambda x: len(x))
for i in lis:
    print(i)
# import sys
# word=set()
# for i in range(int(input())) :
#   word.add(sys.stdin.readline().rstrip())
# word=list(word)
# word.sort()
# word.sort(key=lambda x:len(x))
# print("\n".join(word))