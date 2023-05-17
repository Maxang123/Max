x=int(input())
y=int(input())
empty= []
def krn(z,p):
    for fool_number in range(1,1000,1):
        if z % fool_number == 0 and p % fool_number == 0:
            empty.append(fool_number)
    print(empty)
krn(x,y)

"""


def find_lcm(z, p):
    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    gcd = find_gcd(z, p)
    lcm = (z * p) // gcd
    
    return lcm
lcm = find_lcm(z, p)
print(lcm)

"""