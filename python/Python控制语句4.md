# Python控制语句

> [TOC]
>
> 



## 1 - if

​	多数情况下，在执行程序时要根据程序中的某个条件来决定是否执行某一条语句，这就要用到if。

### 1.1 if基础

if的作用是选择执行语句，形式：

- **语法一**

  **if <条件>:**

  ​    **<语句>**

其中的条件可以是任意类型的表达式。

代码示例：

```Python
x = 3
if x == 3:
    print('1')
```

- **语法二**

  **if <条件1>:**

  ​    **<语句1>**

  **else:**

  ​    **<语句2>**

代码示例：

```Python
x = 3
if x == 3:
    print('1')
else:
    print('0')
```

- **语法三**

  **if <条件1>:**

  ​    **<语句1>**

  **elif <条件2>:**

  ​    **<语句2>**

  **else:**

  ​    **<语句3>**

  代码示例：

  ```Python
  x = 0
  if x > 0:
      print('1')
  elif x < 0:
      print('-1')
  else:
      print('0')
  ```

- **语法四**

  **if <条件1>:**

  ​    **<语句1>**

  **elif <条件2>:**

  ​    **<语句2>**

  **elif <条件3>:**

  ​    **<语句3>**

  **else:**

  ​    **<语句4>**

  代码示例：

  ```Python
  score = float(input('请输入你的分数：'))
  if score >= 90:
      print('A')
  elif score >=80:
      print('B')
  elif score >= 70:
      print('C')
  elif score >= 60:
      print('D')
  else:
      print('抱歉你没通过！')
  ```



### 1.2 if语句嵌套

- **语法一**

**if <条件1>:**

​    **if <条件2>:**

​        **<语句1>**

​    **elif <条件3>:**

​        **<语句2>**

**else:**

​    **<语句3>**

这种嵌套只是一种简单的情况，实际开发中根据功能可以写出更加复杂的嵌套结构。

代码示例：

```Python
score = float(input('请输入你的分数：'))
level = ''
if score >= 90:
    if score <= 95:
        level = 'A'
    else:
        level = 'A+'
elif score >= 80:
    if score <= 85:
        level = 'B'
    else:
        level = 'B+'
elif score >= 70:
    if score <= 75:
        level = 'C'
    else:
        level = 'C+'
else:
    level = 'D'
print(level)
```



## 2 - for

### 2.1 for基础

​	其他高级语言for语句要用循环控制变量来控制循环。Python中for语句通过循环遍历某一序列对象来构建循环。

- **语法**

  **for <循环变量> in <遍历对象>:**

  ​    **<语句1>**

  **else:**

  ​    **<语句2>**

示例代码：

```Python
for i in (1, 4, 5, 6):
    print(i)
else:      #循环结束
    print('over')
```

### 2.2 for 与break、continue

- **break** - 该语句的作用是中断循环的执行，如果在for循环中执行力了break语句，for语句的遍历就会立即终止，即使还有未遍历完的数据，还是会立即终止for循环语句。

- **continue** - 该语句的作用是提前停止循环体的执行，开始下一轮循环。在for语句中如果执行了continue语句，则continue语句后的循环体语句不会被执行，即提前结束了本次循环，然后进行下一个遍历循环。

  示例代码一：

  ```Python
  for i in (1, 2, 3, 4, 5, 6):
      if i % 3 == 0:
          continue
      print(i ** 2)
      if i % 5 == 0:
          break
   """
   结果
   1
   4
   16
   25
   """
  ```

  示例代码二：

  ```Python
  #for遍历字典
  dic = {'a':1, 'b':2, 'c':3}
  for key, value in dic.items():
      print(key, ':', value)
  for key in dic.keys():
      print(key)
  for value in dic.values():
      print(value)
      
  """
  结果
  a : 1
  b : 2
  c : 3
  a
  b
  c
  1
  2
  3
  """
  ```

### 2.3 for与range()

​	for语句中的对象集合不仅可以是列表、字典以及元祖，也可以是range()函数产生的一个整数列表，以完成循环。

- **range()** **-** **包前不包后**

  1. 语法：range([start,] stop[,step])

  2. 参数：

     start - 可选参数，循环开始的位置，默认为0；

     stop - 终止数，如果range只有一个参数x，将产生一个0到x-1的整数；

     step - 可选参数，步长，即每次循环序列增长值。

  3. 代码示例：

     ```Python
     >>> for i in range(6):print(i)
     
     
     0
     1
     2
     3
     4
     5
     
     
     >>> for i in range(2, 7):print(i)
     
     
     2
     3
     4
     5
     6
     
     
     >>> for i in range(2, 7, 2):print(i)
     
     
     2
     4
     6
     ```

     **注：for i in range(0):print(i)这条语句什么也不输出**。

