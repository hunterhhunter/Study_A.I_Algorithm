sik = input().split('-')
lis = []
su = 0
for i in sik:
    tmp = 0
    s = i.split('+')
    for x in s:
        tmp += int(x)
    lis.append(tmp)
su = lis[0]
for i in range(1, len(lis)):
    su -= lis[i]
print(su)



# for i in range(len(sik)):
#     lis.append(list(sik[i].split(sep='+')))
# mi = int(lis[0][0])
# if len(lis) == 1:
#     for i in lis[0][1:]:
#         mi += int(i)
# else:
#     for i in lis[1:]:
#         su = 0
#         for x in i:
#             su += int(x)
#         lis2.append(su)
#     for i in lis2:
#         mi -= i
# print(mi)
# if len(lis) == 1:
#     for x in lis[0][1:]:
#         mi += int(x)
# else:
#     for x in lis[1:]:
#         tmp = 0
#         for i in x:
#             tmp += int(i)
#         mi -= tmp
# print(mi)