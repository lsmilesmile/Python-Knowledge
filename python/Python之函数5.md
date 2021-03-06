# 函数

> [TOC]
>
> 



## 1 - 函数的使用	

​	在编写程序的过程中，我们可以将重复使用的代码写在函数中，这样我们就不必重复的copy代码。

### 1.1 声明函数

- **函数的声明一般形式**

  **def <函数名>(参数列表):**

  ​    **<函数语句>**

  ​    **return <返回值>**

  **注：参数列表和返回值是可选的，如果函数有返回值，则要用return语句返回结果，return语句后面也可以不跟返回值。也可以不写return**

- **代码示例：**

  ```python
  #无返回值、无参数函数
  def test1():
      print('这是一个无返回值和参数的函数')
      
  #有参数、返回值的函数
  def test2(aList):
      sum = 0
      for i in aList:
          sum += i
      return sum
  ```

### 1.2 函数调用

​	函数调用这件事其实我们已经做过很多次，当我们用print()函数向屏幕输出内容时就已经调用了函数，只不过我们调用的是Python的内建函数，我们调用自定义函数和调用内建函数基本相同，只不过在调用自定义函数前必须声明函数。调用方式就是函数后面加圆括号，如果有参数需要传入参数。

代码示例：

```Python
def test():
    print('我是要被调用的函数')
#函数调用    
test()
```



## 2 - 函数参数

​	函数参数的形式有多种，数量也可以有少有多。

### 2.1 默认值参数

- **语法形式**

  def <函数名>(…, 形参名=默认值):
      <代码块>

- 注：

  1. 在调用含有默认值参数的函数时，可以不用为设置了默认值的形参进行传值，此时函数将会直接使用函数定义时设置的默认值，也可以通过显式赋值来替换其默认值；
  2. 可以用函数名.\_\_defaults\_\_随时查看所有默认值参数的当前值；
  3. 默认值参数必须出现在函数形参列表的最右端。

- **代码示例：**

  ```Python
  def test(params='我是默认参数'):
      print(params)
  #不传参调用
  test()
  test('我是传递过来的参数')
  print(test.__defaults__)
  """
  结果
  我是默认参数
  我是传递过来的参数
  ('我是默认参数',)
  """
  ```

如果一个函数有许多参数，但是我只想传递其中的几个，那么是怎么传递的呢？

代码示例：

```Python
def test(name, age, sex='男', address='成都'):
    print('%s, %d, %s, %s' % (name, age, sex, address))

test('felix', 21, '南京')
test('felix', 21, '南京', '女')
```

从上面可以看到，如果给默认值参数传递的参数数量小于默认值参数的数量，那么将按照顺序传递参数，即位置参数。注意，不是默认值的参数的的参数，在传递参数时，一个参数都不能少，即，有几个就传几个。

### 2.2 关键字参数

​	在上面我们知道了，Python的参数传递是按照参数的位置顺序进行传递的，即位置参数，调用时提供的第一个参数会被声明时的参数列表中的第一个参数获取。而Python中还提供了另一种参数传递的方法，**即按照参数名传递**，也叫作关键字参数。

代码示例：

```Python
def test(name, age, sex='男', address='成都'):
    print('%s, %d, %s, %s' % (name, age, sex, address))

test('felix', 21, address='南京')
test('felix', 21, address='南京', sex='女')
```

从上面的代码可以看到，在第一次调用时，即使只给默认值参数传递一个值，但是这时候不是按照顺序传递给sex参数了，还是传递给sex后面的address参数，第二次调用也是，虽然给默认值参数提供的参数数量和声明时的参数一样多，但是由于用了参数名进行传递，这时就把相应的参数传递给对应与参数名的参数。

### 2.3 可变数量参数\*params,\*\*params

- ***params**

		在自定义函数时，在参数名前加上一个星号“*”，则表示该参数就是一个可变长参数。在函数调用时，如果依次将所有的其他变量都赋予值之后，剩下的参数将会放在一个元祖中。

代码示例：

```Python
def test1(*params):
    print(params)
    print(type(params))
    print(sum(params))

def test2(name, *params, address='成都'):
    print(name, params, address)

#把传进去的参数放在元祖里
test1(1, 2, 3)

#如果星号'*'后面的参数不指名关键字参数，那么第一个参数后面的所有参数都会被认为是params
test2('felix', 1, 2, 3, 'hello')

#指明了'hello'的关键字是address，这时候'hello'就不会被包含在params中
test2('felix', 1, 2, 3, address='hello')

"""
结果
(1, 2, 3)
<class 'tuple'>
6
felix (1, 2, 3, 'hello') 成都
felix (1, 2, 3) hello
"""
```

