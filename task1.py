n = int(input())
    while n < 1:
        n = int(input())
a = [1]
for i in range(n-1//2):
    a.append(a[i]+2)
print(a)
