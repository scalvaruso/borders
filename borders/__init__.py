# =============================================================================
# Borders Python Library
# Copyright (c) 2025 Simone Calvaruso
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

__all__ = ["frame"]

from .borders import *
import platform

# Fixing compatibility errors for colorama

if platform.system() == "Windows":
    import colorama
    colorama.just_fix_windows_console()
else:
    pass
