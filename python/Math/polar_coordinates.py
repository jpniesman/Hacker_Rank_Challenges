# Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
# A complex number z = x + yj
# is completely determined by its real part x and imaginary part y.Here, j is the imaginary unit.

import cmath


if __name__ == '__main__':
    z = complex(input())
    print(abs(z))
    print(cmath.phase(z))