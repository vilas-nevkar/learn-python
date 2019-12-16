## Functional Python
### Introduction
* History
* Features
* Limitations
* Versions
* Installation
* Running python program

---------------------------------------------------------------------------------------------------------------------

### Basics
* **Statements**

* **Keywords (35)**
    1. Difference between `del` and `None`:
    1. `async` and `await` - python 3.7

* **Character set**
    1. A-Z
    1. a-z
    1. 0-9
    1. Underscore in Python.
        1. For storing the value of last expression in interpreter.
        1. For ignoring the specific values. (so-called “I don’t care”)
        1. To give special meanings and functions to name of vartiables or functions.
        1. To use as ‘Internationalization(i18n)’ or ‘Localization(l10n)’ functions.
        1. To separate the digits of number literal value.
* **Identifiers**
* **Literals**
    1. Int literals
    1. String literals
* **Variables**
* **Constants**
* **comments**
    1. single line
    1. multiline
* **Interactive shell**
* **Indentation**

---------------------------------------------------------------------------------------------------------------------

### Operators
* Types:
    1. **Arithmetic Operators**
        1. `+` ==>Addition
        1. `-` ==>Subtraction
        1. `*` ==>Multiplication
        1. `/`   ==>Division operator
        1. `%`   ===>Modulo operator
        1. `//`  ==>Floor Division operator
        1. `**`  ==>Exponent operator or power operator
    2. **Relational Operators or Comparison Operators**
        * `>`
        * `<`
        * `>=`
        * `>=`
        * `==`
        * `!=`
    3. **Equality operators**
        * `==`
        * `!=`
        * Chaining
    4. **Logical operators**
        * `and`
        * `or`
        * `not`
        * Boolean types behaviour
        * Non boolean types behaviour
    5. **Bitwise oeprators**
        * `&`
        * `|`
        * `^`
        * `~`
        * `<<`
        * `>>`
    6. **Assignment operators**
        * `=`
        * Augmented Assignments
            * `+=`
            * `-=`
            * `*=`
            * `/=`
            * `//=`
            * `**=`
    7. **Ternary operators**
    6. **Special operators**
        
        1. **Identity Operators**
            1. `is`
            2. `is not`
        2. **Membership operators**
            1. `in`
            2. `not in`
    7. **Walrus operator**
        * `->`
* **Operator precedence**

---------------------------------------------------------------------------------------------------------------------

### Data types
* **Fundamental types**
    1. int
    1. float
    1. complex
    1. bool
    1. str

1. **int**
    1. Literals
        1. Binary
        1. Octals
        1. Hexadecimals

2. **float**

3. **complex**

4. **bool**

