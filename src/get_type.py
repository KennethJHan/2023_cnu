def print_type(obj):
    print(obj, type(obj))

a = "this is a string."
print_type(a) # this is a string. <class 'str'>
b = -2
print_type(b) # -2 <class 'int'>
c = 3.14
print_type(c) # 3.14 <class 'float'>
d = ["abc", 123]
print_type(d) # ['abc', 123] <class 'list'>
e = (1, 2, "ab")
print_type(e) # (1, 2, 'ab') <class 'tuple'>
f = range(4)
print_type(f) # range(0, 4) <class 'range'>
g = {"A": 10, "B": 7}
print_type(g) # {'A': 10, 'B': 7} <class 'dict'>
h = {1, 2, "ab"}
print_type(h) # {1, 2, 'ab'} <class 'set'>
i = True
print_type(i) # True <class 'bool'>
j = b"byte string"
print_type(j) # b'byte string' <class 'bytes'>
k = None
print_type(k) # None <class 'NoneType'>
