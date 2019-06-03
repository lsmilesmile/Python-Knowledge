# Python数据类型

> [TOC]
>
> 

------



## 1 - Python简单数据类型

### 1.1字符串（str）

​	字符串主要用于存储和表示文本。Python中的字符串通常由单引号“ ‘ ’”、双引号“ “ ”、三个单引号或者三个双引号包围的一串字符串组成。

**注：单双引号是英文字符中的符号**

​	字符串中的字符可以包含数字、字母、中文字符、特殊符号，以及一些转义字符，如换行符、制表符等。字符串可以通过序号（从0开始）来提取其中某个字符，如：

```Python
>>> str_temp = "我是Felix，24岁"
>>> str_temp[1]
'是'
>>> str_temp[7]
'，'
```

**三种表示字符串方法的区别和联系**

- 单引号字符串与双引号字符串本质上是相同的，但是当单引号字符串中包含单引号时，直接在字符串中写单引号则会报错，这是就需要用转移字符，这是本来由单引号表示的字符串就会变成由双引号表示的字符串，如果在单引号内有双引号时直接打双引号就行。双引号也是一样的道理。如：

```Python
>>> str_temp = "hello,我'是'felix,23岁"
>>> str_temp
"hello,我'是'felix,23岁"
>>> str_temp = "hello,我\"是\"felix,23岁"
>>> str_temp
'hello,我"是"felix,23岁'
>>> str_temp = 'hello,我"是"felix,23岁'
>>> str_temp
'hello,我"是"felix,23岁'
>>> str_temp = 'hello,我\'是\'felix,23岁'
>>> str_temp
"hello,我'是'felix,23岁"
>>> str_temp = "hello,我\"是felix,23岁"
>>> str_temp
'hello,我"是felix,23岁'
>>> str_temp = 'hello,我是\'felix,23岁'
>>> str_temp
"hello,我是'felix,23岁"
```

- 三引号字符串可以由多行组成（写多少行输出就有多少行字符串），单引号和双引号字符串则不行，如：

```Python
str_temp1 = """"hello,
我是felix,
23岁"""

str_temp2 = "hello,我是felix,23岁"

print(str_temp1)
print('-' * 10)
print(str_temp2)
"""
结果：
"hello,
我是felix,
23岁
----------
hello,我是felix,23岁
"""
```

- 前面已经知道如果一行字符串太长，可以换行写，我们来看看如果把换行写的一行字符串放在一个字符传变量中的输出是啥：

```Python
print("""hello""", \
      """我是felix""", \
      """23岁""")

str_temp1 = """hello""", \
      """我是felix""", \
      """23岁"""

print(str_temp1)
"""
结果：
hello 我是felix 23岁
('hello', '我是felix', '23岁')
"""
```

可以看到如果把它放在字符串，则输出的是一个元祖。

#### 1.1.1转义字符串

​	在Python中如果要在字符串中包含控制字符或特殊含义的符号，就需要使用转义字符。

<center>**表1 常见转义字符**</center>

| 转义字符 |              含义              |
| :------: | :----------------------------: |
|    \b    |   退格把光标移动到前一列位置   |
|    \f    |             换页符             |
|    \n    |             换行符             |
|    \r    |              回车              |
|    \t    |           水平制表符           |
|    \v    |           垂直制表符           |
|    \\    |             一个\              |
|   ////   |               //               |
|   \\'    |             单引号             |
|    \”    |             双引号             |
|   \ooo   |     3位八进制数对应的字符      |
|   \xhh   |    2位十六进制数对应的字符     |
|  \uhhhh  | 4位十六进制数表示的Unicode字符 |

如：

```Python
>>> print('abc\n123')
abc
123
```

#### 1.1.2原始字符串

当我们不想用转义字符‘\’时，可以使用原始字符串。就是在字符串前加上r或R。如：

```Python
>>> p = r'abc\d\ef'
>>> print(p)
abc\d\ef
```

#### 1.1.3格式字符

​	格式字符一般是用来占位的

<center>**表2 格式字符**</center>

| **格式字符** |             **说明**              |
| :----------: | :-------------------------------: |
|      %s      |      字符串（采用str()显示）      |
|      %r      |    字符串（采用repr()的显示）     |
|      %c      |             单个字符              |
|      %b      |            二进制整数             |
|      %d      |            十进制整数             |
|      %i      |            十进制整数             |
|      %o      |            八进制整数             |
|      %x      |           十六进制整数            |
|      %e      |           指数（底为e）           |
|      %E      |           指数（底为E）           |
|    %f、%F    |              浮点数               |
|      %g      | 指数（e）或浮点数（根据显示长度） |
|      %G      | 指数（E）或浮点数（根据长度显示） |
|      %%      |              字符“%”              |

#### 1.1.4字符串格式化输出

- **rjust(),ljust(),center()**

1. **rjust() - 右对齐**

   语法：str.rjust(width, [fillchar])

   参数说明：
   width - 字符串占位长度；

   fillchar - 可选参数，指定填充字符，默认为空格

2. **ljust() - 左对齐**

   语法：str.ljust(width, [fillchar])

   参数说明：

   width - 字符串占位长度；

   fillchar - 可选参数，指定填充字符，默认为空格

3. **center() - 居中**

   语法:str.center(width, fillchar)

   参数说明：

   width - 字符串占位长度；

   fillchar - 可选参数，指定填充字符，默认为空格

示例代码：

```Python
>>> str_temp = 'hello'


>>> str_temp.rjust(10)
'     hello'
>>> str_temp.rjust(10, '*')
'*****hello'

>>> str_temp.ljust(10)
'hello     '
>>> str_temp.ljust(10, '*')
'hello*****'

>>> str_temp.center(10)
'  hello   '
>>> str_temp.center(10, '*')
'**hello***'
>>> 
```

- **%**

语法形式：‘%【-】【+】【0】【m】【.n】格式字符’ % x

<center>**表3 字符串格式化符号和含义**</center>

|   符号   |          含义          |
| :------: | :--------------------: |
|    %     | 格式标志，表示格式开始 |
|   [-]    |     指定左对齐输出     |
|   [+]    |      对正数加正号      |
|   [0]    |      指定空位填0       |
|   [m]    |      指定最小宽度      |
|   [.n]   |        指定精度        |
| 格式字符 |   指定类型（见上表）   |
|    %     |       格式运算符       |
|    x     |     待转换的表达式     |

如：%f给浮点数占位，默认保留6位小数。相关格式：

​	%.2f - 保留两位小数；

​	%.10.2f - 共十位，保留两位小数，其他位用空格填充；

​	%010.2f - 共十位，保留两位小数，其他位用0填充；

示例代码：

```Python
>>> name = 'Felix'
>>> age = 23
>>> height = 180
>>> print('我叫%s，我今年%d岁，身高%dcm' % (name, age, height))
我叫Felix，我今年23岁，身高180cm

>>> pi = 3.1415
>>> print('圆周率是%f' % (pi))
圆周率是3.141500
>>> print('圆周率是%.3f' % (pi))
圆周率是3.142
>>> print('圆周率是%10.2f' % (pi))
圆周率是      3.14
>>> print('圆周率是%010.2f' % (pi))
圆周率是0000003.14

>>> a = 'w'
>>> print('%c' % (a))
w

>>> a = 10
>>> print('%o' % a)
12
>>> print('%x' % a)
a
>>> print('%x' % (a))
a
>>> 
```