### 2.4 for与内置迭代函数

- **enumerate()**

  1. 描述：用于为可迭代对象添加序号，默认序号从0开始，一般用在 for 循环当中。 

  2. 语法：**enumerate(iterable[,start=0])**

  3. 参数：

     - iterable -- 可迭代对象（字符串、列表、元祖、字典）。
     - start -- 序号起始位置，默认为0。

  4. 返回值：返回 enumerate(枚举) 对象。 

  5. 代码示例：

     ```Python
     #enumerate()的简单使用
     >>> l = ['a', 'b', 'c', 'd']
     
     #enumerate()把序号和序列中的元素放在一个元祖里
     l = ['a', 'b', 'c', 'd']
     for i in list(enumerate(l)):
         print(type(i))
         print(i[1])
     """
     结果
     <class 'tuple'>
     a
     <class 'tuple'>
     b
     <class 'tuple'>
     c
     <class 'tuple'>
     d
     """
     
     >>> enumerate(l)
     <enumerate object at 0x000002469C38C048>
     
     >>> list(enumerate(l))
     [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
     
     >>> list(enumerate(l, 1))
     [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
     
     #用普通的for循环给可迭代对象添加序号
     i = 0
     l = ['a', 'b', 'c', 'd']
     for element in l:
         print(i, element)
         i += 1
     """
     结果
     0 a
     1 b
     2 c
     3 d
     """
     
     #for循环使用enumerate()
     l = ['a', 'b', 'c', 'd']
     for i, element in enumerate(l):
         print(i, element)
     """
     结果
     0 a
     1 b
     2 c
     3 d
     """
     ```

- **sorted()** **- 内建函数**

  1. 描述：对所有可迭代的对象进行排序操作。 
  2. 语法：**sorted(iterable, key=None, reverse=False)**
  3. 参数：
     - iterable --  可迭代对象。
     - key --  主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
     - reverse --  排序规则，reverse = True  降序 ， reverse = False 升序（默认）。
  4. 返回值：返回重新排序的列表。 

- **sort()** **- 内建方法**

  1. 描述：直接对列表进行排序

  2. 语法：**list.sort(func=None, key=None, reverse=False)**

  3. 参数：

     - key --  主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
     - reverse --  排序规则，reverse = True  降序 ， reverse = False 升序（默认）。

  4. 返回值：返回重新排序的列表。 

  5. sorted()和sort()代码示例：

     ```Python
     >>> lst1 = [1, 5, 2, 6, 4, 0]
     
     
     >>> lst2 = sorted(lst1)
     
     >>> lst2
     [0, 1, 2, 4, 5, 6]
     
     #sorted()不改变原来的列表
     >>> lst1
     [1, 5, 2, 6, 4, 0]
     
     >>> lst1.sort()
     #sort()改变原来的列表
     >>> lst1
     [0, 1, 2, 4, 5, 6]
     
     #两者不是同一个引用，所以sorted()并没有改变原来的列表
     >>> id(lst1)
     2502292021832
     
     >>> id(lst2)
     2502291722184
     
     #指定升序还是降序
     >>> lst3 = [1, 5, 2, 6, 4, 0]
     >>> lst3.sort(reverse=True)
     >>> lst3
     [6, 5, 4, 2, 1, 0]
     >>> lst4 = [1, 5, 2, 6, 4, 0]
     >>> sorted(lst3, reverse=True)
     [6, 5, 4, 2, 1, 0]
     ```

  **注：**

  > **sort 与 sorted 区别：**
  >
  > sort 是应用在 list 上的方法，这是因为sort在原始序列上进行操作，要改变原始序列，所以他不能操作元祖。而sorted 可以对所有可迭代的对象进行排序操作。list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

- **reversed()**

  1. 描述：函数返回一个反转的迭代器。 

  2. 语法：**reverse(seq)**

  3. 参数：

     - seq - 要转换的序列，可以是 **tuple, string, list** 或 **range**。

  4. 返回值：返回一个反转的迭代器。 

  5. 示例代码：

     ```Python
     >>> str_temp = 'felix'
     >>> 
     reversed(str_temp)
     <reversed object at 0x000002469C37DC18>
     >>> list(reversed(str_temp))
     ['x', 'i', 'l', 'e', 'f']
     >>> tup = ('a', 'b', 'c')
     
     
     >>> reversed(tup)
     <reversed object at 0x000002469C37DCC0>
     
     
     >>> list(reversed(tup))
     ['c', 'b', 'a']
     
     
     >>> r = range(1, 5)
     >>> reversed(r)
     <range_iterator object at 0x000002469C379B90>
     
     
     >>> list(reversed(r))
     [4, 3, 2, 1]
     >>> lst = [1, 2, 3, 4]
     >>> reversed(lst)
     <list_reverseiterator object at 0x000002469C37DCC0>
     
     
     >>> list(reversed(lst))
     [4, 3, 2, 1]
     ```

