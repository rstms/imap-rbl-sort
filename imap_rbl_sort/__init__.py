"""Top-level package for imap-rbl-sort."""

from .cli import cli
from .version import __version__, __timestamp__, __author__, __email__

__all__ = ["cli", __version__, __timestamp__, __author__, __email__]
