"""Lightweight helper for creating tail-recursive functions."""

__all__ = (
    'Recursion',
    'tail_recursive',
)

from functools import wraps
from typing import cast
from typing import Callable
from typing import Dict
from typing import Generic
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union


VT = TypeVar('VT')
KT = TypeVar('KT')
RT = TypeVar('RT')
TailRecFunction = Callable[..., RT]  # noqa, pylint: disable=invalid-name


class NotSet(type):
    """Like None, but we know it's not provided by the user."""

    pass


class Recursion(BaseException, Generic[VT, KT]):
    """Indicate a recursive call to the function from which this was raised."""

    def __init__(self, *args: VT, **kwargs: KT) -> None:
        """Set the values used for the recursive call."""
        super().__init__()
        self.args = args
        self.kwargs = kwargs


def virtual_recurse(func: TailRecFunction, *args: VT, **kwargs: KT) -> RT:
    """Call a function with its raised Recursion args until it returns."""
    result: Union[Type[NotSet], RT] = NotSet
    while result is NotSet:
        try:
            result = func(*args, **kwargs)
        except Recursion as next_call:
            args = cast(Tuple[VT, ...], next_call.args)
            kwargs = cast(Dict[str, KT], next_call.kwargs)

    return cast(RT, result)


def tail_recursive(func: TailRecFunction) -> TailRecFunction:
    """Decorate a function as tail recursive, permitting `raise Recursion`."""
    @wraps(func)
    def _trampolined(*args, **kwargs):
        return virtual_recurse(func, *args, **kwargs)

    return _trampolined
