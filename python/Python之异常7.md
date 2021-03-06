# 异常与程序调试

> [TOC]
>
> 



## 1 - 语法错误

1. 拼写错误

   即Python语言中的关键字写错，变量名、函数名拼写错误等。

   关键字拼写错误会提示**SyntaxError**（语法错误），而变量名、函数名写错会在运行时给出**NameError**的错误提示。

2. 脚本程序不符合Python的语法规范

   如少了括号、冒号等符号，以及表达式书写错误等。

3. 缩进错误

   Python代码之所以清晰，便于阅读，正是因为它有严格的缩进规范。一般来说Python标准的缩进是4个空格作为一个缩进。当然也可以根据自己的习惯使用Tab。但是同一个程序或者项目中应该使用同一缩进风格。

## 2 - 异常处理

​	当程序在运行中引发异常或错误时，程序会由于异常而终止。只有在程序中捕获这些异常，并进行相关处理，才能使程序不会中断运行。

### 2.2 异常处理的基本语法

​	Python中使用try语句来处理异常，一般try语句基本形式如下：

**try:**

​    **<语句块>**                       #可能产生异常的语句块

**except <异常名1>: **              #要处理的异常

​    **<语句块>**

**except <异常名2>:**            #要处理的异常

​    **<语句块>**

**….**

**else:**
    **<语句块> **                        #未触发异常则执行此语句块

**finally: **                                    #无论是否发生异常都执行的语句块，一般为了释放资源等

​    **<语句块>**

以上一句执行的流程图：

![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/7-1.png)

**注：else语句块在未引发异常情况下得到运行。**

异常的常用形式

- **形式一**

  **try:**

  ​    **<语句块>**

  **except <异常名1>:**

  ​    **<语句块>**

- **形式二**

  **try:**

  ​    **<语句块>**

  **except <异常名1>:**

  ​    **<语句块>**

  **finally:**

  ​    **<语句块>**

### 2.3 Python主要的内置异常及其处理

​	常用的预定义异常如下表。

<center>**表1 常用异常名**</center>

|      异常名       |                描述                |
| :---------------: | :--------------------------------: |
|  AttributeError   |     调用不存在的方法引发的异常     |
|     EOFError      |       遇到文件末尾引发的异常       |
|    ImportError    |       导入模块错误引发的异常       |
|    IndexError     |         列表越界引发的异常         |
|      IOError      |         I/O操作引发的异常          |
|     KeyError      | 使用字典中不存在的关键字引发的异常 |
|     NameError     |    使用不存在的变量名引发的异常    |
|     TabError      |      语句缩进不正确引发的异常      |
|    ValueError     |    搜索列表不存在的值引发的异常    |
| ZeroDivisionError |         除数为零引发的异常         |

Python标准异常类

<center>**表2 Python标准异常类**</center>

|         异常名称          |                        描述                        |
| :-----------------------: | :------------------------------------------------: |
|       BaseException       |                   所有异常的基类                   |
|        SystemExit         |                   解释器请求退出                   |
|     KeyboardInterrupt     |             用户中断执行(通常是输入^C)             |
|         Exception         |                   常规错误的基类                   |
|       StopIteration       |                 迭代器没有更多的值                 |
|       GeneratorExit       |        生成器(generator)发生异常来通知退出         |
|        SystemExit         |               Python 解释器请求退出                |
|       StandardError       |              所有的内建标准异常的基类              |
|      ArithmeticError      |               所有数值计算错误的基类               |
|    FloatingPointError     |                    浮点计算错误                    |
|       OverflowError       |                数值运算超出最大限制                |
|     ZeroDivisionError     |            除(或取模)零 (所有数据类型)             |
|      AssertionError       |                    断言语句失败                    |
|      AttributeError       |                  对象没有这个属性                  |
|         EOFError          |             没有内建输入,到达EOF 标记              |
|     EnvironmentError      |                 操作系统错误的基类                 |
|          IOError          |                 输入/输出操作失败                  |
|          OSError          |                    操作系统错误                    |
|       WindowsError        |                    系统调用失败                    |
|        ImportError        |                 导入模块/对象失败                  |
|     KeyboardInterrupt     |             用户中断执行(通常是输入^C)             |
|        LookupError        |                 无效数据查询的基类                 |
|        IndexError         |            序列中没有没有此索引(index)             |
|         KeyError          |                  映射中没有这个键                  |
|        MemoryError        |     内存溢出错误(对于Python 解释器不是致命的)      |
|         NameError         |            未声明/初始化对象 (没有属性)            |
|     UnboundLocalError     |               访问未初始化的本地变量               |
|      ReferenceError       | 弱引用(Weak reference)试图访问已经垃圾回收了的对象 |
|       RuntimeError        |                  一般的运行时错误                  |
|    NotImplementedError    |                   尚未实现的方法                   |
|        SyntaxError        |                  Python 语法错误                   |
|     IndentationError      |                      缩进错误                      |
|         TabError          |                   Tab 和空格混用                   |
|        SystemError        |                一般的解释器系统错误                |
|         TypeError         |                  对类型无效的操作                  |
|        ValueError         |                   传入无效的参数                   |
|       UnicodeError        |                 Unicode 相关的错误                 |
|    UnicodeDecodeError     |                Unicode 解码时的错误                |
|    UnicodeEncodeError     |                 Unicode 编码时错误                 |
|   UnicodeTranslateError   |                 Unicode 转换时错误                 |
|          Warning          |                     警告的基类                     |
|    DeprecationWarning     |               关于被弃用的特征的警告               |
|       FutureWarning       |           关于构造将来语义会有改变的警告           |
|      OverflowWarning      |        旧的关于自动提升为长整型(long)的警告        |
| PendingDeprecationWarning |              关于特性将会被废弃的警告              |
|      RuntimeWarning       |      可疑的运行时行为(runtime behavior)的警告      |
|       SyntaxWarning       |                  可疑的语法的警告                  |
|        UserWarning        |                 用户代码生成的警告                 |