5. **str**
    1. literals
        1. single line
        1. multiline
    1. Raw strings
    1. Operations
        1. Accessing
        1. Indexing
        1. Slicing
        
    1. Operators for string
        1. `+` operator for concatenation
        2. `*` operator for repetition
        3. <,<=,>,>= Comparison
        4. ==,!= equality
        5. in , not in membership

    1. Formatting
    1. Escape Sequenses
        * \a	ASCII Bell (BEL) character
        * \b	ASCII Backspace (BS) character
        * \f	ASCII Formfeed (FF) character
        * \n	ASCII Linefeed (LF) character
        * \N{<name>}	Character from Unicode database with given <name>
        * \r	ASCII Carriage Return (CR) character
        * \t	ASCII Horizontal Tab (TAB) character
        * \uxxxx	Unicode character with 16-bit hex value xxxx
        * \Uxxxxxxxx	Unicode character with 32-bit hex value xxxxxxxx
        * \v	ASCII Vertical Tab (VT) character
        * \oxx	Character with octal value xx
        * \xhh	Character with hex value hh
    1. Methods
        * capitalize()	Converts the first character to upper case
        * casefold()	Converts string into lower case
        * center()	Returns a centered string
        * count()	Returns the number of times a specified value occurs in a string
        * encode()	Returns an encoded version of the string
        * endswith()	Returns true if the string ends with the specified value
        * expandtabs()	Sets the tab size of the string
        * find()	Searches the string for a specified value and returns the position of where it was found
        * format()	Formats specified values in a string
        * format_map()	Formats specified values in a string
        * index()	Searches the string for a specified value and returns the position of where it was found
        * isalnum()	Returns True if all characters in the string are alphanumeric
        * isalpha()	Returns True if all characters in the string are in the alphabet
        * isdecimal()	Returns True if all characters in the string are decimals
        * isdigit()	Returns True if all characters in the string are digits
        * isidentifier()	Returns True if the string is an identifier
        * islower()	Returns True if all characters in the string are lower case
        * isnumeric()	Returns True if all characters in the string are numeric
        * isprintable()	Returns True if all characters in the string are printable
        * isspace()	Returns True if all characters in the string are whitespaces
        * istitle()	Returns True if the string follows the rules of a title
        * isupper()	Returns True if all characters in the string are upper case
        * join()	Joins the elements of an iterable to the end of the string
        * ljust()	Returns a left justified version of the string
        * lower()	Converts a string into lower case
        * lstrip()	Returns a left trim version of the string
        * maketrans()	Returns a translation table to be used in translations
        * partition()	Returns a tuple where the string is parted into three parts
        * replace()	Returns a string where a specified value is replaced with a specified value
        * rfind()	Searches the string for a specified value and returns the last position of where it was found
        * rindex()	Searches the string for a specified value and returns the last position of where it was found
        * rjust()	Returns a right justified version of the string
        * rpartition()	Returns a tuple where the string is parted into three parts
        * rsplit()	Splits the string at the specified separator, and returns a list
        * rstrip()	Returns a right trim version of the string
        * split()	Splits the string at the specified separator, and returns a list
        * splitlines()	Splits the string at line breaks and returns a list
        * startswith()	Returns true if the string starts with the specified value
        * strip()	Returns a trimmed version of the string
        * swapcase()	Swaps cases, lower case becomes upper case and vice versa
        * title()	Converts the first character of each word to upper case
        * translate()	Returns a translated string
        * upper()	Converts a string into upper case
        * zfill()	Fills the string with a specified number of 0 values at the beginning
6. **bytes**

7. **bytearray**

8. **range**

9. **list**
    1. defining list
        1. list = []
        2. list=[10,20,30,40]
        3. With dynamic input: (eval)
        4. With list() function:
    1. Operations
        1. Indexing
        1. Slicing
        1. Traversing
            1. using for loop
    1. List vs immutability:
    1. cloning
        Difference between = operator and copy() function
    1. Operators for list
        1. Concatenation operator(+):
        2. Repetition Operator(*):
        3. Comparison
            ==,!=
            <,<=,>,>=
        4. in , not in Membership
    1. Nested list
        Nested List as Matrix:
    1. Comprehensions
    1. Methods
        * append()	Adds an element at the end of the list
        * clear()	Removes all the elements from the list
        * copy()	Returns a copy of the list
        * count()	Returns the number of elements with the specified value
        * extend()	Add the elements of a list (or any iterable), to the end of the current list
        * index()	Returns the index of the first element with the specified value
        * insert()	Adds an element at the specified position
        * pop()	Removes the element at the specified position
        * remove()	Removes the first item with the specified value
        * reverse()	Reverses the order of the list
        * sort()	Sorts the list

10. **tuple**
    1. Defining tuple
        1. t=()
        2. t=(10,)
        3. t=10,20,30
        4. tuple()
    1. Operations
        1. Indexing
        1. Slicing
        1. Traversing
            using for loop
    1. Tuple vs immutability:
    1. Operators for tuple
        1. Concatenation operator(+):
        2. Repetition Operator(*):
        3. in , not in Membership
    1. Tuple Packing and Unpacking:
    1. Tuple comprehension
    1. Methods
        * count()	Returns the number of times a specified value occurs in a tuple
        * index()	Searches the tuple for a specified value and returns the position of where it was found

