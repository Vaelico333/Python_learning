# Question: Please write a function that calculates liquid volume in a sphere using the following formula. The radius r is always 10, so consider making it a default parameter.

from math import pi
def volume(h, r = 10):
    vol = ((4 * pi * r**3) /3) - ((pi * (2*r-h)**2 * (3 * r-(2*r-h))) /3)
    return vol
def main():
    l = float(input('Introduce the liquid height: '))
    sp = input('Introduce the sphere radius: ')
    r = 10 if sp == '' else float(sp)
    print(volume(l, r))
main()