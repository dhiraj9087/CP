from shutil import register_unpack_format


def func(n):
    return abs(n-50)

list=[100,50,23,80,65]
list.sort(key=func)
print(list)