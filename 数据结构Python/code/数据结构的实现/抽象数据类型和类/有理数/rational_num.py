"""
有理数类
"""
class Rational(object):
    """
    在建立有理数时，应该考虑约去分子和分母的最大公约数。因此需要定义一个求最大公约数的函数gcd。
    这里出现了一个问题，应该在哪里定义这个函数？
    分析：
    1、gcd参数应该是两个整数，它们不属于被定义的有理数类型。
    2、gcd的计算并不依赖任何有理数类的对象。
    因此：
    1、其参数表中不应该以表示有理数的self作为第一个参数。
    2、gcd是为有理数类的实现而需要使用的一种辅助功能。
    所以，gcd应该是有理数类里定义的一个非实例方法。即静态方法，在函数定义前面加@classmethod.
    本质上说，静态方法就是类里面定义的普通函数，但也是该类的局部函数

    """
    @staticmethod
    def _gcd(m, n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n % m, m
        return n

    def __init__(self, num, den = 1):
        # 判断分子分母是否为int
        if not isinstance(num, int) or not isinstance(den, int):
            raise TabError
        # 判断分母是否为0
        if den == 0:
            raise ZeroDivisionError
        """
        约定负有理数的负号在分子上，下面的过程就像：
        sign = 1,分数=-3/5,或（-3）/5
        step1:sign = -1,分子-3变成分子为3
        如果是3/(-5)：
        sign = -1,分母变为5
        
        step2:最终的分子=sign*分子=-1*3，分母=5
        """
        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational._gcd(num, den)
        self._num = sign * (num // g)
        self._den = den // g

    # 获取属性
    def get_num(self):
        return self._num
    def get_den(self):
        return self._den

    """
    定义有理数的一些计算
    """
    # 加法
    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        den = self._den * other.get_den()
        num = self._num * other.get_den() + self._den * other.get_num()
        return Rational(num, den)

    # 减法
    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        den = self._den * other.get_den()
        num = self._num * other.get_den() - self._den * other.get_num()
        return Rational(num, den)

    # 乘法
    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        return Rational(self._num * other.get_num(), self._den * other.get_den())

    # 除法（//整除）
    def __floordiv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        if other.get_num() == 0:
            raise ZeroDivisionError
        return Rational(self._num * other.get_den(), self._den * other.get_num())

    # 除法（不是整除，有小数）
    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError
        if other.get_num() == 0:
            raise ZeroDivisionError
        return Rational(self._num * other.get_den(), self._den * other.get_num())

    # __str__方法用来打印实例，把该类的对象转换到字符串,return后面必须是字符串
    def __str__(self):
        return str(self._num) + '/' + str(self._den)

    def print(self):
        print(self._num, '/', self._den)

def main():
    # 实例化
    five = Rational(2, 3)
    # print(type(five))
    # print(five)
    x = Rational(5, 7)
    # print(x)
    result1 = five.__add__(x)               #返回一个类的对象，也是一个分数。
    print(result1)
    result2 = five.__truediv__(x)
    print(result2)
    result3 = five.__sub__(x)
    print(result3)

if __name__ == '__main__':
    main()
