##GCD calculator
def gcd_calc(a, b):
    i = 0
    a = abs(a)
    b = abs(b)
    while(b != 0):
        a , b = b, a%b
        i = 1+ i
    return a, i

gcd, num = gcd_calc(20, 25)
print(gcd, num )
gcd, num = gcd_calc(-89, -98)
print(gcd, num )
gcd, num = gcd_calc(54321, 50)
print(gcd, num )
    