import math

def ComplexNumber(a,b):
    a = float(a)
    b = float(b)
    if(a == 0 and b >= 0):
        print('%si' %(b))
    elif(a == 0 and b < 0):
        print('%si' %(b))
    elif(a > 0 and b < 0):
        print('%s%si' %(a,b))
    elif(a < 0 and b < 0):
        print('%s%si' % (a, b))
    else:
        print('%s+%si' % (a, b))

def modol_liczby(a,b):
    a = float(a)
    b = float(b)
    return math.sqrt(a*a + b*b)

def argument(a,b):
    a = float(a)
    b = float(b)
    if a > 0:
        return math.atan(a/b)
    elif(a < 0 and b >= 0):
        return math.atan(a/b) + math.pi
    elif(a < 0 and b < 0 ):
        return math.atan(a/b) - math.pi
    elif(a == 0 and b > 0):
        return math.pi/2
    elif(a ==0 and b < 0 ):
        print('-%s'%(math.pi/2))
    else:
        print("Tego nie wie nikt. Pozostawiamy do samointrpreatcji")