- **\*\*params**

  上面用元祖保存变长参数，这是提供的参数不能是关键字参数。如果要传递变长的关键字参数，可以在参数前加两个星星**valuename，这样，多余的关键字参数就会被包含在valuename中。

  **注：若果收集关键字参数，那么所有的关键字参数都要放在参数列表之后，就和默认参数相似。**

  示例代码：

  ```Python
  def test1(a, b, c=0, **params):
      print(params, a, b, c)
      print(type(params))
      print(sum([value for value in params.values()]))
  
  test1(1, 3, j=2, k=9, h=6)
  """
  {'j': 2, 'k': 9, 'h': 6} 1 3 0
  <class 'dict'>
  17
  """
  
  def cube(name, **nature):
      all_nature = {'x':1,
                    'y':1,
                    'z':1,
                    'color':'white',
                    'weight':1}
      all_nature.update(nature)
      print(name, "立方体的属性：")
      print('体积：', all_nature['x'] * all_nature['y'] * all_nature['z'])
      print('颜色：', all_nature['color'])
      print('重量：', all_nature['weight'])
  
  cube('first')
  cube('second', y=3, color = 'red')
  cube('third', z=2, color='green', weight=10)
  
  """
  结果
  first 立方体的属性：
  体积： 1
  颜色： white
  重量： 1
  second 立方体的属性：
  体积： 3
  颜色： red
  重量： 1
  third 立方体的属性：
  体积： 2
  颜色： green
  重量： 10
  """
  ```


### 2.4 序列解包

- 拆解元祖 - 提供位置参数
- 拆解字典 - 提供关键字参数

调用时使用拆解元祖的方法是在调用时提供的参数前加上一个\*号；拆解字典的方法是在调用时提供的参数前加上两个个\*号；

代码示例：

```Python
def test(a, b):
    return a + b

print('元祖：', test(*(1, 2)))
print('字典：', test(**{'a':1, 'b':2}))
print('列表：', test(*[1, 2]))
```

### 2.5 函数调用时参数的传递方式

​	Python中的元素有可变和不可变之分你，如整数、浮点数、字符串、元祖等都属于不可变的；而列表呵呵字典都属于可变的。前面介绍过，“=”号的作用是将对象的引用与内存中某对象进行绑定，所以如果要改变一个指向整数的变量的值，那就直接在内存中创建一个新的整数值，然后将变量引用与其绑定。

代码示例：

```Python

```

**小陷阱**

代码示例：

```Python
def fun(lst=[]):
    lst.append('adc')
    print(lst)

for i in range(1, 4):
    print('第%d次调用fun：' % i);fun()
  
"""
结果
第1次调用fun：
['adc']
第2次调用fun：
['adc', 'adc']
第3次调用fun：
['adc', 'adc', 'adc']
"""
```

按照默认值参数的传递方式，每次调用函数fun()时并不是传递的空列表，而是传递的上次修改过的列表，如果要实现每次传入空列表，可以这样：

```Python
def fun(lst=None):
    lst = [] if lst is None else lst
    lst.append('adc')
    print(lst)
    print('-'*10)
    
    
for i in range(1, 4):
    print('第%d次调用fun：' % i);fun()
   
"""
结果
第1次调用fun：
None
['adc']
----------
第2次调用fun：
None
['adc']
----------
第3次调用fun：
None
['adc']
----------
"""
```

## 3 变量的作用域

### 3.1 Python中的作用域：

- 内置作用域 - Python预先定义的；
- 全局作用域 - 所编写的整个程序；
- 局部作用域 - 某个函数内部范围。

每次执行函数都会创建一个新的命名空间，这个新的命名空间就是局部作用域，同一个函数不同的运行时间，其作用域是独立的，不同的函数也可以具有相同的参数名，其作用域也是独立的。在函数内部已经声明的变量名，在函数意外依然可以使用。并且在函数运行过程中期值并不互相影响。

代码示例：

```Python
def test():
    a = 1
    print(a+1)

a = 'name'

print('全局a：', a)
test()
print('全局a：', a)
"""
结果
全局a： name
2
全局a： name
"""
```

#### 3.1.2 global关键字

global - 在函数中引用全局变量并进行操作。

代码示例：

```Python
def test():
    global a
    a = 1
    print(a+1)

a = 'name'

print('全局a：', a)
test()
print('全局a：', a)

"""
结果
全局a： name
2
全局a： 1
"""
```

## 4 匿名函数 - lambda

​	lambda可以用来创建匿名函数，也可以将匿名函数赋值给一个变量供调用。

- **语法形式** **：**

  **lambda params:expr**

- 参数：

  params - 参数列表；

  expr - 要返回的表达式；

- 代码示例：

  ```Python
  #把匿名函数赋值给变量
  func = lambda x:x ** 3
  print(func(3))
  """
  结果
  27
  """
  ```

### 4.1 作用在函数上的Python内置函数

