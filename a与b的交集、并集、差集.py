a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a&b)
print(a.intersection(b))

print(b&a)
print(b.intersection(a))

print(a|b)
print(a.union(b))

print(b|a)
print(b.union(a))

print(a-b)
print(a.difference(b))

print(b-a)
print(b.difference(a))