11. **set**
    1. Defining set
        1. using set()
    1. Set vs immutability:
    1. Operations:
        1. Union
        1. Intersection
        1. Difference
        1. Symmetric difference
    1. Operators for set
        1. Membership operators: (in , not in)
    1. Set comprehension
    1. Methods
        * add()	Adds an element to the set
        * clear()	Removes all the elements from the set
        * copy()	Returns a copy of the set
        * difference()	Returns a set containing the difference between two or more sets
        * difference_update()	Removes the items in this set that are also included in another, specified set
        * discard()	Remove the specified item
        * intersection()	Returns a set, that is the intersection of two other sets
        * intersection_update()	Removes the items in this set that are not present in other, specified set(s)
        * isdisjoint()	Returns whether two sets have a intersection or not
        * issubset()	Returns whether another set contains this set or not
        * issuperset()	Returns whether this set contains another set or not
        * pop()	Removes an element from the set
        * remove()	Removes the specified element
        * symmetric_difference()	Returns a set with the symmetric differences of two sets
        * symmetric_difference_update()	inserts the symmetric differences from this set and another
        * union()	Return a set containing the union of sets
        * update()	Update the set with the union of this set and others

12. **frozenset**

13. **dict**
    1. Defining dicts
        1. d = {}
        2. d = dict()
    1. Operations
        1. Accessing
        1. Updating dicts
        1. deleting elements
    1. dict comprehensions
    1. Methods
        * clear()	Removes all the elements from the dictionary
        * copy()	Returns a copy of the dictionary
        * fromkeys()	Returns a dictionary with the specified keys and values
        * get()	Returns the value of the specified key
        * items()	Returns a list containing a tuple for each key value pair
        * keys()	Returns a list containing the dictionary's keys
        * pop()	Removes the element with the specified key
        * popitem()	Removes the last inserted key-value pair
        * setdefault()	Returns the value of the specified key. If the key does not exist:
                        insert the key, with the specified value
        * update()	Updates the dictionary with the specified key-value pairs
        * values()	Returns a list of all the values in the dictionary
14. **None**

---------------------------------------------------------------------------------------------------------------------

### Mutability & Immutability

---------------------------------------------------------------------------------------------------------------------


### Shallow and Deep Copy

---------------------------------------------------------------------------------------------------------------------

### Type Casting
1. int()
1. float()
1. complex()
1. bool()
1. str()
1. list()
1. tuple()

---------------------------------------------------------------------------------------------------------------------

### Input and output statements
1. raw_input()
1. input()
1. print()
    1. Formatted string
        1. %i - int
        1. %d - int
        1. %f - float
        1. %s - String type
        1. print with {} operator

---------------------------------------------------------------------------------------------------------------------

### Command line arguments
1. Modules:
    1. sys
    1. argparse
    1. getopt
    1. optparse

---------------------------------------------------------------------------------------------------------------------

### Flow controls
1. **Conditionals**
    1. if
    2. if-elif
    3. if-elif-else
2. **Iterative**
    1. for-else
    2. while-else
3. **Transfer**
    1. continue
    2. break
    3. pass

---------------------------------------------------------------------------------------------------------------------

### Iterators and Iterable

An object is called iterable if we can get an iterator from it
1. Creating iterator
2. Iterating iterator
3. Internal working of for loop
4. Building your own iterator
4. Infinite Iterators

---------------------------------------------------------------------------------------------------------------------

