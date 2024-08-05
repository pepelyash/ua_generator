"""
Random User-Agent
Copyright: 2022-2024 Ekin Karadeniz (github.com/iamdual)
License: Apache License 2.0 
"""
import random
from typing import List

from ..version import Version, WindowsVersion

# https://learn.microsoft.com/en-us/windows/win32/sysinfo/operating-system-version
# https://learn.microsoft.com/en-us/microsoft-edge/web-platform/how-to-detect-win11
versions: List[WindowsVersion] = [
    WindowsVersion(version=Version(major=6, minor=1), ch_platform=Version(major=0)),
    WindowsVersion(version=Version(major=6, minor=2), ch_platform=Version(major=0)),
    WindowsVersion(version=Version(major=6, minor=3), ch_platform=Version(major=0)),
    WindowsVersion(version=Version(major=10, minor=0), ch_platform=Version(major=(1, 10))),
    WindowsVersion(version=Version(major=10, minor=0), ch_platform=Version(major=13)),
]

# https://gs.statcounter.com/os-version-market-share/windows/desktop/worldwide
version_weights = [1.0] * len(versions)
version_weights[-1] = 7.0
version_weights[-2] = 10.0


def get_version() -> WindowsVersion:
    choice: List[WindowsVersion] = random.choices(versions, weights=version_weights, k=1)
    return choice[0]
