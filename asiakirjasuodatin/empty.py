"""Empty or No op filter."""
from pandocfilters import toJSONFilter  # type: ignore


def noop(key, value, format, meta):  # type: ignore
    """Do nothing."""
    return None


if __name__ == '__main__':
    toJSONFilter(noop)
