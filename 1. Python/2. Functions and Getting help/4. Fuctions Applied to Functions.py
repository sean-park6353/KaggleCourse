
# ? Here's something that's powerful, though it can feel very abstract at first.
# ? You can supply functions as arguments to other functions.
# ? Some example may make this clearer:


def mult_by_five(x):
    return 5 * x


def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))


print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n',  # '\n' is the newline character - it starts a new line
)


def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5


print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
