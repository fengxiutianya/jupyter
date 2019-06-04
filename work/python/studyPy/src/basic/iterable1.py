import collections
t = isinstance([], collections.Iterable)
print(t)
t = isinstance({}, collections.Iterable)
print(t)

t = isinstance('abc', collections.Iterable)
print(t)
