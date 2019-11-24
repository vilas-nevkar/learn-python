def outer(value):
    def inner():
        print(value + 2)
    return inner


print(outer(3))
# out = outer(5)
# print(out)