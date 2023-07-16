
l = []

out =[]

n = input()

l = list(map(int,n.split(' ')))

l.sort()

for i in range(len(l)):
    if l[i] >= 0:
        out.append(l[i])

for i in out:
    print(i, end=" ")