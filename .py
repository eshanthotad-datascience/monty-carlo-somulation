a = input('enter')
b = 0
c = []

for i in range(len(a) - 1):

    if a[i] not in c:
        c.append(a[i])

    if a[i] == a[i + 1]:
        b += 1

    else:
        c.append(b + 1)
        b = 0

print(b)
print(c)