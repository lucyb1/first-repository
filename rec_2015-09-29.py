#!/usr/bin/env python

def fib(n):
    if not isinstance(n, (int, long)):
        raise ValueError('argument must be integer')
    if n <= 0:
        raise IndexError('cannot use negative index')
    if 1 == n or 2 == n:
        return 1
    return fib(n-1) + fib(n-2)

# list comprehention
# R.P.: "It's pure f***ing magic!"
print [
    fib(x)
    for x in range(1, 12)
    if x
]
# 3 parts:
# 1. result
# 2. for ... (generator)
# 3. if ... (condition)

print fib(1)

# this is a multiline string
# (or a way how to comment code block)
"""
# try-catch block
try:
    print fib(-5)
except IndexError:
    print 'FML, OMG, Error ...'
finally:
    print 'blabla'
"""
