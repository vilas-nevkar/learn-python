import sys

# Changing the output behaviour of the interactive Python shell
x = 42
print(x)


def my_display(x):
    print("out: ",)
    print(x)


sys.displayhook = my_display
print(x)
