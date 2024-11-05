"""module"""
import math

class Point2D(object):
    """
    Représente un point dans un plan cartésien

    >>> p1 = Point2D(3, 4)
    >>> p1.x
    3
    >>> p1.y
    4
    >>> print(p1)
    Point2D(3,4)
    >>> p2 = Point2D()
    >>> p2.x
    0
    >>> p2.y
    0
    >>> print(p2)
    Point2D(0,0)
    >>> p1.move(1,1)
    >>> p1.x
    4
    >>> p1.y
    5
    >>> print(p1)
    Point2D(4,5)
    >>> p1.distance(p2)
    6.4031242374328485
    """


    def __init__(self, x=0, y=0):
        """Constructeur du point"""
        self.x = x
        self.y = y

    def move(self, dx, dy) -> None:
        """Déplace le point"""
        self.x += dx
        self.y += dy

    def distance(self, other):
        """Calcule la distance entre les points"""
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        """Texte"""
        return f"({self.x}, {self.y})"


def main():
    p1 = Point2D(2, 3)
    p2 = Point2D(5, 1)

    print(p1)  # Affiche (2, 3)
    p1.move(1, -2)
    print(p1)  # Affiche (3, 1)
    print(p1.distance(p2))  # Affiche la distance entre p1 et p2


if __name__ == "__main__":
    main()
