# Build a custom immutable class.
class ImmutablePoint:
    __slots__ = ("_x", "_y")  # prevent dynamic attribute creation

    def __init__(self, x, y):
        super().__setattr__("_x", x)
        super().__setattr__("_y", y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __setattr__(self, key, value):
        raise AttributeError(f"{self.__class__.__name__} is immutable")

    def __repr__(self):
        return f"ImmutablePoint(x={self._x}, y={self._y})"
    
p = ImmutablePoint(10, 20)
print(p)         # ImmutablePoint(x=10, y=20)
print(p.x, p.y)  # 10 20

# Attempt to modify attribute
try:
    p.x = 100
except AttributeError as e:
    print(e)  # ImmutablePoint is immutable





