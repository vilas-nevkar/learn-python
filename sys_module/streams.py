import sys

# Standard data streams
# The following example illustrates the usage of the standard data streams:
print("Going via stdout")
sys.stdout.write("Another way to do it!\n")
x = input("Enter name: ")
print(x)
print('Typed in value', sys.stdin.readline()[:-1])


# The following example combines input and output:
while True:
    print("Yet another iteration")
    try:
        # reading from sys.stdin
        number = input("Enter a number: ")
    except EOFError:
        print("\nciao")
        break
    else:
        number = int(number)
        if number == 0:
            print(sys.stderr, "0 has no inverse")
        else:
            print("inverse of %d is %f" % (number, 1.0/number))
