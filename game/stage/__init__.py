# 3.3이후부터는 __init__이 없어도 패키지로간주해주긴함!
__all__ = ["main", "sub"]
from . import mmain
from . import sub