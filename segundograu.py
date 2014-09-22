from math import sqrt

def baskara(a,b,c):
    delta = ((b**2)-4*a*c)
    if a == 0:
        return 'a nao pode ser 0'
    if delta < 0:
        return 'raiz irreal'
    if delta == 0:
        x1 = (-b+(sqrt(delta)))/2*a
        return x1
    if delta > 0:
        x1 = (-b+(sqrt(delta)))/2*a
        x2 = (-b-(sqrt(delta)))/2*a
        return x1,x2
