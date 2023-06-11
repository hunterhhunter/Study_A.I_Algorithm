def merge_sort(lis):
    if len(lis) < 2:
        return lis

    mid = len(lis)//2
    low_lis = merge_sort(lis[:mid])
    high_lis = merge_sort(lis[mid:])

    merged_lis = []
    l = h = 0

    while l < len(low_lis) and h < len(high_lis):
        if low_lis[l] < high_lis[h]:
            merged_lis.append(low_lis[l])
            l += 1
        else:
            merged_lis.append(high_lis[h])
            h += 1
    merged_lis += low_lis[l:]
    merged_lis += high_lis[h:]
    return merged_lis

lis = list(map(int, input().split()))
print(merge_sort(lis))
