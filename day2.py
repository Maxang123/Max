
#Day 2

#raise ZeroDivisionError
"""
year = int(input())#2012
#assert year <= 2023
if year < 1900 or year > 2023:
    raise ValueError("อายุเกิ้นนน")
print(2023 - year)
"""

#Function

#1  in 1 out
"""
def square(x):
    result = x**2
    return result
n = int(input())
squarre_of_n = square(n)
print(squarre_of_n)

def power(x,y):
    result = x**y
    return result
print(power(3,5))


def introduce():
    print("Hi my name is Max")
    return 'Hi'
#1 in many out
def find_square_and_sqrt(x):
    sqrt_of_x = x **(0.5)
    sqare_of_x2 = x**2
    return sqare_of_x2,sqrt_of_x
print(find_square_and_sqrt(9))
#1 in 0 out
def send_help(name):
    print(f"กำลงะส่งความช่วยเหลือ{name.upper()}")
    #return none
result = send_help("Max")
print(result)
#global scope,local scope
#def f():#global
 #   print (a)#global
"""
a=5
def g():
    a=3 #local
    print(a) #local
g()
print(a)
def h():
    global a #เปลี่ยน a local เป็น global
    a += 3 #local
    print(a) #local
h()

