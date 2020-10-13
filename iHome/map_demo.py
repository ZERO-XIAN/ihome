print("--------一般函数--------")

def add1(num1, num2):
    return num1 + num2
print(add1(3, 7))


print("\n--------匿名函数lambda--------")

add2 = lambda x, y: x + y
print(add2(3, 7))


li1 = [1,2,3,4]
li2 = [2,3,4,5]
li3 = [9, 12, 18, 24, 27]


print("\n--------map(function, iterable, ...)--------")
print(list(map(add1, li1, li2)))
# print(list(map(add2, li1, li2)))
print(list(map(lambda x, y: x + y, li1, li2)))



print("\n--------filter(function, iterable)--------")
print(list(filter(lambda x: x % 3 == 0, li3)))


print("\n--------reduce(function, iterable[, initializer])--------")
from functools import reduce
print(reduce(add1, li1))
# print(reduce(add2, li1))
print(reduce(lambda x, y: x + y, li1))



print("\n--------列表推导式for..in..if--------")
print(list(x+y for x,y in list(zip(li1,li2))))
print(list(x for x in li3 if x%3 == 0))


print("\n--------三目运算符--------")
a1 = 9
a2 = 11
b1 = 5 if a1 < 10 else 50
b2 = 5 if a2 < 10 else 50
print(b1, b2)