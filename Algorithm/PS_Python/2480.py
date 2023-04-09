in1, in2, in3 = map(int, input().split())

if in1 == in2 == in3:
    print(10000+in1*1000)
elif in1 == in2 or in1 == in3:
    print(1000 + in1 * 100)
elif in2 == in3:
    print(1000 + in2 * 100)
else:
    print(max(in1, in2, in3)*100)
