from math import atan
from math import degrees

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    print(f'{int(round(degrees(atan(ab/bc))))}°')