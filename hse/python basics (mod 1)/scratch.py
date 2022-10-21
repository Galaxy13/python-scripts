l1 = input().split(' ')
p1, p2 = 0, 1
new_l = []
while p2 < len(l1):
    if l1[p1] != l1[p2]:
        new_l.append(l1[p1])
        p1 += 1
        p2 += 1
    else:
        p2 += 1
print(*new_l)