__all__ = ["frame"]

from .borders import *
import platform

# Fixing compatibility errors for colorama

if platform.system() == "Windows":
    import colorama
    colorama.just_fix_windows_console()
else:
    pass
