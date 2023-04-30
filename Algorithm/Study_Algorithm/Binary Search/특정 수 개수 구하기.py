n, m = map(int, input().split())
array = list(map(int, input().split()))

def left_binary(target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start
def right_binary(target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start
print(right_binary(m) - left_binary(m))

from bisect import bisect_left, bisect_right

def conun_by_range(array, left_value, right_value): #위의 left_binary + right_binary를 합친 함수
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index