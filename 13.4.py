n = int(input())
a = []
for i in range(n):
    a.append(input())
k = 1
for i in range(n):
    print(a[int((i/2)+0.5)*k])
    k *= -1