**注：待转换的表达式是放在元祖里面的，如果只有一个量，则可以不放元祖里面。**

- **format()** **- 通过{}来代替传统的%方式**

1. 使用位置参数 - 位置参数不受顺序约束，且可以为{}，只要format里有对应的参数值即可，参数索引从0开始，传入位置参数列表可用*列表的形式。

   示例代码：

   ```Python
   >>> li = ['felix', 21]
   
   
   >>> print('my name is {},age{}'.format(li[0], li[1]))
   my name is felix,age21
   
   
   >>> print('my name is {},age{}'.format(*li))  #相当于序列解包
   my name is felix,age21
   
   
   >>> print('my name is {1},age{0}'.format(19, 'smile'))
   my name is smile,age19
   >>> 
   ```

   

2. 使用关键字参数 - 关键字参数值要对得上，可用字典当关键字参数传入值，字典前加**即可。

   示例代码：

   ```Python
   set_temp = {'name':'felix', 'age':19}
   
   
   >>> print('my name is {name},age is {age}'.format(name = 'fff', age = 19))
   my name is fff,age is 19
   
   
   >>> print('my name is {name},age is {age}'.format(**set_temp))
   my name is felix,age is 19
   >>> 
   ```

3. 填充与格式

   语法格式：‘{0:【填充字符】【对齐方式（<^>）】【宽度】}‘.format()

   示例代码：

   ```Python
   >>> print('{0:*<10}'.format(20))
   20********
   
   >>> print('{0:%^11}'.format('felix'))
   %%%felix%%%
   
   >>> print('{0:$>10}'.format(10))
   $$$$$$$$10
   >>> 
   ```

4. 精度与进制

   示例代码：

   ```Python
   >>> print('{0:*>10.3f}'.format(20))
   ****20.000
   """
   参数：
   *：填充空位
   >：右对齐
   10：共占10个位置
   .3f：保留三位有效数字
   """
   >>> print('{0:b}'.format(10))
   1010
   
   >>> print('{:,}'.format(4151656215161717)) #千分位格式化
   4,151,656,215,161,717 
   ```

5. 使用索引

   示例代码：

   ```Python
   >>> li = ['felix', 12]
   
   >>> print('name is {0[0]},age is {0[1]}'.format(li))
   name is felix,age is 12
   >>> 
   ```

#### 1.1.5字符串常用方法

- **find()**

1. 描述：find() 方法从字符串中找出某个子字符串第一个匹配项的索引位置，该方法与index()方法一样，只不过如果子字符串不在字符串中不会报异常，而是返回-1。

