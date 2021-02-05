from collections.abc import Mapping
from collections import UserString
from io import IOBase
from os import PathLike

TRUE_STRINGS = {'TRUE', 'YES', 'ON', '1'}
FALSE_STRINGS = {'FALSE', 'NO', 'OFF', '0', 'NONE', ''}


def is_integer(item):
    return isinstance(item, int)


def is_number(item):
    return isinstance(item, (int, float))


def is_bytes(item):
    return isinstance(item, (bytes, bytearray))


def is_string(item):
    return isinstance(item, str)


def is_unicode(item):
    return isinstance(item, str)


def is_pathlike(item):
    return isinstance(item, PathLike)


def is_list_like(item):
    if isinstance(item, (str, bytes, bytearray, UserString, IOBase)):
        return False
    try:
        iter(item)
    except:
        return False
    else:
        return True


def is_dict_like(item):
    return isinstance(item, Mapping)


def type_name(item, capitalize=False):
    if isinstance(item, IOBase):
        name = 'file'
    else:
        cls = item.__class__ if hasattr(item, '__class__') else type(item)
        named_types = {str: 'string', bool: 'boolean', int: 'integer',
                       type(None): 'None', dict: 'dictionary', type: 'class'}
        name = named_types.get(cls, cls.__name__)
    return name.capitalize() if capitalize and name.islower() else name


def is_truthy(item):
    """Returns `True` or `False` depending is the item considered true or not.

    Validation rules:

    - If the value is a string, it is considered false if it is `'FALSE'`,
      `'NO'`, `'OFF'`, `'0'`, `'NONE'` or `''`, case-insensitively.
      Considering `'NONE'` false is new in RF 3.0.3 and considering `'OFF'`
      and `'0'` false is new in RF 3.1.
    - Other strings are considered true.
    - Other values are handled by using the standard `bool()` function.

    Designed to be used also by external test libraries that want to handle
    Boolean values similarly as Robot Framework itself. See also
    :func:`is_falsy`.
    """
    if is_string(item):
        return item.upper() not in FALSE_STRINGS
    return bool(item)


def is_falsy(item):
    """Opposite of :func:`is_truthy`."""
    return not is_truthy(item)
