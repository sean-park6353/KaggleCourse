
#! Defining Functions
# ? Builtin functions are great,
# ? but we can only get so far with them
# ? before we need to start defining our own functions.
# ? Below is a simple example.


def least_difference(a, b, c):
    '''
    return the smalles difference between any two numbers among
    a,b, and c
    '''
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1, diff2, diff3)


print(least_difference(10, 2, 5))
print(help(least_difference))