2. 语法：**s.find(sub[,start=0,[end=len(s)])**

3. 参数：

   - sub - 指定检索的字符串
   - s - 父字符串
   - start - 可选参数，开始索引，默认为0.（可单独指定）
   - end - 可选参数，结束索引，默认为字符串的长度。（不能单独指定）

4. 返回值：返回字符串第一个匹配项出现在字符串中的索引位置，如果没有匹配项则返回-1。

5. 代码示例

   ```Python
   >>> s = "hello,my name is felix,and you"
   
   >>> s.find('o', 5, len(s))
   28
   >>> s.find('o', 4, len(s))
   4
   >>> s.find('o', 6)
   28
   >>> s.find('o')
   4
   >>> s.find('k')
   -1
   ```

- **rfind()**
  1. 描述：返回字符串最后一次出现在字符中中的索引位置，该方法与rindex()方法一样，只不过如果字符串不在字符串中不会报异常，而是返回-1.

  2. 语法：**s.rfind(sub, [,start=0[,end=len(s)]])**

  3. 参数：

     - sub - 指定检索的字符串
     - s - 父字符串
     - start - 可选参数，开始索引，默认为0.（可单独指定）
     - end - 可选参数，结束索引，默认为字符串的长度。（不能单独指定）

  4. 返回值：返回子字符串最后一次出现在字符串中的的索引位置，如果没有匹配项则返回-1。 

  5. 代码示例

     ```Python
     >>> s = "hello,my name is felix,and you"
     
     >>> s.rfind('o', 0, 5)
     4
     >>> s.rfind('o', 0)
     28
     >>> s.rfind('o')
     28
     >>> s.rfind('k')
     -1
     ```

- **index()**
  1. 描述：检测字符串中是否包含子字符串  ，该方法与find()方法一样，只不过如果子字符串不在 父字符串中会报一个异常。

  2. 语法：**s.index(sub[,start=0[,end=len(s)]])**

  3. 参数:
     - sub - 指定检索的字符串
     - s - 父字符串
     - start - 可选参数，开始索引，默认为0.（可单独指定）
     - end - 可选参数，结束索引，默认为字符串的长度。（不能单独指定）

  4. 返回值：返回字符串第一个匹配项出现在字符串中的索引位置，如果没有匹配项则抛出异常的。

  5. 代码示例

     ```Python
     >>> s = "hello,my name is felix,and you"
     
     >>> s.index('o', 5, len(s))
     28
     >>> s.index('o', 5)
     28
     >>> s.index('o')
     4
     >>> s.index(k)
     Traceback (most recent call last):
       File "<pyshell#4>", line 1, in <module>
         s.index(k)
     NameError: name 'k' is not defined
     ```

- **rindex()**
  1. 描述：返回字符串最后一次出现在字符串中的索引位置，该方法与rfind()方法一样，只不过如果字符串不在字符串中会报一个异常。

  2. 语法：**s.rindex(sub[,start=0[,end=len(s)]])** 

  3. 参数：

     - sub - 指定检索的字符串
     - s - 父字符串
     - start - 可选参数，开始索引，默认为0.（可单独指定）
     - end - 可选参数，结束索引，默认为字符串的长度。（不能单独指定）

  4. 返回值：返回子字符串最后一次出现在字符串中的的索引位置，如果没有匹配项则会报一个异常。 

  5. 代码示例

     ```Python
     >>> s = "hello,my name is felix,and you"
     
     >>> s.rindex('o', 0, 6)
     4
     >>> s.rindex('o', 10)
     28
     >>> s.rindex('o')
     28
     >>> s.rindex('k')
     Traceback (most recent call last):
       File "<pyshell#9>", line 1, in <module>
         s.rindex('k')
     ValueError: substring not found
     ```

- **count()**
  1. 描述：统计子字符串在父字符串中出现的次数。

  2. 语法：**s.count(sub[,start=0[,end=len(s)]])**

  3. 参数：

     - sub - 指定检索的字符串
     - s - 父字符串
     - start - 可选参数，开始索引，默认为0.（可单独指定）
     - end - 可选参数，结束索引，默认为字符串的长度。（不能单独指定）

  4. 返回值：存在则返回出现的次数，不存在返回0。

  5. 代码示例

     ```Python
     >>> s = "hello,my name is felix,and you"
     
     >>> s.count('o', 10, len(s))
     1
     >>> s.count('o', 10)
     1
     >>> s.count('o')
     2
     >>> s.count('k')
     0
     ```

- **split()**
  1. 描述：拆分字符串。通过指定分隔符对字符串进行切片。

  2. 语法：**s.split(sf="",num=string.count(str))[n]** 

  3. 参数：

     - sf - 表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素 
     - num - 表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量 
     - [n] - 表示选取第n个分片 

  4. 返回值：返回分割后的字符串列表（list） 。

  5. 代码示例

     ```Python
     >>> s = "hello,my name is felix,and you"
     
     
     >>> s.split()
     ['hello,my', 'name', 'is', 'felix,and', 'you']
     
     >>> s.split('m', 1)
     ['hello,', 'y name is felix,and you']
     
     >>> s.split('m')
     ['hello,', 'y na', 'e is felix,and you']
     
     >>> s.split('k')
     ['hello,my name is felix,and you']
     ```

- **rsplit()**
  1. 描述：通过指定分隔符对字符串进行分割并返回一个列表，默认分隔符为所有空字符，包括空格、换行(\n)、制表符(\t)等。类似于split()方法，只不过是从字符串最后面开始分割。 

  2. 语法：**s.rsplit(【sep=None】【,count=s.count(sep)】)**

  3. 参数：

     - sep - 可选参数，指定的分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
     - count - 可选参数，分割次数，默认为分隔符在字符串中出现的总次数

  4. 返回值：返回分割后的字符串列表

  5. 代码示例

     ```Python
     >>> s = "hello,my name is felix,and you"
     
     
     >>> s.rsplit()
     ['hello,my', 'name', 'is', 'felix,and', 'you']
     
     >>> s.rsplit('y')
     ['hello,m', ' name is felix,and ', 'ou']
     
     >>> s.rsplit('y', 1)
     ['hello,my name is felix,and ', 'ou']
     
     >>> s.rsplit('k')
     ['hello,my name is felix,and you']
     ```

- **partition()**
  1. 描述：用来根据指定的分隔符将字符串进行分割。如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符前面的子字符串，第二个为分隔符本身，第三个为分隔符后面的子字符串。partition() 方法是在Python 2.5中新增的。

  2. 语法：**s.partition(sep)**

  3. 参数：

     - sep - 指定的分隔符

  4. 返回值：返回一个3元的元组，第一个为分隔符前面的子字符串，第二个为分隔符本身，第三个为分隔符后面的子字符串。 

  5. 代码示例：

     ```Python
     >>> s = "http://www.w3cschool.cc/"
     
     
     >>> s.partition('//')
     ('http:', '//', 'www.w3cschool.cc/')
     
     #指定的分割字符不存在
     >>> s.partition('k')
     ('http://www.w3cschool.cc/', '', '')
     ```

- **rpartiton()**
  1. 描述：用来根据指定的分隔符将字符串进行分割。如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符前面的子字符串，第二个为分隔符本身，第三个为分隔符后面的子字符串。只不过从字符串最后开始分割。

  2. 语法：**s.rpartition(sep)**

  3. 参数：

     - sep - 指定的分隔符

  4. 返回值：返回一个3元的元组，第一个为分隔符前面的子字符串，第二个为分隔符本身，第三个为分隔符后面的子字符串。

  5. 代码示例：

     ```Python
     >>> s = "http://www.w3cschool.cc/"
     
     >>> s.rpartition('w')
     ('http://www.', 'w', '3cschool.cc/')
     
     >>> s.partition('w')
     ('http://', 'w', 'ww.w3cschool.cc/')
     ```

- **join()**
  1. 描述：用于将可迭代对象中的元素以指定的字符连接生成一个新的字符串。 

  2. 语法：**s.join(iterable)**

  3. 参数：

     - iterable -- 可迭代对象（字符串、列表、元祖、字典）。 

  4. 返回值：返回通过指定字符连接可迭代对象中的元素后生成的新**字符串**。 

  5. 代码示例：

     ```Python
     >>> iter_temp = ['h', 'e', 'l', 'l', 'o']
     >>> s1 = ''
     >>> s2 = '_'
     
     >>> s1.join(iter_temp)
     'hello'
     
     >>> s2.join(iter_temp)
     'h_e_l_l_o'
     ```

     

- **lower()**
  1. 描述：转换字符串中所有大写字符为小写。

  2. 语法：**s.lower()**

  3. 参数：\

  4. 返回值：返回将字符串中所有大写字符转换为小写后生成的字符串。

  5. 代码示例：

     ```Python
     >>> s = 'hELlo'
     
     >>> s.lower()
     'hello'
     ```

- **upper()**
  1. 描述：将字符串中所有小写字母转换为大写字母。

  2. 语法：**s.upper()**

  3. 参数：\

  4. 返回值：返回小写字母转换为大写字母的字符串。

  5. 代码示例：

     ```Python
     >>> s = 'hELlo'
     
     >>> s.upper()
     'HELLO'
     ```

- **capitalize()**
  1. 描述：将字符串的第一个字母变成大写，其他字母变小写。

  2. 语法：**s.capitalize()**

  3. 参数：\

  4. 返回值：返回一个首字母大写的字符串。

  5. 代码示例：

     ```Python
     >>> s = 'hELlo'
     
     >>> s.capitalize()
     'Hello'
     ```

- **title()**
  1. 描述：返回“标题化”的字符串，就是说所有单词都是以大写开始的，其余字母均为小写。

  2. 语法：**s.title()**

  3. 参数：\

  4. 返回值：返回"标题化"的字符串，就是说所有单词都是以大写开始。 

  5. 代码示例

     ```Python
     >>> s = "this is string example from runoob....wow!!!"
     
     >>> s.title()
     'This Is String Example From Runoob....Wow!!!'
     ```

- **swapcase()**
  1. 描述：对字符串的大小写字母进行转换。 

  2. 语法：**s.swapcase()**

  3. 参数：\

  4. 返回值：返回大小写字母转换后生成的新字符串。

  5. 代码示例

     ```Python
     >>> s = 'HellO'
     
     >>> s.swapcase()
     'hELLo'
     ```

- **replace()**
  1. 描述：用于把字符串中指定的旧子字符串替换成指定的新子字符串，如果指定 count 可选参数则替换指定的次数，默认全部替换。 

  2. 语法：**s.replace(old, new【,count=s.count(old)】)**

  3. 参数：

     - old - 指定的旧子字符串
     - new - 指定的新子字符串
     - count - 可选参数，替换的次数，默认为指定的旧子字符串在字符串中出现的总次数。

  4. 返回值：返回把字符串中指定的旧子字符串替换成指定的新子字符串后生成的新字符串，如果指定 count 可选参数则替换指定的次数，默认为指定的旧子字符串在字符串中出现的总次数。 

  5. 代码示例

     ```Python
     >>> s = 'i do not like he,but he is good'
     
     >>> s.replace('he', 'she')
     'i do not like she,but she is good'
     
     >>> s.replace('he', 'she', 1)
     'i do not like she,but he is good'
     ```

- **maketrans()**
  1. 描述：用于给translate()方法创建字符映射转换表。可以只接受一个参数，此时这个参数是个字典类型。

     对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串，表示转换的目标。两个字符串的长度必须相同，为一一对应的关系。在Python3中可以有第三个参数，表示要删除的字符，也是字符串。一般 maketrans() 方法需要配合translate()方法一起使用。

     **注：Python3.4 以后已经不需要从外部 string 模块中来调用 maketrans() 方法了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans()。**

  2. 语法：**s.maketrans(intab, outtab[,delchars])**

  3. 参数：

     - intab - 需要转换的字符组成的字符串。
     - outtab - 转换的目标字符组成的字符串。
     - delchars - 可选参数，表示要删除的字符组成的字符串。

  4. 返回值：返回一个字符映射转换表供translate()方法调用。 

  5. 代码示例：

     ```Python
     >>> s = 'hello,my name is felix,i love China'
     >>> intab = 'emixo'
     >>> outtab = '12345'
     >>> deltab = 'fya'
     
     #创建字符映射表
     >>> trantab1 = str.maketrans(intab, outtab)
     #创建字符映射表并删除指定字符
     >>> trantab2 = str.maketrans(intab, outtab, deltab)
     
     >>> print(s.translate(trantab1))
     h1ll5,2y na21 3s f1l34,3 l5v1 Ch3na
     
     >>> print(s.translate(trantab2))
     h1ll5,2 n21 3s 1l34,3 l5v1 Ch3n
     
     
     ```

- **translate()**

  **见maketrans()函数**

- **strip()**
  1. 描述：用于删除字符串头部和尾部指定的字符，默认字符为所有空字符，包括空格、换行(\n)、制表符(\t)等。 

  2. 语法：**s.strip([chars])**

     ```
     注：[chars]是字符的集合，只要头尾的字符出现在[chars]中则全部删除
     ```

  3. 参数：

     - chars - 可选参数，要删除的指定字符（串），默认字符为所有空字符，包括空格、换行(\n)、制表符(\t)等。 

  4. 返回值：返回删除字符串头部和尾部指定的字符后生成的新的字符串。 

  5. 代码示例

     ```Python
     >>> s = '   my name is felix  '
     
     >>> s.strip()
     'my name is felix'
     
     #如果头尾不存在要删除的字符（串），则返回原字符（串）
     >>> s.strip('m')
     '   my name is felix  '
     >>> s.strip('m') == s
     True
     
     #删除指定字符（串）
     >>> s = 'my name is felm'
     >>> s.strip('m')
     'y name is fel'
     ```

     

- **rstrip()**
  1. 描述：删除字符串尾部指定的字符，默认字符为所有空字符，包括空格、换行(\n)、制表符(\t)等。 

  2. 语法：**s.rstrip([chars])**

  3. 参数：

     - chars - 可选参数，要删除的指定字符，默认字符为所有空字符，包括空格、换行(\n)、制表符(\t)等。 

  4. 返回值：返回删除字符串尾部指定的字符后生成的新的字符串。 

  5. 代码示例

     ```Python
     >>> s = 'my name is felix  '
     
     >>> s.rstrip()
     'my name is felix'
     
     
     >>> s = 'my name is felix'
     >>> s.rstrip('x')
     'my name is feli'
     
     #删除不存在的字符（串），返回原始字符串
     >>> s.rstrip('k')
     'my name is felix'
     ```

- **lstrip()**
  1. 描述：删除字符串头部指定的字符，默认字符为所有空字符，包括空格、换行(\n)、制表符(\t)等。 

  2. 语法：**s.lstrip([chars])**

  3. 参数：

     - chars - 可选参数，要删除的指定字符，默认字符为所有空字符，包括空格、换行(\n)、制表符(\t)等。 

  4. 返回值：返回删除字符串头部指定的字符后生成的新的字符串。 

  5. 代码示例：

     ```Python
     >>> s = '   my name is felix'
     
     >>> s.lstrip()
     'my name is felix'
     
     >>> s = 'my name is felix'
     >>> s.lstrip('m')
     'y name is felix'
     
     #删除不存在的字符（串），返回原始字符串
     >>> s.lstrip('k')
     'my name is felix'
     ```

- **eval()**
  1. 描述：执行一个字符串表达式，并返回表达式的值。 

  2. 语法：**eval(expression[, globasl[, locals]])**

  3. 参数：

     - expression - 表达式。
     - globals - 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
     - locals - 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

  4. 返回值：返回表达式计算结果。 

  5. 代码示例：

     ```Python
     >>> x = 4
     
     >>> s = '3 * x'
     >>> eval(s)
     12
     
     >>> eval('pow(2, 2)')
     4
     ```

- **in/not in**

  1. 描述：**in** - 如果在指定的序列中找到值返回 True，否则返回 False。**not in** - 如果在指定的序列中没有找到值返回 True，否则返回 False。 

  2. 语法：**s in string/s not in string**

  3. 参数：\

  4. 返回值：True/False

  5. 代码示例：

     ```Python
     >>> s = 'hello'
     
     >>> 'h' in s
     True
     >>> 'k' in s
     False
     ```

- **startswith()**

  1. 描述：判断字符串是否以指定前缀开头，如果是则返回 True，否则返回 False。 

  2. 语法：**s.startswith(prefix[,start=0[,end=len(s)]])**

  3. 参数：

     - s - 父字符串。
     - prefix - 指定前缀，该参数可以是一个字符串或者是一个元素。
     - start - 可选参数，字符串中的开始位置索引，默认为0。（可单独指定）
     - end - 可选参数，字符中结束位置索引，默认为字符串的长度。（不能单独指定）

  4. 返回值：如果**字符串（包括字符）**以指定的前缀开头返回 True ，否则返回 False。 

  5. 代码示例：

     ```Python
     >>> s = 'my name is felix'
     
     >>> s.startswith('m')
     True
     >>> s.startswith('my')
     True
     >>> s.startswith('k')
     False
     >>> s.startswith('n', 3)
     True
     >>> s.startswith('n', 3, len(s))
     True
     ```

- **endswith()**

  1. 描述：判断字符串是否以指定后缀结尾，如果是则返回 True，否则返回 False。 

  2. 语法：**s.endswith(suffix,[,start=0[,end=len(s)]])**

  3. 参数：
     - s - 父字符串。
     - suffix - 指定后缀，该参数可以是一个字符串或者是一个元素。
     - start - 可选参数，字符串中的开始位置索引，默认为0。（可单独指定）
     - end - 可选参数，字符中结束位置索引，默认为字符串的长度。（不能单独指定）

  4. 返回值：如果字符串以指定的后缀结尾返回 True ，否则返回 False。 

  5. 代码示例

     ```Python
     >>> s = 'my name is felix'
     
     
     >>> s.endswith('x')
     True
     >>> s.endswith('ix')
     True
     
     
     >>> s.endswith('k')
     False
     >>> s.endswith('i', 3)
     False
     
     #后面两个参数的范围是[3,6),即[3, 5],前包后不包
     >>> s.endswith('e', 3, 6)
     False
     >>> s.endswith('m', 3, 6)
     True
     >>> s.startswith('n', 3, 6)
     True
     ```

- **isalnum()**

  1. 描述：测字符串是否由**字母或数字**组成。 

  2. 语法：**s.isalnum()**

  3. 参数：\

  4. 返回值：如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False 

  5. 代码示例：

     ```Python
     >>> s = 'ljld8686'
     
     >>> s.isalnum()
     True
     
     #有点
     >>> s = 'www.51jb.com'
     >>> s.isalnum()
     False
     ```

- **isalpha()**

  1. 描述：检测字符串是否**只由字母或汉字**组成。 

  2. 语法：**s.isalpha()**

  3. 参数：\

  4. 返回值：如果字符串至少有一个字符并且所有字符都是字母或汉字则返回 True,否则返回 False 。

  5. 代码示例：

     ```Python
     >>> s = 'my name is 刘'
     >>> s.isalpha()
     False
     
     >>> s = 'mynameis刘'
     >>> s.isalpha()
     True
     >>> 
     ```

- **isdigit()**

  1. 描述：检测字符串是否**只由数字组成**。 

  2. 语法：**s.isdigit()**

  3. 参数：\

  4. 返回值：如果字符串只包含数字则返回 True 否则返回 False。 

  5. 代码示例：

     ```Python
     >>> s = '3.1415926ppp'
     >>> s.isdigit()
     False
     
     >>> s = '3.1415926'
     >>> s.isdigit()
     False
     
     >>> s = '31415926'
     >>> s.isdigit()
     True
     ```

- **isspace()**

  1. 描述：检测字符串是否**只由空格**组成。 

  2. 语法：**s.isspace()**

  3. 参数：\

  4. 返回值：如果字符串中至少有一个字符，并且所有字符都是空格，则返回 True，否则返回 False。 

  5. 代码示例：

     ```Python
     >>> s = 'hello python'
     >>> s.isspace()
     False
     
     >>> s = '     '
     >>> s.isspace()
     True
     ```

- **isupper()**

  1. 描述：检测**字符串中所有的字母**是否都为大写。 

  2. 语法：**s.isupper()**

  3. 参数：\

  4. 返回值：如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False 

  5. 代码示例：

     ```Python
     #只有字母，全部小写
     >>> s = 'hello'
     >>> s.isupper()
     False
     
     #只有字母，大小写都有
     >>> s = 'HELLo'
     >>> s.isupper()
     False
     
     #只有字母，全部大写
     >>> s = 'HELLO'
     >>> s.isupper()
     True
     
     #有字母、数字、符号，是字母的都是大写
     >>> s = 'H453ELL098O...'
     >>> s.isupper()
     True
     ```

     

- **islower()**

  1. 描述：检测**字符串中所有的字母**是否都为小写。 

  2. 语法：**s.islower()**

  3. 参数：\

  4. 返回值：如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False 。

  5. 代码示例：

     ```Python
     >>> s = 'HELLO'
     >>> s.islower()
     False
     
     >>> s = 'HELlo'
     >>> s.islower()
     False
     
     >>> s = 'hello'
     >>> s.islower()
     True
     
     >>> s = 'www.baidu.com/123'
     >>> s.islower()
     True
     ```

- **zfill()**

  1. 描述：返回指定长度的字符串，原字符串右对齐，前面填充0。 

  2. 语法：**s.zfill(width)**

  3. 参数：

     -  width - 指定字符串的长度。原字符串右对齐，前面填充0。

  4. 返回值 ：返回指定长度的字符串。 

  5. 代码示例：

     ```Python
     >>> s = 'qwertyuiop'
     >>> s.zfill(10)
     'qwertyuiop'
     
     #长度小于原始字符串则返回原始字符串
     >>> s.zfill(5)
     'qwertyuiop'
     
     >>> s.zfill(11)
     '0qwertyuiop'
     
     >>> s.zfill(20)
     '0000000000qwertyuiop'
     ```

#### 1.1.6中文字符串处理

​	在Python3.x版本中，字符串已全面支持中文，并且默认都是utf-8编码字符串。但是在不同的平台或者应用系统之间，字符编码可能不同，就会造成字符乱码现象，这时应该用相关函数对字符串进行编码或者解码。

如，在网络上发送字符串时必须转换成字节串（bytes）形式，那么就要使用**字符串的encode()**方法，**返回字节串**（bytes），形式如下：

**encode(encoding=‘uutf-8’, errors=‘strict’)**

参数意义：

- encoding默认编码方式是utf-8，也可以使用gbk、gb2312等方式编码；
- errors编码错误的处理方式。默认为strict（报错），或者用ignore、replace等形式。

反之，如果从网络上接受的字节串为字符串，则要使用**字节串的decode()**方法来进行解码，才能看到原来的字符串，形式如下

**decode(encoding=‘utf-8’, errors=‘strict’)**

参数意义与前面相同，**返回字符串类型数据**。

示例代码：

```Python
>>> test = '我在成都'


>>> test_ec = test.encode()
>>> print(test_ec)
b'\xe6\x88\x91\xe5\x9c\xa8\xe6\x88\x90\xe9\x83\xbd'

>>> test_dc = test_ec.decode()
>>> print(test_dc)
我在成都
```

#### 1.6.7 提取字符串中某个字符

```Python
'''
提取字符串中的某一个字符
方式:
从左往右开始, 下标从0开始提取
str[0]   str[1]   str[2] ..... str[n]

从优往左开始, 下标从-1开始
str[-1]  str[-2] .....  str[-n]

'''
str1 = 'It is a dog'
print(str1[0])
print(str1[-2])

# pytjon中的字符串一旦定义好之后,是不可以修改的
str1[0] = 'i'
print('str1 =', str1)
```

#### 1.6.8 字符串比较大小

```Python
[规则:]从第一个字符开始比较,将字符转换成ascii值进行比较
如果小于则返回True,否则返回False
```



### 1.2整数（int）

#### 1.2.1整数的表示

​	整数包括正整数、负整数和零。Python中的整数的其他进制表示方式：0 + “进制标志” + 数字代表不同进制的数，具体如下：

- 0o【0O】数字 - 八进制整数（如：0o24、0O24）；

- 0x【0X】数字 - 十六进制整数（如：0x3F、0X3F）；

- 0b【0B】数字 - 二进制整数（如：0b101、0B101）。

  不带进制标志的为十进制整数。

#### 1.2.2整数的运算

<center>表5 整数运算符</center>

| 运算符 |   描述   |
| :----: | :------: |
|   **   |   乘方   |
|   *    |   乘法   |
|   /    |   除法   |
|   //   |   整除   |
|   %    |   取余   |
|   +    |   加法   |
|   -    |   减法   |
|   \|   |   位或   |
|   ^    |  位异或  |
|   &    |   位与   |
|   <<   | 左移运算 |
|   >>   | 右移运算 |

**以上运算符优先级（高到低排列）：**

- **
- *、/、%
- +、-
- |、^、&、<<、>>

**注：括号里的具有最高的优先级**

#### 1.2.3位运算

示例代码：

```Python
'''
位运算符:一般情况下把数字当做二进制来进行计算
&(按位与)
|(竖杠)(按位或)
^(按位异或)
~(按位取反)
<<(左移)
>>(右移)
'''
'''
按位与
规则: 有0则0,双1则1
'''
"""
00000000000000000000000000000100
00000000000000000000000000000101
----------------------------------
000000000000000000000000000000100
00000110
00001000
--------------
00000000
"""
print(4 & 5) #结果：4
print(6 & 8) #0

"""
按位或:
规则: 有1则1,双0则0
00000000000000000000000000000011
00000000000000000000000000000110
---------------------------------
00000000000000000000000000000111
00000101
00001001
--------
00001101
"""
print(3 | 6) #7
print(5 | 9) #13

"""
按位异或:
规则: 相同为0,不同为1
00000100
00000110
--------
00000010

00000111
00001000
--------------
00001111
"""
print(4 ^ 6) #2
print(7 ^ 8) #15


"""
按位取反:
规则: [将二进制数+1之后乘以-1]
00000100
00000101
-------------
1000000000000000000000000000101

0000000000000000000000000000011
0000000000000000000000000000100
-------------------------------
1000000000000000000000000000100

0000000000000000000000000001000
0000000000000000000000000001001
-----------------------------------
10000000000000000000000000001001

"""
print(~4) #-5
print(~3) #-4
print(~8) #-9



"""
左移: 
规则: 每个二进制位为全部向左移动,高位弃之,低位补0
0000000000000000000000000000101
0000000000000000000000000010100


"""
print(5 << 2) #20
print(1 << 2) #4
print(-1 << 2) #-4


"""
右移:
规则: 每个二进制位为全部向右移动,低位弃之,高位补0
1000000000000000000000000000101
1000000000000000000000000000001


"""
print(5 >> 2) #1
print(1 >> 2) #0
print(-5 >> 2)#-2
print(-2 >> 2)#-1
```

#### 1.2.4Python中的and和or

**and** - 从左到右计算表达式，若所有值都为真则返回最后一个值，若存在假，则返回第一个假值；

**or** - 从左到右计算表达式，返回第一个为真的值。

示例代码：

```Python
>>> 'a' and 'b'
'b'              #a和b都为真，返回b

>>> '' and 'b'
''               #''为假，返回第一个假

>>> 'a' or 'b'
'a'              #a和b都为真，返回第一个真

>>> '' or 'b'
'b'              #第一个真为b
```



### 1.3浮点数（float）

浮点数就是小数。

书写形式：

- 19.   小数部分为零，可以不写；
- .098  整数部分为零，可以不写；
- -2e3  科学计数法，表示-2乘以10的3次方



### 1.4类型转换

Python常用类型转换：

- str(obj)
- int(obj)
- float(obj)

示例代码：

```Python
>>> a = 10
>>> str(a)
'10'

>>> a = '10'
>>> int(a)
10

>>> a = '10.1'
>>> float(a)
10.1
>>> 
```



### 1.5 标识符与赋值号

​	标识符是任何一种高级编程语言必须使用的，主要用于变量名、类名和函数名等。“=”在一般编程语言中都是赋值符号，作用是 给变量赋值。

#### 1.5.1 标志符

​	Python规定的标识符只能以**字母**或者**下划线**开头，后面跟随**0个或多个非空字符、下划线或数字**，并且区分大小写。

#### 1.5.2 “=“

​	在其他编程语言中，赋值符号就是将右边的值赋给左边的变量。

​	在Python中，“=”的作用是将对象引用与内存中某对象进行绑定。如果对象存在，就进行简单的绑定，以便引用右边的对象；若对象不存在，就由“=”操作符创建对象并绑定。我们知道在Python中的一切即对象。

### 1.6 数字型总结

```Python
分类: 整数 浮点数  复数
整数: 
 
[重点]
int(): 转换成整数,不进行四舍五入
float(): 转换成浮点数
# 如果在数字字符串中夹杂一些无用的字符,程序直接会报错
# 总结1:以下内容全部报错
# 总结2:只要某一行代码宝报错,后边程序不再执行.
```



## 2 - Python结构数据类型

​	Python中的结构数据类型有很多，如字典、列表元祖等

### 2.1列表（list）

​	列表是以方括号“[]”包围的数据集合，不同成员之间以“,”分隔。列表中可以包含任何数据类型，也可以包含另一个列表。可以通过序号来访问其中的成员，从0开始。

**2.1.1列表基本操作**

```Python
>>> alist = list()   #创建一个空列表

>>> print(alist)
[]
>>> [1,]             #创建一个只有一个值的列表，可以在最后加“,”，也可以不加
[1]
>>> [1]             
[1]

>>> [1, 2, 3]        #创建一个有三个值的列表
[1, 2, 3]
>>> [1, 2, 3,]
[1, 2, 3]

>>> alist = ['a', 1, 'b', 4.6]   #列表中有不同的数据类型
>>> print(alist)
['a', 1, 'b', 4.6]
>>> alist[0]                     #取第一个元素，序号为0
'a'

>>> ['strs', 4] + [2, 'True']    #列表支持加法运算
['strs', 4, 2, 'True']  

>>> [None] * 7                   #列表支持乘法运算
[None, None, None, None, None, None, None]
>>> [1] * 10
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

#### 2.1.2列表的常用操作函数

<center>**表6 列表的常用操作函数**</center>

|                 方法                  |                             作用                             |
| :-----------------------------------: | :----------------------------------------------------------: |
|             lst.append(x)             |                  将元素x添加至列表lst的尾部                  |
|             lst.extend(L)             |             将列表L中的所有元素添加至列表lst尾部             |
|         lst.insert(index, x)          | 在列表lst指定位置index处添加元素x，该元素后面的所有元素后移一个位置 |
|             lst.remove(x)             | 在列表lst中删除首次出现的指定元素，该元素之后的所有元素前移一个位置 |
|           lst.pop([index])            | 删除并返回列表lst中下标为index（默认为-1，即列表尾部）的元素 |
|              lst.clear()              |           删除列表lst中的所有元素，但保留列表对象            |
|             lst.index(x)              | 返回列表lst中第一个值为x的元素的下标，若不存在值为x的元素则抛出异常 |
|             lst.count(x)              |              返回指定元素x在列表lst中的出现次数              |
|             lst.reverse()             |                  将列表lst所有元素进行逆序                   |
| lst.sort(key = None, reverse = False) | 对列表lst中的元素进行排序，key用来指定排序依据，reverse决定升序（False）还是降序（True） |
|              lst.copy()               |                     返回列表lst的浅复制                      |

示例代码：

```Python
>>> alist = [1, 't', 5]

#在列表后面添加一个元素
>>> alist.append(5)
>>> alist
[1, 't', 5, 5]

#把列表blist连接到alist后面
>>> blist = ['y', 7]
>>> alist.extend(blist)
>>> alist
[1, 't', 5, 5, 'y', 7]

#在列表指定位置插入一个元素
>>> alist.insert(1, '这是在第二个位置插入的元素')
>>> alist
[1, '这是在第二个位置插入的元素', 't', 5, 5, 'y', 7]

#删除列表中出现的第一个5，不存在则报错
>>> alist.remove(5)
>>> alist
[1, '这是在第二个位置插入的元素', 't', 5, 'y', 7]

#弹出列表的一个元素并输出，默认是尾部的第一个元素
>>> alist.pop()
7
>>> alist
[1, '这是在第二个位置插入的元素', 't', 5, 'y']

#弹出列表指定位置的元素并输出
>>> alist.pop(1)
'这是在第二个位置插入的元素'
>>> alist
[1, 't', 5, 'y']


>>> alist.append(5)
>>> alist
[1, 't', 5, 'y', 5]
#返回列表中第一个元素为5的下标
>>> alist.index(5)
2
#统计列表中共有多少个5
>>> alist.count(5)
2

#逆置列表
>>> alist.reverse()
>>> alist
[5, 'y', 5, 't', 1]


>>> clist = [1, 5, 2, 9, 0]
#对列表进行排序，默认升序
>>> clist.sort()
>>> clist
[0, 1, 2, 5, 9]

#参数reverse决定是升序还降序，True - 升序，False - 降序
>>> clist.sort(reverse=False)


>>> clist
[0, 1, 2, 5, 9]

#赋值clist并赋值给cp_clist
>>> cp_clist = clist.copy()
>>> cp_clist
[0, 1, 2, 5, 9]

#copy() - 潜复制 - 不改变原来的列表，把复制的列表复制给另一个变量，即地址。
>>> id(clist)
2332722665224
>>> id(cp_clist)
2332722663944

#清空列表
>>> clist.clear()
>>> clist
[]
```



### 2.2元祖（tuple）

​	元祖是一种特殊的列表，与列表不同的是元祖一旦建立就不能改变，既不能改变其中的元素，也不能添加和删除数据项。

​	基本形式是用圆括号“()”括起来的数据元素，也可以通过序号来引用其中的元素。

示例代码：

```Python
#创建空元祖
>>> atuple = tuple()
>>> atuple
()
>>> ()
()

#创建只有一个元素的元祖
>>> atuple = (1,)
>>> atuple
(1,)

#直接输入两个值也可以创建一个元祖
>>> 2, 3
(2, 3)

#右边是一个元祖，自动解压赋值给x，y
>>> x, y = 1, 2
>>> x
1
>>> y
2

#按序号取元祖的元素
>>> btuple = (1, 2, 4)
>>> btuple[0]
1

#交换x与y的值
>>> x, y = y, x
>>> x
2
>>> y
1
```

**注：和创建只有一个元素的列表不同，创建只有一个元素的元祖必须在元素后加一个“,”，否则就是一个值，如：**

```Python
>>> a = (1)
>>> a
1

>>> a = (1,)
>>> a
(1,)
```



### 2.3字典（set）

​	字典是比较特殊的数据类型，字典中的每个成员以“键：值”对得形式存在的。

​	字典以大括号“{}”包围的以“键：值”对方式声明和存在的数据集合。与列表最大的不同在于字典是无序的。字典中通过键来访问成员，而并不能通过为止来访问。

#### 2.3.1字典基本操作

代码示例：

```Python
#创建空字典
>>> {}
{}
>>> dict()
{}

#创建字典
>>> adict = {'a':1, 'b':2, 'c':3}
>>> adict
{'a': 1, 'b': 2, 'c': 3}

#通过键来访问元素
>>> adict['a']
1
>>> 
```

#### 2.3.2字典操作函数

<center>**表7 字典操作函数**</center>

|         字典操作          |                             描述                             |
| :-----------------------: | :----------------------------------------------------------: |
|        dic.clear()        |                           清空字典                           |
|        dic.copy()         |                           赋值字典                           |
|   dic.get(k, [default])   |             获得键k对应的值，不存在则返回default             |
|        dic.items()        |                   获得由键和值组成的迭代器                   |
|        dic.keys()         |                        获得键的迭代器                        |
|        dic.pop(k)         |                        删除k:v键值对                         |
|     dic.update(adict)     |       从另一个字典更新成员（不存在就创建，存在就覆盖）       |
|       dic.values()        |                        获得值的迭代器                        |
| dic.fromkeys(iter, value) |        以列表或元祖中给定的键建立字典，默认值为value         |
|       dic.popitem()       |                 从字典中删除一k:v项并返回它                  |
| dic.setdefault(k,default) | 若字典中存在key值为k的，则返回其对应的值；否则在字典中建立一个k:default字典成员 |

代码示例：

```Python
>>> dic = {'a':1, 'b':2}


>>> type(dic)      #字典类型                     
<class 'dict'>
>>> dic.get('a')   #获得键a的值
1
>>> dic.get('j')   #键不存在返回默认值
>>> dic['j']       #直接以键获取值，不存在抛出异常
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dic['j']
KeyError: 'j'


>>> dic.items()      #取得所有的键值对
dict_items([('a', 1), ('b', 2)])
>>> dic.keys()       #返回字典所有的键
dict_keys(['a', 'b'])


>>> dic.values()     #返回字典所有的值
dict_values([1, 2])
>>> dic.update({'a':3})  #用另一个字典（存在键）取更新dic字典
>>> dic
{'a': 3, 'b': 2}


>>> dic.update({'c':3})   #用另一个字典（不存在键）取更新dic字典
>>> dic
{'a': 3, 'b': 2, 'c': 3}


>>> dic.setdefault('a')   #存在键就返回值
3


>>> dic.setdefault('d',0) #不存在键就新建一个键值对
0


>>> dic
{'a': 3, 'b': 2, 'c': 3, 'd': 0}


>>> dic.pop('d')    #删除d并返回值
0
>>> dic
{'a': 3, 'b': 2, 'c': 3}
>>> dic.popitem()   #删除任意一项键值对并返回它
('c', 3)


>>> dic
{'a': 3, 'b': 2}
>>> dic.pop('d')   #删除不存在的键值对引发异常
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dic.pop('d')
KeyError: 'd'
```

### 2.4 集合

```Python
'''
set(集合):类似于dict, 也是无序的,以key-value新的形势存在,但是没有value
作用: 是对list,tuple,dict进行去重的, 求交集.并集
1.set是无序
2.set集合是不可改变的


'''

# set1 = set([1, 2, 3, 5, 3, 2])
# print(set1)
# print(type(set1))
# set2 = set((1, 2, 3, 5, 3, 2, 4, 5))
# print(set2)
# print(type(set2))
# set3 = set({3, 4, 5,5, 6, 3, 7})
# print(set3)
# print(type(set3))



# 添加
set4 = set([3, 3, 4, 5, 7, 2, 1, 2])
set4.add(8)
# set4.add(3)#可以添加重复的值,但是没效果

# 总结:list和dict是可改变的, 而tuple是不可改变
# set4.add([10, 9])#直接报错,不能添加list
# set4.add((10, 9))
# set4.add({'a':1})#直接报错,不能添加字典
#
# print(set4)



# 修改
set5 = set([1, 2, 3, 4, 5])
# 将list dict tuple 等等整个插入进去
# set5.update([6, 7, 8])
# set5.update({9, 10})
# set5.update((11, 56))
# print(set5)



# 删除
# set6= set([3, 4, 5, 6, 7])
# set6.remove(4)
# print(set6)

# 遍历
set7 = set([1, 2, 3, 4, 6])
set7 = set(['aaa', 'bbb', 'ccc'])
set7 = set((1, 2, 3, 2, 4, 2, 3))
# 在set集合中,没有value,即使有value也遍历不出来
set7 = set({'name':'小花', 'age': 18})
# for i in set7:
#     print(i, end = ',')



# 交集  &
set8 = set([1, 2, 3, 4])
set9 = set([3, 2, 4, 5])
set10 = set8 & set9
set11 = set8 | set9
print(set10)
print(type(set10))
print(set11)
print(type(set11))
```



## 3 - Python内置常量与逻辑运算符、比较运算符

​	在Python中，除了上面介绍的各种数据类型以及相关运算外，还有一些常用的内置常量和逻辑运算、比较运算符。

### 3.1常用内置常量

- None - 无，表示没有值对象。
- True（真）与False（假） - Python的逻辑 数据。

**注：Python中逻辑假包括False、None、0、“”、()、[]、和{}等。**

### 3.2逻辑运算符

与（and）、或（or）、非（not）。

1. not：运算对象只有一个，一般称为语言运算符规则为非假即真；非真即假。

   代码示例：

   ```Python
   >>> not True
   False
   
   >>> not [1,2]
   False
   
   >>> not []
   True
   
   >>> not 1
   False
   
   >>> not 0
   True
   ```

2. or：”或“运算符，两个参与运算的操作数又一个为真则结果为真，否则结果为假。它是一种短路运算符，并且总是返回决定运算结果的参与运算得操作数。其运算处理过程是这样的：**如果第一个操作数或表达式为真则直接返回第一个操作数，而不是处理第二个操作数或表达式；如果第一个操作数或表达式为假则返回第二个操作数或表达式的值。**

   示例代码：

   ```Python
   >>> 1 or 0   #第一个操作数为1，为真，所以直接返回1，结果为真
   1
   
   >>> 0 or False  #第一个操作数0为假，直接返回第二个操作数
   False
   
   >>> [1, 3] or [2, 4]  #第一个操作数为真，直接返回[1, 3]
   [1, 3]
   >>> print(1 or 0)
   1
   
   >>> [] or ()    #第一个操作数[]为假，直接返回第二个操作数()
   ()
   ```

3. and：“与”运算符，两个参与运算的操作数都为真，则结果为真，否则结果为假。也是一种短路运算符，并且总是返回决定运算结果的参与运算的操作数，运算处理过程是这样的：**如果第一个操作数或者表达式为假则直接返回第一个操作数，而不处理第二个操作数或表达式；如果第一个操作数或者表达式为真则返回第二个操作数或表达式的值。**

   ```Python
   >>> [] and 1
   []
   
   >>> 1 and []
   []
   
   >>> 1 and 7*2
   14
   ```

### 3.3比较运算符

<center>**表8 比较运算符**</center>

| 运算符 |   意义   |
| :----: | :------: |
|   ==   |   相等   |
|   >    |   大于   |
|   <    |   小于   |
|   >=   | 大于等于 |
|   <=   | 小于等于 |
|   !=   |  不等于  |

### 3.4其他逻辑运算符

#### 3.4.1 is和not

​	is和is not都是二元操作符，用于判断左端与右端对象引用是否指向同一个对象。对于is操作符，相同则返回True，不同则返回False；is not操作符相反。

代码示例：

```Python
>>> x = 4

>>> y = x
>>> x is y     #x、y引用同一个对象，结果为True
True

>>> x is None
False

>>> x is not y
False
```

#### 3.4.2 in和not in

​	in和not in称为成员运算符，用于检查某个数据是否存在于某包含多个成员的数据类型（如字符串、列表、元祖、字典等）之中。如果是成员关系，则in返回真；否则返回假；而not in则相反。

代码示例：

```Python
>>> lst1 = [1, 2, 3]
>>> 1 in lst1
True

>>> lst2 = ['a', 'b', 'c']
>>> 'a' in lst2
True

>>> 'a' in 'afrgrgr'
True

>>> dit = {'a':1, 'b':2}
>>> 'a' in dit      #键'a'属于dit键成员
True
>>> 1 in dit         #1是字典中的值，不是键成员
False
```

### 3.3序列

​	序列表示索引为非负整数的**有序**对象集合，包含前面的字符串、列表和元祖。字符串是字符的序列，列表和元祖则是任意Python数据类型或对象的序列。元祖不可变，字符串也是不可变的。

#### 3.3.1序列切片

​	对于任何一个序列，他们的元素都是**有序**的，都可以使用序号来获取每一项成员的值。Python中序列的序号既可以从左至右从0开始计数，又可以从右至左从-1开始计数。如图1所示：

![](C:\Users\lsmil\Documents\Python Knowledge\images\1.png)

<center>**图1 序列序号图<**/center>

代码示例：

```Python
>>> alist = [1, 4, 3, 7, 8]
>>> alist[0]
1
>>> alist[-1]
8
```

​	序列的切片是指用形如[开始：结束：步长]来去序列中的部分成员数据项。从开始位置到**结束位置的前一个结束**，每隔步长去一个成员。

<center>**表9 切片常用方法**</center>

|   使用形式   |                 意义                 |
| :----------: | :----------------------------------: |
|   alst[:]    |           取全部成员数据项           |
|   alst[0:]   |           取全部成员数据项           |
|  alst[:-1]   | 取除最后一个成员之外的所有成员数据项 |
|  alst[2:5]   |         开始位置2，结束位置5         |
|  alst[::2]   |        从0到整个长度，步长是2        |
| alst[0:5:2]  |           从0到5，步长是2            |
|  alst[::-1]  |          从右向左取全部成员          |
| alst[5:0:-2] |        从右到左隔一个取一个值        |

代码示例：

```Python
>>> alst = [1, 3, 5, 2, 1, 9, 0]


>>> alst[:]
[1, 3, 5, 2, 1, 9, 0]

>>> alst[0:]
[1, 3, 5, 2, 1, 9, 0]

>>> alst[:-1]
[1, 3, 5, 2, 1, 9]

>>> alst[-1]
0

>>> alst[2:5]
[5, 2, 1]

>>> alst[::2]
[1, 5, 1, 0]

>>> alst[0:5:2]
[1, 5, 1]

>>> alst[::-1]
[0, 9, 1, 2, 5, 3, 1]

>>> alst[5:0:-2]
[9, 2, 3]
```

#### 3.3.2序列内置操作

<center>**表10 序列操作方法**</center>

|       方法       |               操作                |
| :--------------: | :-------------------------------: |
|      len(s)      |      返回s的长度（元素个数）      |
|      min(s)      |           返回s中最小值           |
|      max(s)      |           返回s中最大值           |
| sum(s[,element]) | 返回s中各项的和（再加上element）  |
|      all(s)      |   s中所有项则返回真，否则返回假   |
|      any(s)      | s中有一项为真则返回真，否则返回假 |

代码示例：

```Python
>>> s = [1, 3, 4, 4, 2]


>>> len(s) #长度
5

>>> min(s) #最小值
1

>>> max(s) #最大值
4

>>> sum(s) #所有元素的和
14
>>> sum(s, 10) #所有元素的和加上10
24

>>> all(s)
True

>>> any(s)
True

>>> s = ['', 4]


>>> all(s)
False

>>> any(s)
True
```



## 4 - 小结

​	本文档主要讲述了Python的简单数据类型和结构数据类型，简单数据类型如整数、浮点数、字符串，结构数据类型如列表、元祖、和字典。以及讲了他们之间的类型转换、参与的运算和函数方法，另外还包括标识符、常用内置常量、逻辑运算等内容。