- **map()**

  1. 描述：将一个函数依次作用（或映射）到序列或迭代器对象的每个元素上，并返回一个map对象作为结果（不对原序列或迭代器对象作任何修改） 

  2. 语法：**map(function, iterable, …)**

  3. 参数：

     - funtion - 函数
     - iterable - 一个或多个序列

  4. 返回值：Python2.x返回列表，Python3.x返回迭代器

  5. 代码示例：

     ```Python
     print(map(lambda x:x ** 2, [1, 2, 3]))   #计算一个数的平方，返回可迭代对象
     print(map(lambda x,y:x+y, [1, 3, 5], (2, 4, 6))) #计算两个数的和
     print(list(map(lambda x:x ** 2, [1, 2, 3])))    #把结果放入列表中
     print(list(map(lambda x, y:x+y, [1, 3, 5], (2, 4, 6))))
     """
     结果
     <map object at 0x00000255778B83C8>  
     <map object at 0x00000255778B8550>
     [1, 4, 9]     
     [3, 7, 11]
     """
     ```

- **filter()**

  1. 描述：函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

  2. 语法：**filter(function, iterable)**

  3. 参数：

     - function - 函数
     - iterable - 可迭代对象

  4. 返回值：对象，可以用list()函数让它返回列表

  5. 代码示例：

     ```Python
     ite = filter(lambda x:x%2 == 0, [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10])
     aList = list(filter(lambda x:x%2 == 0, [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]))
     print(ite)
     print(aList)
     """
     结果
     <filter object at 0x00000168D8458550>
     [2, 4, 6, 8, 10]
     """
     ```

- **reduce()**

  1. 描述：函数会对参数序列中元素进行累积。函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

  2. 语法：**reduce(function, iterable[, initializer])**

  3. 参数：

     - function - 函数，有两个参数
     - iterable - 可迭代对象
     - Initializer - 可选，初始参数

  4. 返回值：返回计算结果

  5. 代码示例：

     ```Python
     from functools import reduce
     
     #计算1+2+3+...+100
     print(reduce(lambda x, y:x+y, range(1, 101)))
     #加初始值
     print(reduce(lambda x, y:x+y, range(1, 101), 100))
     """
     结果
     5050
     5150
     """
     ```



## 5 - 小结

​	该文档主要介绍函数的定义，函数的参数变量的作用域，还有Python的内置函数。



### 小练习

- **计算时间的下一秒**

  ```Python
  '''
  14:30:05
  14:30:06
  '''
  # '14:30:05'
  
  def timeNext():
      timeStr = input()
  
      # split():将字符串按照指定的字符进行分割
      list1 = timeStr.split(':')
      # print(list1)
      hour = int(list1[0])
      minute = int(list1[1])
      second = int(list1[2])
      # print(type(hour))
  
      second += 1
      if second == 60:
          second = 0
          minute += 1
          if minute == 60:
              minute = 0
              hour += 1
              if hour == 24:
                  hour = 0
  
      # print('%02d:%02d:%02d' % (hour, minute, second))
      return '%02d:%02d:%02d' % (hour, minute, second)
  
  if __name__ == '__main__':
      print(timeNext())
  ```

- **求两个数的最大公约数**

  ```Python
  def maxNum(num1, num2):
      if num1 < num2:
          num1, num2 = num2, num1
      if num1 % num2 == 0:
          return num2
      else:
          num3 = num1 % num2
          num1 = num2
          num2 = num3
          return maxNum(num2, num1)
  
  if __name__ == '__main__':
      print(maxNum(24, 46))
  ```

- **绘制奥运五环**

  ```Python
  import turtle
  turtle.pensize(10)
  turtle.color('black')
  turtle.circle(100)
  
  # 抬起画笔
  turtle.penup()
  # 画笔移动, x轴向左移是负的,向右移动是正的.y轴向上移动是正的,向下移动是负的
  turtle.goto(-200, 0)
  # 画笔放下
  turtle.pendown()
  turtle.color('blue')
  turtle.circle(100)
  
  
  # 抬起画笔
  turtle.penup()
  # 画笔移动, x轴向左移是负的,向右移动是正的.y轴向上移动是正的,向下移动是负的
  turtle.goto(200, 0)
  # 画笔放下
  turtle.pendown()
  turtle.color('red')
  turtle.circle(100)
  
  
  # 抬起画笔
  turtle.penup()
  # 画笔移动, x轴向左移是负的,向右移动是正的.y轴向上移动是正的,向下移动是负的
  turtle.goto(100, -172)
  # 画笔放下
  turtle.pendown()
  turtle.color('green')
  turtle.circle(100)
  
  
  # 抬起画笔
  turtle.penup()
  # 画笔移动, x轴向左移是负的,向右移动是正的.y轴向上移动是正的,向下移动是负的
  turtle.goto(-100, -172)
  # 画笔放下
  turtle.pendown()
  turtle.color('yellow')
  turtle.circle(100)
  
  turtle.done()
  ```

  



###  