### Functions:
**Types:**
1. **Built in Functions**
    1.  **Math**
        1. abs()	Returns absolute value of a number
        1. divmod()	Returns quotient and remainder of integer division
        1. max()	Returns the largest of the given arguments or items in an iterable
        1. min()	Returns the smallest of the given arguments or items in an iterable
        1. pow()	Raises a number to a power
        1. round()	Rounds a floating-point value
        1. sum()	Sums the items of an iterable

    1. **Type Conversion**
        1. ascii()	Returns a string containing a printable representation of an object
        1. bin()	Converts an integer to a binary string
        1. bool()	Converts an argument to a Boolean value
        1. chr()	Returns string representation of character given by integer argument
        1. complex()	Returns a complex number constructed from arguments
        1. float()	Returns a floating-point object constructed from a number or string
        1. hex()	Converts an integer to a hexadecimal string
        1. int()	Returns an integer object constructed from a number or string
        1. oct()	Converts an integer to an octal string
        1. ord()	Returns integer representation of a character
        1. repr()	Returns a string containing a printable representation of an object
        1. str()	Returns a string version of an object
        1. type()	Returns the type of an object or creates a new type object

    1. **Iterables and Iterators**
        1. all()	Returns True if all elements of an iterable are true
        1. any()	Returns True if any elements of an iterable are true
        1. enumerate()	Returns a list of tuples containing indices and values from an iterable
        1. filter()	Filters elements from an iterable
        1. iter()	Returns an iterator object
        1. len()	Returns the length of an object
        1. map()	Applies a function to every item of an iterable
        1. next()	Retrieves the next item from an iterator
        1. range()	Generates a range of integer values
        1. reversed()	Returns a reverse iterator
        1. slice()	Returns a slice object
        1. sorted()	Returns a sorted list from an iterable
        1. zip()	Creates an iterator that aggregates elements from iterables

    1. **Composite Data Type**
        1. bytearray()	Creates and returns an object of the bytearray class
        1. bytes()	Creates and returns a bytes object (similar to bytearray, but immutable)
        1. dict()	Creates a dict object
        1. frozenset()	Creates a frozenset object
        1. list()	Constructs a list object
        1. object()	Returns a new featureless object
        1. set()	Creates a set object
        1. tuple()	Creates a tuple object

    1. **Classes, Attributes, and Inheritance**
        1. classmethod()	Returns a class method for a function
        1. delattr()	Deletes an attribute from an object
        1. getattr()	Returns the value of a named attribute of an object
        1. hasattr()	Returns True if an object has a given attribute
        1. isinstance()	Determines whether an object is an instance of a given class
        1. issubclass()	Determines whether a class is a subclass of a given class
        1. property()	Returns a property value of a class
        1. setattr()	Sets the value of a named attribute of an object
        1. super()	Returns a proxy object that delegates method calls to a parent or sibling class

    1. **Input/Output**
        1. format()	Converts a value to a formatted representation
        1. input()	Reads input from the console
        1. open()	Opens a file and returns a file object
        1. print()	Prints to a text stream or the console
        1. Variables, References, and Scope
        1. Function	Description
        1. dir()	Returns a list of names in current local scope or a list of object attributes
        1. globals()	Returns a dictionary representing the current global symbol table
        1. id()	Returns the identity of an object
        1. locals()	Updates and returns a dictionary representing current local symbol table
        1. vars()	Returns __dict__ attribute for a module, class, or object

    1. **Miscellaneous**
        1. callable()	Returns True if object appears callable
        1. compile()	Compiles source into a code or AST object
        1. eval()	Evaluates a Python expression
        1. exec()	Implements dynamic execution of Python code
        1. hash()	Returns the hash value of an object
        1. help()	Invokes the built-in help system
        1. memoryview()	Returns a memory view object
        1. staticmethod()	Returns a static method for a function
        1. `__import__()`	Invoked by the import statement


1. **User Defined Functions**
    1. defining a function
    2. calling a function
    3. returning from function
    1. namespace
    1. global Vs local variables
    4. function arguments
        1. positional args
        2. default args
        3. keyword args
        4. `**args`
        5. `**kwargs`
    5. Nested functions
        1. defining nested function
        2. calling nested function
        3. returning nested functions which is not returning value
        3. returning nested functions which is returning value
        4. returning nested function reference which is not returning value
        4. returning nested function reference which is returning value
        5. function closure
        6. use of `global` keyword
        7. use of `nonlocal` keyword
    6. function aliasing
    7. Function as a argument
        1. calling passed function
        2. returning passed function call
        3. returning passed function reference
    7. generators
        1. Using functions
        2. Using tuple comprehension
        3. yield from
        4. `send()`
    8. function decorators
        1. without function args
        2. with function args
        3. with decorator args
        4. with @wrap
        5. decorator chaining
    9. Recursive functions
    10. Lambda function

