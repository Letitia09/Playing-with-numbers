a=int(input())
l=[int(x) for x in input().split()]
d=int(input())
s=l[d:]+l[:d]
print(s)