- **zip()**

  1. 描述：将可迭代的对象作为参数，将对象中**对应的元素**打包成一个个元组，然后返回由这些元组组成的列表。 

  2. 语法：**zip([iterable, …])**

  3. 参数：

     - iterabl - 一个或多个迭代器。

  4. 返回值：返回zip对象，如果要变成列表需要自己转换。 

  5. 示例代码：

     ```Python
     >>> a = [1, 2, 3]
     >>> b = [4, 5, 6]
     >>> c = [7, 8, 9, 10]
     
     #压缩
     >>> zipped = zip(a, b)
     >>> zipped
     <zip object at 0x000002469C3A2848>
     >>> list(zipped)
     [(1, 4), (2, 5), (3, 6)]
     
     >>> zip(a, c)
     <zip object at 0x000002469C36D148>
     >>> list(zip(a, c))
     [(1, 7), (2, 8), (3, 9)]
     
     #解压
     >>> zip(*zipped)
     <zip object at 0x000002469C36D148>
     
     #解压完一次后就不存在了
     >>> list(zip(*zipped))
     []
     
     >>> zipped = zip(a, b)
     >>> list(zip(*zipped))
     [(1, 2, 3), (4, 5, 6)]
     
     >>> list(zip(*zip(a,c)))
     [(1, 2, 3), (7, 8, 9)]
     ```



## 3 - while

​	for 语句以遍历对象的方式构造循环，但我们有时候需要构造一种类似无限循环的程序控制结构或某种不确定运行次数的循环，while语句就派上了用场。

### 3.1 while基础

- **语法**

**while <条件>:**

​    **<语句1>**

**else:**

​    **<语句2>**

当while循环不是由break语句终止的话，则会执行else语句块中的语句。在while循环语句中，我们应尽量避免死循环。

代码示例：

```Python
aList = [1, 3, 2, 5, 6]
i = 0
sum = 0
while i < len(aList):
    sum += aList[i]
    i += 1
else:
    print('aList的和是：%.2f' % sum)
```

### 3.2 增量赋值运算符

如+的增量赋值：

**x += 1**

在while语句中，用增量运算符来修改循环控制变量比较方便。



## 4 - 推导或内涵

### 4.1 推导基础

​	推导的意思是指在Python中以紧凑的方式对列表、元祖、字典等序列或一系列元素进行处理，处理结果仍然放在一个列表、字典等序列之中的语法形式。

- **列表推导式的基本形式**

  **[<i相关表达式> for i in iterator]**

  其中 iterator是一个可遍历的对象，如列表、元祖也可以是range()函数。

  **注：当对列表、元祖、字典序列中的元素进行处理时，应该尝试用列表推导式完成，这有助于降低代码的复杂性。**

  代码示例：

  ```Python
  #把1~10之间的奇数的平方放在列表里
  aList = [i ** 2 for i in range(1, 11, 2)]
  print(aList)
  ```

- **字典的推导式语法**

  **{key, value for key, value in dict}**

  代码示例：

  ```Python
  >>> keys = {'name', 'age', 'sex'}
  >>> value = {'Felix', 12, '男'}
  
  
  >>> zip(keys, value)
  <zip object at 0x00000241BB753F88>
  
  >>> list(zip(keys, value))
  [('age', 'Felix'), ('name', '男'), ('sex', 12)]
  
  >>> {k:v for k, v in zip(keys, value)}
  {'age': 'Felix', 'name': '男', 'sex': 12}
  
  >>> {k:v for k, v in list(zip(keys, value))}
  {'age': 'Felix', 'name': '男', 'sex': 12}
  ```

  ### 4.2 给推导式添加条件

  ​	推导式不仅可以对所有元素进行遍历，也可以通过if语句对部分元素进行遍历。

  - **列表推导式**

    **[<i相关表达式> for i in iterator if <条件>]**

  - **字典推导式**

    **{key, value for key, value in iterator if <条件>}**

  - 代码示例：

    ```Python
    #序列中的奇数乘以2
    >>> aList = [2 * i for i in [1, 2,3, 4, 5, 6] if i %2 == 1]
    >>> aList
    [2, 6, 10]
    ```



## 5 - 小结

​	本文档简单的介绍了Python语言中一些常见的控制语句，以及它们的使用方法，这对于我们在处理实际问题时的不同选择有很大的用处。



