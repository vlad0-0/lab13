n = int(input())-1
a = [1]
for i in range(n//2):
    a.append(a[i]+2)
print(a)