---------------------------------------------------------------------------------------------------------------------

### Special variables
1. `__init__`
1. `__name__`
1. `__main__`
1. `__doc__`
1. `__closure__`
1. `__module__`
1. `__file__`
1. `__builtins__`
1. `__loader__`
1. `__spec__`
1. `__package__`
1. `__class__`
1. `__bases__`

---------------------------------------------------------------------------------------------------------------------

### File Handling
1. **syntax**
    1. open()
    2. with open()

2. **Access modes**

     1. ``r''   Open text file for reading.  The stream is positioned at the
             beginning of the file.

     1. ``r+''  Open for reading and writing.  The stream is positioned at the
             beginning of the file.

     1. ``w''   Truncate file to zero length or create text file for writing.
             The stream is positioned at the beginning of the file.

     1. ``w+''  Open for reading and writing.  The file is created if it does not
             exist, otherwise it is truncated.  The stream is positioned at
             the beginning of the file.

     1. ``a''   Open for writing.  The file is created if it does not exist.  The
             stream is positioned at the end of the file.  Subsequent writes
             to the file will always end up at the then current end of file,
             irrespective of any intervening fseek(3) or similar.

     1. ``a+''  Open for reading and writing.  The file is created if it does not
             exist.  The stream is positioned at the end of the file.  Subse-
             quent writes to the file will always end up at the then current
             end of file, irrespective of any intervening fseek(3) or similar.

    1. 'x'	Creates a new file. If file already exists, the operation fails.
    1. 't'	This is the default mode. It opens in text mode.
    1. 'b'	This opens in binary mode.

