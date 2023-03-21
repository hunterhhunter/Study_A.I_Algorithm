def byun(hak):
    if hak == 'A+':
        return 4.5
    elif hak == 'A0':
        return 4.0
    elif hak == 'B+':
        return 3.5
    elif hak == 'B0':
        return 3.0
    elif hak == 'C+':
        return 2.5
    elif hak == 'C0':
        return 2.0
    elif hak == 'D+':
        return 1.5
    elif hak == 'D0':
        return 1.0
    elif hak == 'F':
        return 0.0
    else:
        pass

subject_o = []
biyul_o = []
score_o = []
chong = 0
count = 0

for i in range(20):
    subject, biyul, score = input().split()
    subject_o.append(subject)
    if score == 'P':
        count += 1
    else:
        score_o.append(byun(score))
        biyul_o.append(float(biyul))

for x in range(20-count):
    chong += biyul_o[x] * score_o[x]

print('%.6f' % (chong / sum(biyul_o)))