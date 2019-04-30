"""
1.2 如何使用特殊方法
    特殊方法的存在是为了被解释器调用的，在调用的时候，如__len__是一个特殊方法，但是没有my_object.__len__()这种调用方法，
而是使用len（my_object）这种调用方法。
"""

"""
1.2.1 模拟数值类型
例1.2 一个简单的二维向量
"""

from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # 定义输出格式
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        # hypot(): 返回欧几里德范数 sqrt(x*x + y*y)
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)

# 向量相加
print(v1 + v2)

v = Vector(3, 4)
# 取向量的模
print(abs(v))
# 向量的标量乘法，不可写成 3 * v
print(v * 3)

"""
1.2.2 字符串的表示形式
    例1.2中，内置函数repr，能把一个对象用字符串的形式表达出来，使得对象更加友好，这就是字符串表现形式。
    
    __repr__和__str__的区别：后者是在str(）函数被调用，或是在用print函数打印一个对象的时候才被调用的，
    并且它返回的字符串对终端用户更友好。
    
    首选使用__repr__,如果对象中没有__str__，而python又需要调用它，解释器会__repr__用替代。
"""

"""
1.2.3 算术运算符
    例1.2中，__add__和__mul__分别带来了+和*两个算术运算符，而且两个方法返回的是一个新创建的向量对象，而
    最初的两个被操作的向量则不变，只是读取了他们的值。即：中缀运算符的原则就是不改变操作对象，而是产出一个
    新值。
"""

"""
1.2.4 自定义的布尔值
    例1.2 中，对自定义的bool类型实现比较简单，如果向量的模是0，则返回alse,其他情况则返回True，__boll__
    函数的返回类型应该是布尔型，所以通过bool(abs(self))把模值变成了布尔值。
    也可写为：
        def __bool__(self):
            return bool(self.x or self.y)
    这样程序不易读，但是更高效。
"""

"""
1.3 ———— 1.6
    略
"""