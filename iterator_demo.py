import getopt
import sys
import argparse
import optparse

mytuple = ("apple", "banana", "cherry")
ml = ["apple", "banana", "cherry"]
print(iter(mytuple))
print(iter(ml))


def gen():
    for i in range(10):
        yield i


a = iter(gen())
# print(next(a))

# b = iter(int, 1)
#
# for i in b:
#     print(i)

print(int())