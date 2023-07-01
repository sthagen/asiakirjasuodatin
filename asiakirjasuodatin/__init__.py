"""Document filter (Finnish: asiakirjasuodatin) that read a JSON serialization of the Pandoc AST from stdin, transform it in some way, and write it to stdout."""
import pathlib

# [[[fill git_describe()]]]
__version__ = '2023.6.24+parent.ca064f8f'
# [[[end]]] (checksum: 1ddc9981f2f3804884391b42c2f12878)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

APP_ALIAS = str(pathlib.Path(__file__).parent.name)
APP_ENV = APP_ALIAS.upper()
APP_NAME = locals()['__doc__']

VERSION = __version__
VERSION_INFO = __version_info__

__all__ = [
    'APP_ALIAS',
    'APP_ENV',
    'APP_NAME',
    'VERSION',
    'VERSION_INFO',
]
