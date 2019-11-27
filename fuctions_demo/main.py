# defining inner function
# CASE 1: outer function is calling inner function


# def outer(value):
#     """
#     Here outer function is calling to inner function it does not return itself
#     :param value:
#     :return:
#     """
#     print("In outer function")
#
#     def inner():
#         print("In inner function")
#         print(value + 2)
#     # calling inner function in outer
#     print("calling inner function")
#     inner()
#
#
# outer(2)


# CASE 1: outer function is returning inner function call
# which is not returning anything

# def outer(value):
#     """
#     Here note the parenthesis while returning inner function
#     removing parenthesis will gives you function reference.
#     Here returning from outer function will give None
#     coz inner function does not have return statement
#     therefore inner function will return None
#     :param value:
#     :return:
#     """
#     print("In outer function")
#
#     def inner():
#         print("In inner function")
#         print(value + 2)
#     # calling inner function in outer
#     print("calling inner function")
#     return inner()

#
# outer(4)
# print()
# print(outer(4))
# print()
# out = outer(4)
# print(out)


# CASE 3: outer function is returning inner function call
# which is returning a value
#
# def outer(value):
#     """
#     Here note the parenthesis while returning inner function
#     removing parenthesis will gives you function reference.
#     Here returning from outer function will give
#     value returned from inner function
#     :param value:
#     :return:
#     """
#     print("In outer function")
#
#     def inner():
#         print("In inner function")
#         print(value + 2)
#         return "Returned {}".format(value + 4)
#     # calling inner function in outer
#     print("calling inner function")
#     return inner()
#
#
# outer(4)
# print()
# out = outer(4)
# print(out)



# CASE 4: outer function is returning inner function reference
# which is not returning anything

# def outer(value):
#     """
#     Here note the absence of parenthesis while returning inner function
#     removing parenthesis will gives you function reference.
#     Here returning from outer function will give callable
#     we can call inner function from outside using its returned reference
#
#     calling outer only executes outer
#     to executes inner you must call returned reference
#     :param value:
#     :return:
#     """
#     print("In outer function")
#
#     def inner():
#         print("In inner function")
#         print(value + 2)
#     # calling inner function in outer
#     print("calling inner function")
#     return inner
#
#
# outer(4)
# print()
# out = outer(4)
# out()
# print()
# print(out())


# CASE 5: outer function is returning inner function reference
# which is returning value


# def outer(value):
#     """
#     Here note the absence of parenthesis while returning inner function
#     removing parenthesis will gives you function reference.
#     Here returning from outer function will give callable
#     we can call inner function from outside using its returned reference
#
#     calling outer only executes outer
#     to executes inner you must call returned reference
#     :param value:
#     :return:
#     """
#     print("In outer function")
#
#     def inner():
#         print("In inner function")
#         print(value + 2)
#         return "Returned {}".format(value + 2)
#     # calling inner function in outer
#     print("calling inner function")
#     return inner
#
#
# outer(4)
# print()
# out = outer(4)
# out()
# print()
# print(out())


# closure demo

def outer(value):
    """
    :param value:
    :return:
    """
    print("In outer function")

    def inner(temp):
        print("In inner function")
        print(value + temp)
    # calling inner function in outer
    print("returning ref of inner function")
    return inner


inner_ref = outer(4)
print()
inner_ref2 = inner_ref
inner_ref3 = outer(4)
inner_ref(6)
print()
inner_ref2(6)
print()
del inner_ref
del outer
inner_ref2(6)
print()
inner_ref3(6)


# function passing demo

"""
All the protocols of inner function are applied to the passed function
passed function can be called
passed function can be returned
"""


def test():
    print("I am going to be passed")

#
# def outer(func):
#     print("In outer function")
#     print("calling passed function")
#     return func


# t = outer(test)
# t()


# def outer(func):
#     print("In outer function")
#     print("calling passed function")
#     return func()


# print(outer(test))


# decorator demo
# CASE 1: without passed function args

"""
TO understand decorator one must understand following
1. Function can be passed to another function
2. Function within function can be defined
3. Enclosing function need to be called
4. Function can return enclosing function as a call or as a ref
5. Function closure
"""


def test():
    print("I am test function")


def decor(func):
    print("Inside decorator")

    def inner():
        print("Inside inner")
        print("I am decorator")
        func()
    return inner


# better = decor(test)
# better()


# CASE 2: With passed function args
# def decor2(func):
#     print('In decorator')
#
#     def inner(a, b):
#         print("decorating")
#         if b == 0:
#             print("division Not possible")
#         else:
#             func(a, b)
#     return inner
#
#
# @decor2
# def div_tes(a, b):
#     print("I am division testing")
#     print(a // b)
#
#
# out = decor2(div_tes)  # If you pass args here, it wont works
# out(10, 0)  # decorator works here only


# CASE 3: using wraps
# CASE 4: With decorator args
