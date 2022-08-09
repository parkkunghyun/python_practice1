# 3.3이후부터는 __init__이 없어도 패키지로간주해주긴함!
__all__ = ["character", "object_type"]
from . import object_type
from . import character