"""
A module to implement all pythons magic method
"""

# Construction and initialization

import os


class FileObject:
    """Wrapper for file objects to make sure the file gets closed on deletion"""

    def __init__(self, filepath='~', filename='sample.txt'):
        # open a file filename in filepath in read and write mode
        self.file = open(os.path.join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file


# Comparison magic methods

class Word(str):
    """class for words, defining comparison based on word length"""
    def __new__(cls, word):
        # note that we have to use __new__. This is because str is an immutable type.
        # so we have to initialize it early (at creation)
        if ' ' in word:
            print("Value contains spaces. Truncating to first space")
            word = word[:word.index(' ')]  # Word is now all chars before first space
            return str.__new__(cls, word)

        def __gt__(self, other):
            return len(self) > len(other)

        def __lt__(self, other):
            return len(self) < len(other)

        def __ge__(self, other):
            return len(self) >= len(other)

        def __le__(self, other):
            return len(self) <= len(other)


# Numeric magic methods

# 1 Unary operators and functions

"""
__pos__(self)
Implements behavior for unary positive (e.g. +some_object)

__neg__(self)
Implements behavior for negation (e.g. -some_object)

__abs__(self)
Implements behavior for the built in abs() function.

__invert__(self)
Implements behavior for inversion using the ~ operator. For an explanation on what this does, 
see the Wikipedia article on bitwise operations.

__round__(self, n)
Implements behavior for the built in round() function. n is the number of decimal places to round to.

__floor__(self)
Implements behavior for math.floor(), i.e., rounding down to the nearest integer.

__ceil__(self)
Implements behavior for math.ceil(), i.e., rounding up to the nearest integer.

__trunc__(self)
Implements behavior for math.trunc(), i.e., truncating to an integral.
"""

# 2 Normal arithmetic operators

"""
__add__(self, other)
Implements addition.

__sub__(self, other)
Implements subtraction.

__mul__(self, other)
Implements multiplication.

__floordiv__(self, other)
Implements integer division using the // operator.

__div__(self, other)
Implements division using the / operator.

__truediv__(self, other)
Implements true division. Note that this only works when from __future__ import division is in effect.

__mod__(self, other)
Implements modulo using the % operator.

__divmod__(self, other)
Implements behavior for long division using the divmod() built in function.

__pow__
Implements behavior for exponents using the ** operator.

__lshift__(self, other)
Implements left bitwise shift using the << operator.

__rshift__(self, other)
Implements right bitwise shift using the >> operator.

__and__(self, other)
Implements bitwise and using the & operator.

__or__(self, other)
Implements bitwise or using the | operator.

__xor__(self, other)
Implements bitwise xor using the ^ operator.

"""


# 3 Reflected arithmetic operators

"""
__radd__(self, other)
Implements reflected addition.

__rsub__(self, other)
Implements reflected subtraction.

__rmul__(self, other)
Implements reflected multiplication.

__rfloordiv__(self, other)
Implements reflected integer division using the // operator.

__rdiv__(self, other)
Implements reflected division using the / operator.

__rtruediv__(self, other)
Implements reflected true division. Note that this only works when from __future__ import division is in effect.

__rmod__(self, other)
Implements reflected modulo using the % operator.

__rdivmod__(self, other)
Implements behavior for long division using the divmod() built in function, when divmod(other, self) is called.

__rpow__
Implements behavior for reflected exponents using the ** operator.

__rlshift__(self, other)
Implements reflected left bitwise shift using the << operator.

__rrshift__(self, other)
Implements reflected right bitwise shift using the >> operator.

__rand__(self, other)
Implements reflected bitwise and using the & operator.

__ror__(self, other)
Implements reflected bitwise or using the | operator.

__rxor__(self, other)
Implements reflected bitwise xor using the ^ operator.
"""

# 4 Augmented assignment

"""
__iadd__(self, other)
Implements addition with assignment.

__isub__(self, other)
Implements subtraction with assignment.

__imul__(self, other)
Implements multiplication with assignment.

__ifloordiv__(self, other)
Implements integer division with assignment using the //= operator.

__idiv__(self, other)
Implements division with assignment using the /= operator.

__itruediv__(self, other)
Implements true division with assignment. Note that this only works when from __future__ import division is in effect.

__imod__(self, other)
Implements modulo with assignment using the %= operator.

__ipow__
Implements behavior for exponents with assignment using the **= operator.

__ilshift__(self, other)
Implements left bitwise shift with assignment using the <<= operator.

__irshift__(self, other)
Implements right bitwise shift with assignment using the >>= operator.

__iand__(self, other)
Implements bitwise and with assignment using the &= operator.

__ior__(self, other)
Implements bitwise or with assignment using the |= operator.

__ixor__(self, other)
Implements bitwise xor with assignment using the ^= operator.
"""


# 5 Type conversion magic methods

"""
__int__(self)
Implements type conversion to int.

__long__(self)
Implements type conversion to long.

__float__(self)
Implements type conversion to float.

__complex__(self)
Implements type conversion to complex.

__oct__(self)
Implements type conversion to octal.

__hex__(self)
Implements type conversion to hexadecimal.

__index__(self)
Implements type conversion to an int when the object is used in a slice expression. 
If you define a custom numeric type that might be used in slicing, you should define __index__.

__trunc__(self)
Called when math.trunc(self) is called. __trunc__ should return the value of `self truncated to an 
integral type (usually a long).

__coerce__(self, other)
Method to implement mixed mode arithmetic. __coerce__ should return None if type conversion is impossible. Otherwise, 
it should return a pair (2-tuple) of self and other, manipulated to have the same type.
"""

# Representing your Classes.

"""
__str__(self)
Defines behavior for when str() is called on an instance of your class.

__repr__(self)
Defines behavior for when repr() is called on an instance of your class. The major difference between str() and repr() 
is intended audience. repr() is intended to produce output that is mostly machine-readable (in many cases, it could be 
valid Python code even), whereas str() is intended to be human-readable.

__unicode__(self)
Defines behavior for when unicode() is called on an instance of your class. unicode() is like str(), but it returns a 
unicode string. Be wary: if a client calls str() on an instance of your class and you've only defined __unicode__(), 
it won't work. You should always try to define __str__() as well in case someone doesn't have the luxury of using unicode.

__format__(self, formatstr)
Defines behavior for when an instance of your class is used in new-style string formatting. For instance, 
"Hello, {0:abc}!".format(a) would lead to the call a.__format__("abc"). This can be useful for defining your own 
numerical or string types that you might like to give special formatting options.

__hash__(self)
Defines behavior for when hash() is called on an instance of your class. It has to return an integer, and its result 
is used for quick key comparison in dictionaries. Note that this usually entails implementing __eq__ as well. 
Live by the following rule: a == b implies hash(a) == hash(b).

__nonzero__(self)
Defines behavior for when bool() is called on an instance of your class. Should return True or False, 
depending on whether you would want to consider the instance to be True or False.

__dir__(self)
Defines behavior for when dir() is called on an instance of your class. This method should return a list of attributes 
for the user. Typically, implementing __dir__ is unnecessary, but it can be vitally important for interactive use of 
your classes if you redefine __getattr__ or __getattribute__ (which you will see in the next section) or 
are otherwise dynamically generating attributes.


__sizeof__(self)
Defines behavior for when sys.getsizeof() is called on an instance of your class. This should return the size of your 
object, in bytes. This is generally more useful for Python classes implemented in C extensions, but it helps to be aware of it.
"""

# Controlling Attribute Access

"""
__getattr__(self, name)
You can define behavior for when a user attempts to access an attribute that doesn't exist (either at all or yet). 
This can be useful for catching and redirecting common misspellings, giving warnings about using deprecated attributes 
(you can still choose to compute and return that attribute, if you wish), or deftly handing an AttributeError. 
It only gets called when a nonexistent attribute is accessed, however, so it isn't a true encapsulation solution.

__setattr__(self, name, value)
Unlike __getattr__, __setattr__ is an encapsulation solution. It allows you to define behavior for assignment to an 
attribute regardless of whether or not that attribute exists, meaning you can define custom rules for any changes in 
the values of attributes. However, you have to be careful with how you use __setattr__, as the example at the 
end of the list will show.

__delattr__(self, name)
This is the exact same as __setattr__, but for deleting attributes instead of setting them. The same precautions 
need to be taken as with __setattr__ as well in order to prevent infinite recursion (calling del self.name 
in the implementation of __delattr__ would cause infinite recursion).

__getattribute__(self, name)
After all this, __getattribute__ fits in pretty well with its companions __setattr__ and __delattr__. However, 
I don't recommend you use it. __getattribute__ can only be used with new-style classes (all classes are new-style 
in the newest versions of Python, and in older versions you can make a class new-style by subclassing object. 
It allows you to define rules for whenever an attribute's value is accessed. It suffers from some similar 
infinite recursion problems as its partners-in-crime (this time you call the base class's __getattribute__ 
method to prevent this). It also mainly obviates the need for __getattr__, which, when __getattribute__ is implemented, 
only gets called if it is called explicitly or an AttributeError is raised. This method can be used (after all, 
it's your choice), but I don't recommend it because it has a small use case (it's far more rare that we need 
special behavior to retrieve a value than to assign to it) and because it can be really difficult to implement bug-free.
"""


def __setattr__(self, name, value):
    self.name = value
    # since every time an attribute is assigned, __setattr__() is called, this
    # is recursion.
    # so this really means self.__setattr__('name', value). Since the method
    # keeps calling itself, the recursion goes on forever causing a crash


def __setattr__(self, name, value):
    self.__dict__[name] = value # assigning to the dict of names in the class
    # define custom behavior here


class AccessCounter(object):
    '''A class that contains a value and implements an access counter.
    The counter increments each time the value is changed.'''

    def __init__(self, val):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        # Make this unconditional.
        # If you want to prevent other attributes to be set, raise AttributeError(name)
        super(AccessCounter, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)


# Making Custom Sequences

"""
__len__(self)
Returns the length of the container. Part of the protocol for both immutable and mutable containers.

__getitem__(self, key)
Defines behavior for when an item is accessed, using the notation self[key]. This is also part of both the mutable 
and immutable container protocols. It should also raise appropriate exceptions: TypeError if the type of the key 
is wrong and KeyError if there is no corresponding value for the key.

__setitem__(self, key, value)
Defines behavior for when an item is assigned to, using the notation self[nkey] = value. This is part of the 
mutable container protocol. Again, you should raise KeyError and TypeError where appropriate.

__delitem__(self, key)
Defines behavior for when an item is deleted (e.g. del self[key]). This is only part of the mutable container protocol. 
You must raise the appropriate exceptions when an invalid key is used.

__iter__(self)
Should return an iterator for the container. Iterators are returned in a number of contexts, most notably by 
the iter() built in function and when a container is looped over using the form for x in container:. Iterators 
are their own objects, and they also must define an __iter__ method that returns self.

__reversed__(self)
Called to implement behavior for the reversed() built in function. Should return a reversed version of the sequence. 
Implement this only if the sequence class is ordered, like list or tuple.

__contains__(self, item)
__contains__ defines behavior for membership tests using in and not in. Why isn't this part of a sequence protocol, 
you ask? Because when __contains__ isn't defined, Python just iterates over the sequence and returns 
True if it comes across the item it's looking for.

__missing__(self, key)
__missing__ is used in subclasses of dict. It defines behavior for whenever a key is accessed that does not 
exist in a dictionary (so, for instance, if I had a dictionary d and said d["george"] when "george" is 
not a key in the dict, d.__missing__("george") would be called).

"""


class FunctionalList:
    '''A class wrapping a list with some extra functional magic, like head,
    tail, init, last, drop, and take.'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key is of invalid type or value, the list values will raise the error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)

    def head(self):
        # get the first element
        return self.values[0]

    def tail(self):
        # get all elements after the first
        return self.values[1:]

    def init(self):
        # get elements up to the last
        return self.values[:-1]

    def last(self):
        # get last element
        return self.values[-1]

    def drop(self, n):
        # get all elements except first n
        return self.values[n:]

    def take(self, n):
        # get first n elements
        return self.values[:n]


# Reflection

"""
__instancecheck__(self, instance)
Checks if an instance is an instance of the class you defined (e.g. isinstance(instance, class).

__subclasscheck__(self, subclass)
Checks if a class subclasses the class you defined (e.g. issubclass(subclass, class)).
"""


# Callable Objects


class Entity:
    '''Class to represent an entity. Callable to update the entity's position.'''

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''Change the position of the entity.'''
        self.x, self.y = x, y

    # snip...


# Context Managers

"""
__enter__(self)
Defines what the context manager should do at the beginning of the block created by the with statement. 
Note that the return value of __enter__ is bound to the target of the with statement, or the name after the as.

__exit__(self, exception_type, exception_value, traceback)
Defines what the context manager should do after its block has been executed (or terminates). 
It can be used to handle exceptions, perform cleanup, or do something always done immediately after the action 
in the block. If the block executes successfully, exception_type, exception_value, and traceback will be None. 
Otherwise, you can choose to handle the exception or let the user handle it; if you want to handle it, 
make sure __exit__ returns True after all is said and done. If you don't want the exception to be 
handled by the context manager, just let it happen.
"""


class Closer:
    '''A context manager to automatically close an object with a close method
    in a with statement.'''

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj # bound to target

    def __exit__(self, exception_type, exception_val, trace):
        try:
           self.obj.close()
        except AttributeError: # obj isn't closable
           print('Not closable.')
           return True # exception handled successfully


# Here's an example of Closer in action, using an FTP connection to demonstrate it (a closable socket):

from ftplib import FTP

with Closer(FTP('ftp.somesite.com')) as conn:
    conn.dir()
# long AttributeError message, can't use a connection that's closed

with Closer(int(5)) as i:
    i += 1


# ABC
# Building Descriptor Objects


"""
To be a descriptor, a class must have at least one of __get__, __set__, and __delete__ implemented. 
Let's take a look at those magic methods:

__get__(self, instance, owner)
Define behavior for when the descriptor's value is retrieved. instance is the instance of the owner object. 
owner is the owner class itself.

__set__(self, instance, value)
Define behavior for when the descriptor's value is changed. instance is the instance of the owner class and value 
is the value to set the descriptor to.

__delete__(self, instance)
Define behavior for when the descriptor's value is deleted. instance is the instance of the owner object.
"""


class Meter(object):
    '''Descriptor for a meter.'''

    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Foot(object):
    '''Descriptor for a foot.'''

    def __get__(self, instance, owner):
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Distance(object):
    '''Class to represent distance holding two descriptors for feet and
    meters.'''
    meter = Meter()
    foot = Foot()


# Copying

"""
__copy__(self)
Defines behavior for copy.copy() for instances of your class. copy.copy() returns a shallow copy of your object -- 
this means that, while the instance itself is a new instance, all of its data is referenced -- i.e., the object itself 
is copied, but its data is still referenced (and hence changes to data in a shallow copy may cause changes in the original).

__deepcopy__(self, memodict={})
Defines behavior for copy.deepcopy() for instances of your class. copy.deepcopy() returns a deep copy of your object -- 
the object and its data are both copied. memodict is a cache of previously copied objects -- this optimizes copying 
and prevents infinite recursion when copying recursive data structures. When you want to deep copy an individual 
attribute, call copy.deepcopy() on that attribute with memodict as the first argument.
"""


# Pickling your own Objects

"""
__getinitargs__(self)
If you'd like for __init__ to be called when your class is unpickled, you can define __getinitargs__, which should 
return a tuple of the arguments that you'd like to be passed to __init__. Note that this method will only work for old-style classes.

__getnewargs__(self)
For new-style classes, you can influence what arguments get passed to __new__ upon unpickling. 
This method should also return a tuple of arguments that will then be passed to __new__.

__getstate__(self)
Instead of the object's __dict__ attribute being stored, you can return a custom state to be stored when the object 
is pickled. That state will be used by __setstate__ when the object is unpickled.

__setstate__(self, state)
When the object is unpickled, if __setstate__ is defined the object's state will be passed to it instead of directly 
applied to the object's __dict__. This goes hand in hand with __getstate__: when both are defined, 
you can represent the object's pickled state however you want with whatever you want.

__reduce__(self)
When defining extension types (i.e., types implemented using Python's C API), you have to tell Python how to pickle 
them if you want them to pickle them. __reduce__() is called when an object defining it is pickled. It can either 
return a string representing a global name that Python will look up and pickle, or a tuple. The tuple contains 
between 2 and 5 elements: a callable object that is called to recreate the object, a tuple of arguments for that 
callable object, state to be passed to __setstate__ (optional), an iterator yielding list items to be pickled (optional), 
and an iterator yielding dictionary items to be pickled (optional).

__reduce_ex__(self)
__reduce_ex__ exists for compatibility. If it is defined, __reduce_ex__ will be called over __reduce__ on pickling. 
__reduce__ can be defined as well for older versions of the pickling API that did not support __reduce_ex__.
"""


import time


class Slate:
    '''Class to store a string and a changelog, and forget its value when pickled.'''

    def __init__(self, value):
        self.value = value
        self.last_change = time.asctime()
        self.history = {}

    def change(self, new_value):
        # Change the value. Commit last value to history
        self.history[self.last_change] = self.value
        self.value = new_value
        self.last_change = time.asctime()

    def print_changes(self):
        print('Changelog for Slate object:')
        for k, v in self.history.items():
            print('%s\t %s' % (k, v))

    def __getstate__(self):
        # Deliberately do not return self.value or self.last_change.
        # We want to have a "blank slate" when we unpickle.
        return self.history

    def __setstate__(self, state):
        # Make self.history = state and last_change and value undefined
        self.history = state
        self.value, self.last_change = None, None