Python异常结构图：

![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/7-2.png)

except语句的语法：

- except:#捕获所有异常；
- except <异常名>:捕获指定异常；
- except (异常名1, 异常名2):#捕获异常名1或者异常名2；
- except <异常名> as <数据>:#捕获指定异常及其附加数据；
- except (异常名1， 异常名2) as <数据>:#捕获异常名1或者异常名2及异常的附加数据。

代码示例：

```Python
def testTryAll(index, i):
    stulst = ("John", "Jenny", "Tom")
    try:
        print(len(stulst[index])/i)
    except:
        print("Error")
    
testTryAll(1, 2)
testTryAll(1, 0)
testTryAll(4, 0)
"""
2.5
Error
Error
"""
```

### 2.4 手动抛出异常

​	Python程序中使用raise语句来引发指定的异常，并向异常传递数据。

#### 2.4.1 raise手工抛出异常

形式：

**raise 异常名**

**raise 异常名,附加数据**

**raise 类名**

代码示例1：

```Python
def testRaise():
    for i in range(5):
        if i == 2:
            raise NameError
        print(i)
    print('end...')
    
testRaise()
"""
0
Traceback (most recent call last):
1
  File "D:/PyCharm/code/projects/python35/exam.py", line 8, in <module>
    testRaise()
  File "D:/PyCharm/code/projects/python35/exam.py", line 4, in testRaise
    raise NameError
NameError


当循环变量i为2时，抛出NameError异常，因为没有处理该异常而导致程序运行中断，后面所有的输出都得不到执行。
"""
```

示例代码2：

```Python
def testRaise2():
    for i in range(5):
        try:
            if i ==2:
                raise NameError
        except NameError:
            print('Raise a NameError!')
        print(i)
    print('end...')

testRaise2()

"""
0
1
Raise a NameError!
2
3
4
end...

当循环变量为2时抛出NameError异常，但是这个异常引发会被捕捉，程序就不会中断，后面的所有输出都得到执行。
"""
```

#### 2.4.2 assert语句

形式

**assert <条件测试>,<异常附加数据>**                         #异常附加数据是可选的

assert语句是简化的raise语句，它引发异常的前提是其后面的条件测试为假。

代码示例：

```Python
def testAssert():
    for i in range(3):
        try:
            assert i<2
        except AssertionError:
            print('Raise a AssertionError')
        print(i)
    print('end...')

testAssert()
"""
0
1
Raise a AssertionError
2
end...

当循环变量i为2 时，assert后的条件测试会变为假，抛出AssertError异常，但是这个异常引发会被捕捉，程序不会中断，后面的输出得到执行。
"""
```

### 2.5 自定义异常类

​	Python中自定义异常类只要通过继承Exception类来创建自己的异常类。下面是一个简单的示例：

```Python
class MyError(Exception):
    pass
```

如果需要异常类带有一定的提示信息，可以重载\_\_init\_\_和\_\_str\_\_两个方法

代码示例：

```Python
class ErrorTest(Exception):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value

raise ErrorTest('发生了错误')
"""
Traceback (most recent call last):
  File "D:/PyCharm/code/projects/python35/exam.py", line 9, in <module>
    raise ErrorTest('发生了错误')
__main__.ErrorTest: 发生了错误
"""
```

