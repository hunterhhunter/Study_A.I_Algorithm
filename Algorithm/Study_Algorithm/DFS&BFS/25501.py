cnt = 0
# def palindrome(word):
#     return reculsive(word, 0, len(word)-1)
#
# def reculsive(word, a, b):
#     global cnt
#     cnt += 1
#     if a >= b:
#         return 1
#     elif word[a] != word[b]:
#         return 0
#     else:
#         reculsive(word, a+1, b-1)
def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

inp = int(input())

for _ in range(inp):
    cnt = 0
    wor = input()
    result = isPalindrome(wor)
    print(result, cnt)