"""
Introduction
    History
    Features
    Limitations
    Versions
    Installation
    Running python program

Basics
    Statements
    Keywords
    Character set
    Identifiers
    Variables
    comments
        single line
        multiline
    Interactive shell
    Indentations

Data types
    Fundamental types
        int
        float
        complex
        bool
        str

    1. int
        Literals
            Binary
            Octals
            Hexadecimals

    2. float
    3.complex
    4.bool
    5.str
        literals
            single line
            multiline
        Raw strings
        Accessing
            Indexing
            Slicing
        Operators for string
            1. + operator for concatenation
            2. * operator for repetition
            3. <,<=,>,>= Comparison
            4. ==,!= equality
            5. in , not in membership

        Formatting
        Escape Sequenses
            \a	ASCII Bell (BEL) character
            \b	ASCII Backspace (BS) character
            \f	ASCII Formfeed (FF) character
            \n	ASCII Linefeed (LF) character
            \N{<name>}	Character from Unicode database with given <name>
            \r	ASCII Carriage Return (CR) character
            \t	ASCII Horizontal Tab (TAB) character
            \uxxxx	Unicode character with 16-bit hex value xxxx
            \Uxxxxxxxx	Unicode character with 32-bit hex value xxxxxxxx
            \v	ASCII Vertical Tab (VT) character
            \oxx	Character with octal value xx
            \xhh	Character with hex value hh
        Methods
            capitalize()	Converts the first character to upper case
            casefold()	Converts string into lower case
            center()	Returns a centered string
            count()	Returns the number of times a specified value occurs in a string
            encode()	Returns an encoded version of the string
            endswith()	Returns true if the string ends with the specified value
            expandtabs()	Sets the tab size of the string
            find()	Searches the string for a specified value and returns the position of where it was found
            format()	Formats specified values in a string
            format_map()	Formats specified values in a string
            index()	Searches the string for a specified value and returns the position of where it was found
            isalnum()	Returns True if all characters in the string are alphanumeric
            isalpha()	Returns True if all characters in the string are in the alphabet
            isdecimal()	Returns True if all characters in the string are decimals
            isdigit()	Returns True if all characters in the string are digits
            isidentifier()	Returns True if the string is an identifier
            islower()	Returns True if all characters in the string are lower case
            isnumeric()	Returns True if all characters in the string are numeric
            isprintable()	Returns True if all characters in the string are printable
            isspace()	Returns True if all characters in the string are whitespaces
            istitle()	Returns True if the string follows the rules of a title
            isupper()	Returns True if all characters in the string are upper case
            join()	Joins the elements of an iterable to the end of the string
            ljust()	Returns a left justified version of the string
            lower()	Converts a string into lower case
            lstrip()	Returns a left trim version of the string
            maketrans()	Returns a translation table to be used in translations
            partition()	Returns a tuple where the string is parted into three parts
            replace()	Returns a string where a specified value is replaced with a specified value
            rfind()	Searches the string for a specified value and returns the last position of where it was found
            rindex()	Searches the string for a specified value and returns the last position of where it was found
            rjust()	Returns a right justified version of the string
            rpartition()	Returns a tuple where the string is parted into three parts
            rsplit()	Splits the string at the specified separator, and returns a list
            rstrip()	Returns a right trim version of the string
            split()	Splits the string at the specified separator, and returns a list
            splitlines()	Splits the string at line breaks and returns a list
            startswith()	Returns true if the string starts with the specified value
            strip()	Returns a trimmed version of the string
            swapcase()	Swaps cases, lower case becomes upper case and vice versa
            title()	Converts the first character of each word to upper case
            translate()	Returns a translated string
            upper()	Converts a string into upper case
            zfill()	Fills the string with a specified number of 0 values at the beginning
    6.bytes
    7.bytearray
    8.range
    9.list
        defining list
            1. list = []
            2. list=[10,20,30,40]
            3. With dynamic input: (eval)
            4. With list() function:
        Accessing
            Indexing
            Slicing
        Traversing
            using for loop
        List vs immutability:
        cloning
            Difference between = operator and copy() function
        Operators for list
            1. Concatenation operator(+):
            2. Repetition Operator(*):
            3. Comparison
                ==,!=
                <,<=,>,>=
            4. in , not in Membership
        Nested list
            Nested List as Matrix:
        Comprehensions
        Methods
            append()	Adds an element at the end of the list
            clear()	Removes all the elements from the list
            copy()	Returns a copy of the list
            count()	Returns the number of elements with the specified value
            extend()	Add the elements of a list (or any iterable), to the end of the current list
            index()	Returns the index of the first element with the specified value
            insert()	Adds an element at the specified position
            pop()	Removes the element at the specified position
            remove()	Removes the first item with the specified value
            reverse()	Reverses the order of the list
            sort()	Sorts the list
    10.tuple
        Defining tuple
            1. t=()
            2. t=(10,)
            3. t=10,20,30
            4. tuple()
        Accessing
            Indexing
            Slicing
        Traversing
            using for loop
        Tuple vs immutability:
        Operators for tuple
            1. Concatenation operator(+):
            2. Repetition Operator(*):
            3. in , not in Membership
        Tuple Packing and Unpacking:
        Tuple comprehension
        Methods
            count()	Returns the number of times a specified value occurs in a tuple
            index()	Searches the tuple for a specified value and returns the position of where it was found

    11.set
        Defining set
            1. using set()
        Set vs immutability:
        Operations on set:
            Union
            Intersection
            Difference
            Symmetric difference
        Operators for set
            Membership operators: (in , not in)
        Set comprehension
        Methods
            add()	Adds an element to the set
            clear()	Removes all the elements from the set
            copy()	Returns a copy of the set
            difference()	Returns a set containing the difference between two or more sets
            difference_update()	Removes the items in this set that are also included in another, specified set
            discard()	Remove the specified item
            intersection()	Returns a set, that is the intersection of two other sets
            intersection_update()	Removes the items in this set that are not present in other, specified set(s)
            isdisjoint()	Returns whether two sets have a intersection or not
            issubset()	Returns whether another set contains this set or not
            issuperset()	Returns whether this set contains another set or not
            pop()	Removes an element from the set
            remove()	Removes the specified element
            symmetric_difference()	Returns a set with the symmetric differences of two sets
            symmetric_difference_update()	inserts the symmetric differences from this set and another
            union()	Return a set containing the union of sets
            update()	Update the set with the union of this set and others
    12.frozenset
    13.dict
        Defining dicts
            1. d = {}
            2. d = dict()
        Accessing
        Operations on dicts
            Updating dicts
            deleting elements
        dict comprehensions
        Methods
            clear()	Removes all the elements from the dictionary
            copy()	Returns a copy of the dictionary
            fromkeys()	Returns a dictionary with the specified keys and values
            get()	Returns the value of the specified key
            items()	Returns a list containing a tuple for each key value pair
            keys()	Returns a list containing the dictionary's keys
            pop()	Removes the element with the specified key
            popitem()	Removes the last inserted key-value pair
            setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
            update()	Updates the dictionary with the specified key-value pairs
            values()	Returns a list of all the values in the dictionary
    14.None

Type Casting
    1. int()
    2. float()
    3. complex()
    4. bool()
    5. str()
    6. list()
    7. tuple()

Mutability & Immutability
Constants
Operators
    1. Arithmetic Operators
        + ==>Addition
        - ==>Subtraction
        * ==>Multiplication
        / ==>Division operator
        % ===>Modulo operator
        // ==>Floor Division operator
        ** ==>Exponent operator or power operator
    2. Relational Operators or Comparison Operators
        >,>=,<,<=
    3. Equality operators
        == , !=
        Chaining
    4. Logical operators
        and, or ,not
        Boolean types behaviour
        Non boolean types behaviour
    5. Bitwise oeprators
        &,|,^,~,<<,>>
    6. Assignment operators
        Augmented Assignments
    7. Ternary operators
    6. Special operators
        1. Identity Operators
            1. is
            2. is not
        2. Membership operators
            1. in
            2. not in
    Operator precedence

Input and output statements
    1. raw_input()
    2. input()
    3. print()
        Formatted string
            %i====>int
            %d====>int
            %f=====>float
            %s======>String type
            print with {} operator

Command line arguments
Flow controls
    1. Conditionals
        1. if
        2. if-elif
        3. if-elif-else
    2. Iterative
        1. for-else
        2. while-else
    3. Transfer
        1. continue
        2. break
        3. pass
Difference between del and None:

Functions:
    Types:
        1. Built in Functions
            Math
                abs()	Returns absolute value of a number
                divmod()	Returns quotient and remainder of integer division
                max()	Returns the largest of the given arguments or items in an iterable
                min()	Returns the smallest of the given arguments or items in an iterable
                pow()	Raises a number to a power
                round()	Rounds a floating-point value
                sum()	Sums the items of an iterable

            Type Conversion
                ascii()	Returns a string containing a printable representation of an object
                bin()	Converts an integer to a binary string
                bool()	Converts an argument to a Boolean value
                chr()	Returns string representation of character given by integer argument
                complex()	Returns a complex number constructed from arguments
                float()	Returns a floating-point object constructed from a number or string
                hex()	Converts an integer to a hexadecimal string
                int()	Returns an integer object constructed from a number or string
                oct()	Converts an integer to an octal string
                ord()	Returns integer representation of a character
                repr()	Returns a string containing a printable representation of an object
                str()	Returns a string version of an object
                type()	Returns the type of an object or creates a new type object

            Iterables and Iterators
                all()	Returns True if all elements of an iterable are true
                any()	Returns True if any elements of an iterable are true
                enumerate()	Returns a list of tuples containing indices and values from an iterable
                filter()	Filters elements from an iterable
                iter()	Returns an iterator object
                len()	Returns the length of an object
                map()	Applies a function to every item of an iterable
                next()	Retrieves the next item from an iterator
                range()	Generates a range of integer values
                reversed()	Returns a reverse iterator
                slice()	Returns a slice object
                sorted()	Returns a sorted list from an iterable
                zip()	Creates an iterator that aggregates elements from iterables

            Composite Data Type
                bytearray()	Creates and returns an object of the bytearray class
                bytes()	Creates and returns a bytes object (similar to bytearray, but immutable)
                dict()	Creates a dict object
                frozenset()	Creates a frozenset object
                list()	Constructs a list object
                object()	Returns a new featureless object
                set()	Creates a set object
                tuple()	Creates a tuple object

            Classes, Attributes, and Inheritance
                classmethod()	Returns a class method for a function
                delattr()	Deletes an attribute from an object
                getattr()	Returns the value of a named attribute of an object
                hasattr()	Returns True if an object has a given attribute
                isinstance()	Determines whether an object is an instance of a given class
                issubclass()	Determines whether a class is a subclass of a given class
                property()	Returns a property value of a class
                setattr()	Sets the value of a named attribute of an object
                super()	Returns a proxy object that delegates method calls to a parent or sibling class

            Input/Output
                format()	Converts a value to a formatted representation
                input()	Reads input from the console
                open()	Opens a file and returns a file object
                print()	Prints to a text stream or the console
                Variables, References, and Scope
                Function	Description
                dir()	Returns a list of names in current local scope or a list of object attributes
                globals()	Returns a dictionary representing the current global symbol table
                id()	Returns the identity of an object
                locals()	Updates and returns a dictionary representing current local symbol table
                vars()	Returns __dict__ attribute for a module, class, or object

            Miscellaneous
                callable()	Returns True if object appears callable
                compile()	Compiles source into a code or AST object
                eval()	Evaluates a Python expression
                exec()	Implements dynamic execution of Python code
                hash()	Returns the hash value of an object
                help()	Invokes the built-in help system
                memoryview()	Returns a memory view object
                staticmethod()	Returns a static method for a function
                __import__()	Invoked by the import statement
            Magic fuctions
        2. User Defined Functions
"""