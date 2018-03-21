# tailrecursion
[![CircleCI](https://circleci.com/gh/OJFord/python-tailrecursion.svg?style=svg)](https://circleci.com/gh/OJFord/python-tailrecursion)

Lightweight helper for creating tail-recursive functions in Python.

## Why?

Recursion may be faster or more readable than a naïve loop, but Python does not optimise tail-recursive function calls (as many languages do) - so you'll soon fill its stack with all but the smallest of recursions.

This small module uses a pattern known as 'trampolining' to perform this optimisation via exception handling, so you can use the tail-recursive form without filling your stack, and probably much faster than the loop form too - since only a call that returns a base case (typically one, the final call) is actually computed.

## Installation
```
pip install https://github.com/OJFord/python-tailrecursion/archive/{VERSION}.tar.gz
```

## Usage
Decorate the tail-recursive function, and then instead of recursing directly, `raise Recursion` with the arguments to the recursive call:
```python
from tailrecursion import Recursion
from tailrecursion import tail_recursive


@tail_recursive
def print42(msg: str, _n: int = 42) -> None:
    """Print a message 42 times."""
    if _n == 0:
        return

    print(msg)
    raise Recursion(msg, _n=(_n - 1))
```
