"""Test tailrecursion.py."""
from tailrecursion import Recursion
from tailrecursion import tail_recursive


@tail_recursive
def fib(seq_num: int, _i: int = 0, _j: int = 1) -> int:
    """Return the nth Fibonacci number."""
    if seq_num == 0:
        return _i
    else:
        raise Recursion(seq_num - 1, _i=_j, _j=(_i + _j))


def test_correctness():
    """Test we get the correct result."""
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(5) == 5
    assert fib(100) == 354224848179261915075


def test_function_meta():
    """Test we don't destroy the function by decorating it."""
    @tail_recursive
    def my_fn():
        """TEST."""
        pass

    assert my_fn.__doc__ == 'TEST.'
