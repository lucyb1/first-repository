### Bash Stuff - Aliases

`set` - core thing of bash, gives you all currently set variables

`alias new_command_name='command_to_execute'`

this will only work in current bash - closing and reopening/opening a new one - message lost

solution: use command `source *something*` for example `source .bash_aliases` or `. .bash_aliases` -> define your aliases in a file that gets sourced

every linux has 8 standard terminals `ctrl+alt+f*` in X server (desktop environment)

not all dot files (*.something*) loads (=are sourced) in all environments

`ctrl+d` - EOF

### Recursion
= function calls itself

```python
def fib(n):
    if not isinstance(n, (int, long)):
        raise ValueError('argument must be integer')
    if n <= 0:
        raise IndexError('cannot use negative index')
    if 1 == n or 2 == n:
        return 1
    return fib(n-1) + fib(n-2)
```

`assert <condition>[, custom error message]`:
- use four debugging of your own code
- use when you want to be 100% sure of something
- while compiling the code for production, the compiler (mostly) erases them

list comprehention

```python
print [
    fib(x)
    for x in range(1, 12)
    if x
]
```

try-catch block

```python
try:
    print fib(-5)
except IndexError:
    print 'FML, OMG, Error ...'
finally:
    print 'blabla'
```

### Shebang Line

- the first line of unix script
- determines the script interpreter
- its format: `#!full_interpreter_path`

`/user/bin/env python` - opens python environment (so you don't have to know where exactly the python is)
