n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in range(n//2):
    print(a[2*i+1])
for i in range(n//2+n%2):
    print(a[-2*i-n%2])
