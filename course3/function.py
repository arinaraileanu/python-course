def function():
    print("first function")
def a():
    print("Ex1")

def b():
    print("Ex2")

def c():
    a()
    b()

def sum(param1, param2):
    '''
    :param param1: first number
    :param param2: second number
    :return: sum of numbers
    '''
    print("Sum of numbers is {}".format(param1 + param2))
    return param1 + param2

def paramOrder(age, name, color="red"):
    print("Hi {}, you're {} years old. Your color is: {}".format(name, age, color))

def asteriskSum(p1, p2, *p3):
    # at least 2 params
    x = p1 + p2
    if p3:
        print("c = {}".format(x))
        for e in p3:
            x += e
    return x

def f(b, **a):
    print("a is equal to {}".format(a))
    print("b is equal to {}".format(b))

multipleList = [x**2 for x in range(2, 15, 1) if not x % 2]

function()
c()
# 1 and 2 are attributes, param1 and param2 are parameters
sum(1, 2)
x = sum(3, 5)
print(x)
paramOrder(name="John", age=21)
paramOrder(name="John", age=21, color="blue")
asteriskSum(1, 2, 3, 4)
print(asteriskSum(1, 2, 3, 4, 5))
f("Parameter b", one = 1, two = 2)
print(multipleList)