3. **Methods**
    1. close()	Close an open file. It has no effect if the file is already closed.
    1. detach()	Separate the underlying binary buffer from the TextIOBase and return it.
    1. fileno()	Return an integer number (file descriptor) of the file.
    1. flush()	Flush the write buffer of the file stream.
    1. isatty()	Return True if the file stream is interactive.
    1. read(n)	Read atmost n characters form the file. Reads till end of file if it is negative or None.
    1. readable()	Returns True if the file stream can be read from.
    1. readline(n=-1)	Read and return one line from the file. Reads in at most n bytes if specified.
    1. readlines(n=-1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
    1. seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
    1. seekable()	Returns True if the file stream supports random access.
    1. tell()	Returns the current file location.
    1. truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
    1. writable()	Returns True if the file stream can be written to.
    1. write(s)	Write string s to the file and return the number of characters written.
    1. writelines(lines)	Write a list of lines to the file.

4. **Modules:**
    1. os
    1. pathlib
    1. tempfile
    1. shutil
    1. zipfile
    1. tarfile
    1. fileinput

5. **Common Operation**
    1. Get directory contents and file properties
    1. Create directories and directory trees
    1. Filename pattern matching
    1. Traversing dir and processing file
    1. Deleting files and dir
    1. Move, rename, copy, and delete files or directories
    1. Create temporary files and directories
    1. Read and extract data from different types of archives
        1. zip
        1. tar
    1. Read multiple files simultaneously using fileinput
    1. Reading continuously growing file

6. Working with csv files
7. working with JSON data

---------------------------------------------------------------------------------------------------------------------
### Context Managers
* with function
* with classes

---------------------------------------------------------------------------------------------------------------------

### Exception handling
1. **keywords**
    1. try
    1. except
    1. finally
    1. else
    1. raise

1. **Exception hierarchy**
   
    1. BaseException
        * SystemExit
        * KeyboardInterrupt
        * GeneratorExit
        * Exception
            * StopIteration
            * StopAsyncIteration
            * ArithmeticError
                * FloatingPointError
                * OverflowError
                * ZeroDivisionError
            * AssertionError
          * AttributeError
          * BufferError
          * EOFError
          * ImportError
              * ModuleNotFoundError
          * LookupError
              * IndexError
              * KeyError
          * MemoryError
          * NameError
            * UnboundLocalError
          * OSError
              * BlockingIOError
              * ChildProcessError
              * ConnectionError
                  * BrokenPipeError
                  * ConnectionAbortedError
                  * ConnectionRefusedError
                  * ConnectionResetError
              * FileExistsError
              * FileNotFoundError
              * InterruptedError
              * IsADirectoryError
              * NotADirectoryError
              * PermissionError
              * ProcessLookupError
              * TimeoutError
          * ReferenceError
          * RuntimeError
              * NotImplementedError
              * RecursionError
          * SyntaxError
            * IndentationError
                * TabError
          * SystemError
          * TypeError
          * ValueError
            * UnicodeError
              * UnicodeDecodeError
              * UnicodeEncodeError
              * UnicodeTranslateError
          * Warning
               * DeprecationWarning
               * PendingDeprecationWarning
               * RuntimeWarning
               * SyntaxWarning
               * UserWarning
               * FutureWarning
               * ImportWarning
               * UnicodeWarning
               * BytesWarning
               * ResourceWarning
---------------------------------------------------------------------------------------------------------------------

### Regular expression

1. Metacharacters:

    1. `\`	escape special characters
    1. `.`	matches any character
    1. `^`	matches beginning of string
    1. `$`	matches end of string
    1. `[5b-d]`	matches any chars '5', 'b', 'c' or 'd'
    1. `[^a-c6]`	matches any char except 'a', 'b', 'c' or '6'
    1. `R|S`	matches either regex R or regex S
    1. `()`	creates a capture group and indicates precedence
    
1. Quantifiers    
    1. `*`  0 or more (append ? for non-greedy)
    1. `+`	1 or more (append ? for non-greedy)
    1. `?`	0 or 1 (append ? for non-greedy)
    1. `{m}`	exactly mm occurrences
    1. `{m, n}`	from m to n. m defaults to 0, n to infinity
    1. `{m, n}?`	from m to n, as few as possible
    
1. Special sequences    
    1. `\A`	start of string
    1. `\b`	matches empty string at word boundary (between \w and \W)
    1. `\B`	matches empty string not at word boundary
    1. `\d`	digit
    1. `\D`	non-digit
    1. `\s`	whitespace: `[ \t\n\r\f\v]`
    1. `\S`	non-whitespace
    1. `\w`	alphanumeric: `[0-9a-zA-Z_]`
    1. `\W`	non-alphanumeric
    1. `\Z`	end of string
    1. `\g<id>`	matches a previously defined group
    1. `(?iLmsux)`	matches empty string, sets re.X flags
    1. `(?:...)`	non-capturing version of regular parentheses
    1. `(?P...)`	matches whatever matched previously named group
    1. `(?P=)`	digit
    1. `(?#...)`	a comment; ignored
    1. `(?=...)`	lookahead assertion: matches without consuming
    1. `(?!...)`	negative lookahead assertion
    1. `(?<=...)`	lookbehind assertion: matches if preceded
    1. `(?<!...)`	negative lookbehind assertion
    1. `(?(id)yes|no)`	match 'yes' if group 'id' matched, else 'no'
    
1. Method:
    1. `match()` Returns match object on successful search
    1. `findall()`	Returns a list containing all matches
    1. `search()`	Returns a Match object if there is a match anywhere in the string
    1. `split()`	Returns a list where the string has been split at each match
    1. `sub()`	Replaces one or many matches with a string
    1. `subn()` The re.subn() is similar to re.sub() except it returns a tuple of 2 items containing the new string and the number of substitutions made.

1. Flags:

    1. [re.M]	Make begin/end consider each line
    1. [re.I]	It ignores case
    1. [re.S]	Make [ . ]
    1. [re.U]	Make { \w,\W,\b,\B} follows Unicode rules
    1. [re.L]	Make {\w,\W,\b,\B} follow locale
    1. [re.X]	Allow comment in Regex
---------------------------------------------------------------------------------------------------------------------

## Modular Python
1. Builtin modules
2. User defined modules
3. Imports
    1. Absolute imports
    2. Relative imports
4. Module aliasing while importing
5. Member aliasing
6. Reloading a module
7. Finding members of module using dir()
4. `if __name__ == '__main__'`

---------------------------------------------------------------------------------------------------------------------

### Packages
1. Builtin packages
2. User defined packages
3. Use of `__init__`

---------------------------------------------------------------------------------------------------------------------

### Package management
* What is PIP
* easy_install
* Installing packages

---------------------------------------------------------------------------------------------------------------------

### Environments
* Whats is envs
* Creating envs
    * Using Pipenv
    * Using virtualenv
* activating and deactivating envs
* Installing packages in envs

---------------------------------------------------------------------------------------------------------------------
### Database Programming

1. Modules:

---------------------------------------------------------------------------------------------------------------------

## Object Oriented Python

### Python magic methods (Object oriented python)

    # Numeric magic methods

        # 1 Unary operators and functions

            __pos__(self)
            __neg__(self)
            __abs__(self)
            __invert__(self)
            __round__(self, n)
            __floor__(self)
            __ceil__(self)
            __trunc__(self)

        2 Normal arithmetic operators

            __add__(self, other)
            __sub__(self, other)
            __mul__(self, other)
            __floordiv__(self, other)
            __div__(self, other)
            __truediv__(self, other)
            __mod__(self, other)
            __divmod__(self, other)
            __pow__
            __lshift__(self, other)
            __rshift__(self, other)
            __and__(self, other)
            __or__(self, other)
            __xor__(self, other)

        # 3 Reflected arithmetic operators

            __radd__(self, other)
            __rsub__(self, other)
            __rmul__(self, other)
            __rfloordiv__(self, other)
            __rdiv__(self, other)
            __rtruediv__(self, other)
            __rmod__(self, other)
            __rdivmod__(self, other)
            __rpow__
            __rlshift__(self, other)
            __rrshift__(self, other)
            __rand__(self, other)
            __ror__(self, other)
            __rxor__(self, other)

    # 4 Augmented assignment

        __iadd__(self, other)
        __isub__(self, other)
        __imul__(self, other)
        __ifloordiv__(self, other)
        __idiv__(self, other)
        __itruediv__(self, other)
        __imod__(self, other)
        __ipow__
        __ilshift__(self, other)
        __irshift__(self, other)
        __iand__(self, other)
        __ior__(self, other)
        __ixor__(self, other)

    # 5 Type conversion magic methods

        __int__(self)
        __long__(self)
        __float__(self)
        __complex__(self)
        __oct__(self)
        __hex__(self)
        __index__(self)
        __trunc__(self)
        __coerce__(self, other)

    # Representing your Classes.

        __str__(self)
        __repr__(self)
        __unicode__(self)
        __format__(self, formatstr)
        __hash__(self)
        __nonzero__(self)
        __dir__(self)
        __sizeof__(self)

    # Controlling Attribute Access

        __getattr__(self, name)
        __setattr__(self, name, value)
        __delattr__(self, name)
        __getattribute__(self, name)

    # Making Custom Sequences

        __len__(self)
        __getitem__(self, key)
        __setitem__(self, key, value)
        __delitem__(self, key)
        __iter__(self)
        __reversed__(self)
        __contains__(self, item)
        __missing__(self, key)

    # Reflection

        __instancecheck__(self, instance)
        __subclasscheck__(self, subclass)

    # Context Managers

        __enter__(self)
        __exit__(self, exception_type, exception_value, traceback)

    # Building Descriptor Objects

        __get__(self, instance, owner)
        __set__(self, instance, value)
        __delete__(self, instance)

    # Copying

        __copy__(self)
        __deepcopy__(self, memodict={})

    # Pickling your own Objects

        __getinitargs__(self)
        __getnewargs__(self)
        __getstate__(self)
        __setstate__(self, state)
        __reduce__(self)
        __reduce_ex__(self)
        __reduce_ex__ exists for compatibility. If it is defined, __reduce_ex__ will be called over __reduce__ on pickling.
        __reduce__ can be defined as well for older versions of the pickling API that did not support __reduce_ex__.
