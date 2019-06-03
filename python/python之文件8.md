# 文件

> [TOC]
>
> 



## 1 - 打开文件

Python中打开文件用open方法:

- 基本语法：**open(file_name, \[, access_mode][, buffering])**

- 参数：

  - file_name：包含要访问的文件名称的字符串值；

  - access_mode：打开文件的模式，如只读，写入和追加等。默认为只读（r）；、
  - buffering：
    1. 0：没有寄存；
    2. 1：访问文件有寄存；
    3. \>1：寄存区的缓冲大小；
    4. \<0：寄存去的缓冲大小就是系统默认值。

- 返回值：open函数返回一个File（文件）对象。

- 示例：

  ```Python
  path = 'd:/test.txt'
  f_name = open(path)
  print(f_name.name)
  
  """
  结果
  d:/test.txt
  """
  ```

**补充：文件路径**

- 绝对路径：总是从根文件夹开始；
- 相对路径：相对于程序当前工作目录的路径。



### 1.1 打开文件的模式

| 模式 |                             描述                             |
| :--: | :----------------------------------------------------------: |
|  r   | 以**只读**的方式打开文件。文件的指针放在文件的开头，这是**默认模式** |
|  rb  | 以**二进制格式**打开文件用于**只读**。文件指针在文件开头，这是**默认模式** |
|  r+  |        打开一个文件用于**读写**，文件的指针在文件开头        |
| rb+  | 以**二进制格式**打开一个文件用于**读写**，文件的指针会放在文件的开头 |
|  w   | 打开一个文件**只用于写入**。如果文件已经存在就将其覆盖；否则就创建新文件 |
|  wb  | 以**二进制格式**打开一个文件**只用于写入**。如果文件存在就将其覆盖；否则创建 |
|  w+  |  打开一个文件用于**读写**。如果文件存在就将其覆盖；否则创建  |
| wb+  | 以**二进制格式**打开一个文件用于**读写**。如果文件存在就将其覆盖；否则创建 |
|  a   | 打开一个文件用于**追加**。如果文件存在，文件的指针就会放在文件的结尾。即新内容会被写在已有内容之后。如果文件不存在就创建新文件进行写入 |
|  ab  | 以**二进制格式**打开一个文件用于**追加**。如果文件存在，文件的指针就会放在文件的结尾。即新内容会被写在已有内容之后。如果文件不存在就创建新文件进行写入 |
|  a+  | 打开一个文件用于**读写**。如果文件存在文件的指针将会放在文件的结尾。即新内容会被写在已有内容之后。如果文件不存在就创建新文件进行写入 |
| ab+  | 以**二进制格式**打开一个文件用于**追加**。如果该文件已经存在，文件指针将会放在文件结尾；如果该文件不存在，创建新文件就用于读写。 |

### 1.2 缓冲

​	open函数的第三个参数是可选的，该函数控制文件的缓存。如果该参数赋值为0或者False，I/O(输入/输出)就是无缓存的。如果是1或Ture，I/O就是由缓存的。大于1 的整数就是缓存的大小（单位字节），-1或者小于0的整数代表使用默认的缓存大小。

## 2 - 基本文件方法

### 2.1 流

​	I/O编程中，Stream（流）是一个很重要的概念。可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。浏览网页时，浏览器和服务器之间至少需要建立两根水管，才能发送数据和接受数据。

### 2.2 读和写

open函数返回的是一个File对象，有了File对象就可以开始读取内容。

**相关方法**

- **read()**

  1. 描述：该方法从文件的开头开始读入，如果没有传入参数count，就会尝试尽可能多地读取内容，可能一直读到文件末尾。

  2. 语法形式：**fileobject.read([count])**

  3. 参数：

     count：是从已打开的文件中读取的字节计数。

  4. 代码：

     ```Python
     '''
     test.txt中的内容：
     hello
     felix
     nihao
     '''
     # 代码段1
     path = 'd:/test.txt'
     f_name = open(path, 'r')
     print(f_name.read(4))    # 第一次读取4个字节
     print(f_name.read(5))    # 第二次从第一次结束的地方继续读5个字节
     print(f_name.read(6))    # 第三次从第二次结束的地方继续读6个字节
     
     '''
     结果
     hell
     o
     fel
     ix
     nih
     '''
     
     #代码段2
     path = 'd:/test.txt'
     f_name = open(path, 'r')
     print(f_name.read())              #读取了全部内容
     '''
     结果
     hello
     felix
     nihao
     '''
     ```

     **注：打开文件，在文件未关闭的情况下是继上一次读的结束的位置继续读取的。并且换行也作为一个字符被当成是读取的内容。**

- **write()**

  1. 描述：向一个文件写入数据。write()方法可将任意字符串写入一个打开的文件。注意，Python字符串可以是二进制数据，不仅仅是文字；

  2. 语法形式：**fileObject.write(string)**；

  3. 参数：string要写入文件的内容；

  4. 返回值：**写入文件的字符串的长度；**

  5. 代码：

     ```Python
     path = 'D:/test.txt'
     f_name = open(path, 'w')
     print(f_name.write('hello'))
     f_name = open(path, 'r')
     print(f_name.read())
     
     '''
     结果
     5
     hello
     '''
     ```

     **注：写文件方法的处理方式是：将覆盖原有文件，从头开始，每次写入都会覆盖前面所有的内容。**如果要在当前字符串后面追加字符，可用a模式，即追加模式打开文件。代码：

     ```Python
     path = 'D:/test.txt'
     # 先看文件的内容
     f_name = open(path, 'r')
     print(f_name.read())
     # 以追加方式写入文件
     f_name = open(path, 'a')
     print(f_name.write('liuxiao'))
     # 再打开文件查看内容
     f_name = open(path, 'r')
     print(f_name.read())
     '''
     结果
     hello
     7
     helloliuxiao
     '''
     ```

     **注：**

     1. **以a方式写入文件，返回值是追加到文件的字符数。**
     2. **如果传递给open函数的文件名不存在，写模式（w）和追加模式（a）就会创建一个空文件，然后执行写入或者追加。**

     如果要追加在文件的下一行，则：

     ```Python
     path = 'D:/test.txt'
     # 先看文件的内容
     f_name = open(path, 'r')
     print(f_name.read())
     # 以追加方式写入文件
     f_name = open(path, 'a')
     # 追加在已有文件的下一行，加'\n'
     print(f_name.write('\nliuxiao'))
     # 再打开文件查看内容
     f_name = open(path, 'r')
     print(f_name.read())
     '''
     结果
     hello
     8
     hello
     liuxiao
     '''
     ```

**提示**：若要读写特定编码方式的文本，则需要给open函数传入encoding参数；若需要读取GBK文件，则：

```Python
f_name = openn(path, 'r', encoding='gbk')
```

这样读取到的文件就是GBK编码方式的文件了。

### 2.3 读写行

- **readline()**

  代码：

  ```Python
  path = 'D:/test.txt'
  f_name = open(path, 'r')
  # 先看文件内容
  print(f_name.read())
  f_name.close()
  # 再打开
  f_name = open(path, 'r')
  # 读取一行
  print(f_name.readline())
  
  '''
  结果
  hello
  liuxiao
  hello
  (\n)
  '''
  ```

  **注：该方法从文件中读了一行，并且还读了末尾的换行符，所以输出的内容会多一行。**

  如果还不清楚，可以验证一下，看它读了几个字符：

  ```Python
  path = 'D:/test.txt'
  f_name = open(path, 'r')
  # 先看文件内容
  print(f_name.read())
  f_name.close()
  # 再打开
  f_name = open(path, 'r')
  # 读取一行
  print(len(f_name.readline())
        
  '''
  结果
  hello
  liuxiao
  6
  '''
  ```

  ‘hello’是5个字符，可是读的长度是6个，可见，是读了换行符的。

  ```Python
  path = 'D:/test.txt'
  f_name = open(path, 'r')
  # 先看文件内容
  print(f_name.read())
  f_name.close()
  # 再打开
  f_name = open(path, 'r')
  # 读取一行
  print(f_name.readline())
  # 读到最后一行，由于最后一行没有下一行了，所以就没有换行符
  # 虽然在输出上看是多了一行，那是因为print()函数本身就自动换行。
  print(len(f_name.readline()))
  # 已经全部读完后再读，这时就会返回空字符串
  print(f_name.readline())
  print(len(f_name.readline()))
  
  '''
  hello
  liuxiao
  hello
  
  7
  
  0
  '''
  ```

  readline()函数和read()函数方法一样传入数值读取对应的字符串，传入小于0的数值表示整行都输出

  ```Python
  path = 'D:/test.txt'
  f_name = open(path, 'r')
  # 先看文件内容
  print(f_name.read())
  f_name.close()
  # 再打开
  f_name = open(path, 'r')
  # 读取一个字符
  print(f_name.readline(1))
  # 由于上面只读取一个字符，这一行还没有读完，所以继续读完上一行
  print(f_name.readline())
  # 传入的值是负数，则读整行
  print(f_name.readline(-2))
  
  '''
  hello
  liuxiao
  h
  ello
  
  liuxiao
  '''
  ```

- **readlines()**

  ```Python
  path = 'D:/test.txt'
  f_name = open(path, 'r')
  # 先看文件内容
  print(f_name.read())
  f_name.close()
  # 再打开
  f_name = open(path, 'r')
  # 读取全部，且把每一行的都存放在列表里，换行符也在内
  print(f_name.readlines())
  
  '''
  hello
  liuxiao
  ['hello\n', 'liuxiao']
  '''
  ```

  有关readlines()中传入的参数的讨论：

  ```Python
  path = 'D:/test.txt'
  f_name = open(path, 'w')
  content = ['hello\n', 'world\n']
  # writelines()函数一次写入多行内容
  print(f_name.writelines(content))
  f_name.close()
  
  f_name = open(path, 'r')
  # 读取内容
  print(f_name.read())
  
  f_name = open(path, 'r')
  # 全部读取
  print(f_name.readlines())
  
  f_name = open(path, 'r')
  # 参数小于或等于（这里不包括换行符）列表中一个字符串长度，该字符串会被读取
  print(f_name.readlines(2))
  
  f_name = open(path, 'r')
  # 传入参数小于0， 所有字符都会被读取
  print(f_name.readlines(-2))
  
  f_name = open(path, 'r')
  # 6这个长度，（不包括换行符）大于第一行字符串的长度，所以这时已经把第一行的全部读取了
  # 还剩一个字符读到下一行时小于下一行的长度，则全部读取。
  print(len(f_name.readlines()))
  
  f_name = open(path, 'r')
  print(len(f_name.readlines(6)))
  
  '''
  None
  hello
  world
  
  ['hello\n', 'world\n']
  ['hello\n']
  ['hello\n', 'world\n']
  2
  '''
  ```


### 2.4 关闭文件

```Python
path = 'D:\test.txt'
f_naem = open(path, 'r')
# 关闭文件
f_name.close()
```

文件的读取过程中经常会出现异常，我们最好显示关闭文件，我们可以使用finally，保证最后一定将文件关闭。

```Python
path = 'D:\test.txt'
try:
    f_name = open(path, 'w')
    print(f_name.write('hello'))
finally:
    if f_name:
        f_name.close()
```

可是每次写都麻烦，我们可以使用with语句

```Python
path = 'D:\test.txt'
with open(path, 'w') as f:
    print(f.write('hello'))
```

### 2.5 文件重命名

- **os.rename(filename)**

  ```Python
  import os
  
  path1 = 'D:/t.txt'  # 要重命名的文件
  path2 = 'D:/test/tt.txt'  # 重命名后的文件
  
  os.rename(path1, path2)
  ```

  **注：重命名后的文件将代替原来的文件，执行代码后原来位置的文件将不存在，新的文件被建在新的文件位置，和新的名称。**

### 2.6 删除文件

- **os.remove(filename)**

  ```Python
  import os
  
  path2 = 'D:/test/tt.txt'
  
  os.remove(path2)
  ```

  

## 3 - 对文件内容进行迭代

### 3.1 按字节处理

- **read([count])**

```Python
path = 'D:/test.txt'
f_name = open(path, 'w')
print(f_name.write('hello_world.'))
f_name = open(path)
# 用while循环进行
while True:
    c_str = f_name.read(1)
    if not c_str:
        break
    print(c_str)
f_name.close()

'''
12
h
e
l
l
o
_
w
o
r
l
d
.
'''
```

### 3.2 按行操作

- **readline([count])**

  ```Python
  path = 'D:/test.txt'
  f_name = open(path, 'r')
  print(f_name.read())
  f_name.close()
  f_name = open(path)
  while True:
      line = f_name.readline()
      if not line:
          break
      print(line)
  f_name.close()
  
  '''
  hello_world.
  felix
  hello_world.
  
  felix
  '''
  ```

- **fileinput**

  ```Python
  import fileinput
  
  path = 'D:/test.txt'
  
  for line in fileinput.input(path):
      print(line)
  
  '''
  hello_world.
  
  felix
  '''
  ```

  **注：文件的打开与关闭操作都被封装在input()方法内部了。**

### 3.3 文件迭代器

直接在for循环中使用文件对象，进行迭代

```Python
path = 'D:/test.txt'
f_name = open(path)

for line in f_name:
    print(line)
    
'''
hello_world.

felix
'''
```



## 4 - 递归

```
三要素:
1.写出临界条件
2.返回上一级和下一级之间的关系
3.根据上一次计算出的结果求出本次计算的结果
```

代码：

```Python
def test(n):
    while n > 0:
        print('%d' % n)
        n -= 1
        test(n)
test(10)
```

### 4.1 递归目录

```Python
import os
'''
getAllDir(path, str = '')
path: 文件路径
str: 路径字符串
'''
# 实现目录的遍历
def getAllDir(path, str = ''):
    # 返回一个指定文件夹(目录)包含文件和文件夹(目录),并且返回一个列表,但是不包含.和..,他一般按照英文首字母排序
    fillAll = os.listdir(path)
    print(fillAll)
    str += '.'
    for filename in fillAll:

        # 一定不能少了全路径的拼接
        filePath = os.path.join(path, filename)
        # print(filePath)

        # 判断filePath是否是目录
        if os.path.isdir(filePath):
            print(str + '文件夹' + filename)
            # filePath是目录
            getAllDir(filePath, str)
        else:
            # filePath不是目录,即是文件
            print(str + '文件:' + filename)


getAllDir('D:/pycharm/')
```

**4.1.1 使用栈模拟递归遍历目录**

```Python
import os
def getALLDir(path):
    list1 = []
    list1.append(path)
    # print(list1)

    while len(list1) != 0:
        # 开始从列表中取数据
        dirPath = list1.pop()
        # print(dirPath)
        # 得到文件下边的所有文件路径
        filesAll = os.listdir(dirPath)

        # print(filesAll)

        for filename in filesAll:
            # 路径拼接全路径
            filePath = os.path.join(dirPath, filename)
            if os.path.isdir(filePath):
                # 是目录
                list1.append(filePath)

            else:
                # 是文件
                print('文件' + filename)
```

**4.1.2 使用队列模拟递归遍历目录**

```Python
import os
import collections

def getAllDir(path):
    # 创建列表
    # 使用collections.deque方法可以创建一个两端都可以操作的列表,也就是说我们可以在两端进行添加和删除
    que = collections.deque()
    que.append(path)
    # print(que)

    while len(que) != 0:
        # 得到文件路径
        dirPath = que.popleft()

        # 获取该路径下边的文件和文件夹
        filesPath = os.listdir(dirPath)

        for filename in filesPath:
            # 拼接全路径
            filePath = os.path.join(dirPath, filename)

            if os.path.isdir(filePath):
                # 是目录
                que.append(filePath)
            else:
                # 是文件
                print('文件' + filename)

getAllDir('../test')
```



## 5 - StringIO与BytesIO

### 5.1 StringIO

```python
'''
StringIO:就是在内存中读写str
通常我们一般写内容实在内文件来写.
使用StringIO会比在文件中操作内容速度快一些
'''
from io import StringIO

# # 创建StringIO的对象
# f = StringIO()
# # print(f)
#
# value = f.write('hongfenghuang,fenfenghuang,hongfenfenghuang')
# # 有返回值: 返回str的长度
# # print(value)
#
# value = f.write(' ')
#
# value = f.write('nani')

# print(f.getvalue())




f = StringIO('hongfenghuang\nfenfenghuang\nhongfenhongfenghuang\n')

# print(f)
while 1:
    str = f.readline()
    if str == '':
        break
    print(str.strip())

```

### 5.2 BytesIO

```python
'''
StringIO只能操作str,那如果要操作二进制,则需要BytesIO

'''
from io import BytesIO

# f = BytesIO()
# # print(f)
#
# # 一个汉字表示三个字节
# value = f.write('刘海艳'.encode('utf-8') )
# print(value)

# print(f.getvalue())


f = BytesIO(b'\xe5\x88\x98\xe6\xb5\xb7\xe8\x89\xb3')
print(f.read().decode())


```

```python
from io import BytesIO

f = BytesIO()

str = '曾经错过的就别再珍惜了因为后面还有更好的也就只能这么安慰自个了'
# 一个汉字表示两个字节
value = f.write(str.encode('gbk'))
# print(value)
# print(f.getvalue())
# 将指针指向内容的开始
f.seek(0)
print(f.read().decode('gbk'))


f1 = BytesIO()
value = f1.write(str.encode('utf-8'))
# print(value)
# print(f1.getvalue())
# 将指针指向内容的开始
f1.seek(0)
print(f1.read().decode('utf-8'))
```

## 6 - csv文件操作

```python
'''
csv是跨多种形式的导入导出的标准格式 比如: mysql excel

它是一种一纯文本形式来存储数据.文件中的每一行代表一条数据.每条记录包含逗号分隔
'''

#读取csv 文件
import csv
def readCsv(path):
    list1 = []
    with open(path, 'r', encoding='gbk') as f:
        # print(f)
        result = csv.reader(f)
        # print(result)
        # 遍历可以遍历列表,还可以遍历对象
        for row in result:
            # 每次遍历一行,结果是一个列表
            # print(row)
            list1.append(row)

    return list1

path = r'test.csv'
# info = readCsv(path)
# print(info)




# 往csv中写内容
def WriteCsv(path, data):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        print(data)
        # for row in data:
        #     print('row =', row)
        #
        #     # 往文件中写内容
        #     writer.writerow(row)
        writer.writerows(data)







path = r'write.csv'
data = [[1, 2, 4, 5], [3, 4, 5, 6], [6, 7, 8, 9], [10, 2, 3, 4]]

WriteCsv(path, data)
```



## 7 - 序列化与反序列化

​	在程序运行过程中所有的变量都在内存中，我们把变量从内存中变成可存储或传输的过程称为**序列化**。我们可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。反过来，把变量内容从序列化的对象重新读到内存里称为**反序列化**。

```
序列化 - 将数据结构或对象转换成二进制串的过程；
反序列化 - 将序列化过程中生成的二进制串转换成数据结构或二进制串的过程。
```

## 7.1 一般序列化与反序列化

Python的pickle模块实现了基本数据序列与反序列化。通过pickle模块的序列化操作，能够将程序中运行的对象保存到文件中，从而永久存储。通过pickle的反序列化操作，能够从文件中创建上一次程序保存的对象。

- pickle模块

```Python
# 导入pickle模块
import pickle
# 将dumps(obj)返回的字节存储在变量中
dic = {'name':'felix', 'age':12}
# 变成二进制
byte_data = pickle.dumps(dic)
print(byte_data)

# 读取数据
# 数据以字节保存在了byte_data变量中，需要再次使用的时候使用loads函数
obj = pickle.loads(byte_data)
print(obj)

# 存储在文件中
# 也可以存储在文件中，是的对象持久化。使用dump()和load()函数。
# 由于pickle写入的二进制数据，所以打开方式需要以wb和rb方式

#序列化
with open('D:/file.txt', 'wb') as f:
    dic = {'name':'felix', 'age':12}
    pickle.dump(dic, f)
# 反序列化
with open('D:/file.txt', 'rb') as f:
    a = pickle.load(f)
    print(a)
    print(type(a))

'''
b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x05\x00\x00\x00felixq\x02X\x03\x00\x00\x00ageq\x03K\x0cu.'
{'name': 'felix', 'age': 12}
{'name': 'felix', 'age': 12}
<class 'dict'>
'''
```

- 序列化用户自定义模块

  ```Python
  import pickle
  
  # Person类
  class Person(object):
      def __init__(self, name, age, job):
          self.name = name
          self.age = age
          self.job = job
  
      def work(self):
          print(self.name, 'is working...')
  
  # pickle模块不仅可以写入类本身，也能写入它的一个参数
  
  # 将实例存储在变量中，当然也能存在文件中
  a_person = Person('abc', 22, 'waiter')
  person_abc = pickle.dumps(a_person)
  p = pickle.loads(person_abc)
  p.work()
  # 将类本身存储在变量中，loads的时候返回类本身，而非它的一个实例
  class_Person = pickle.dumps(Person)
  Person = pickle.loads(class_Person)
  p = Person('Bob', 23, 'Student')
  p.work()
  
  # 下面这个例子演示的就是将类存储在文件中
  # 序列化
  with open('D:/file.txt', 'wb') as f:
      pickle.dump(Person, f)
  # 反序列化
  with open('D:/file.txt', 'rb') as f:
      Person = pickle.load(f)
      aa = Person('gg', 23, '6')
      aa.work()
  
  '''
  abc is working...
  Bob is working...
  gg is working...
  '''
  ```

- json模块

  ​	pickle可以很方便地序列化所有对象。不过json作为更为标准的格式，具有更好的可读性（pickle是二进制数据）和跨平台性。是个不错的选择。

  json使用的四个函数名和pickle一致。

  ```Python
  # 序列化为字符串
  dic = {'age': 23, 'job': 'student'}
  dic_str = json.dumps(dic)
  print(type(dic_str), dic_str)
  # out: <class 'str'> {"age": 23, "job": "student"}
   
  dic_obj = json.loads(dic_str)
  print(type(dic_obj), dic_obj)
  # out: <class 'dict'> {'age': 23, 'job': 'student'}
  
  # 可以看到，dumps函数将对象转换成了字符串。loads函数又将其恢复成字典。
  
  # 存储为json文件
  dic = {'age': 23, 'job': 'student'}
  with open('abc.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f)
   
  with open('abc.json', encoding='utf-8') as f:
    obj = json.load(f)
    print(obj)
      
  # 存储自定义对象
  # 还是上面的Person对象。如果直接序列化会报错
  aa = Person('Bob', 23, 'Student')
  with open('abc.json', 'w', encoding='utf-8') as f:
    json.dump(aa, f) # 报错
  '''
  Object of type 'Person' is not JSON serializable此时dump函数里传一个参default就可以了，这个参数接受一个函数，这个函数可以将对象转换为字典。
  '''
  def person2dict(person):
    return {'name': person.name,
        'age': person.age,
        'job': person.job}
  # 这样返回的就是一个字典了，对象实例有个方法可以简化这一过程。直接调用实例的__dict__。例如
  print(aa.__dict) # {'name': 'Bob', 'age': 23, 'job': 'Student'}
  
  #同时在读取的时候load出来的是一个字典，再转回对象就可，同样需要一object_hook参数，该参数接收一个函数，用于将字典转为对象
  def dict2person(dic):
    return Person(dic['name'], dic['age'], dic['job'])
  
  # 于是完整的程序应该写成下面这样
  with open('abc.json', 'w', encoding='utf-8') as f:
    json.dump(aa, f, default=person2dict)
   
  with open('abc.json', encoding='utf-8') as f:
    obj = json.load(f, object_hook=dict2person)
    print(obj.name, obj.age, obj.job)
    obj.work()
  
  # 由于可以使用__dict__代替person2dict函数，再使用lambda函数简化。
  with open('abc.json', 'w', encoding='utf-8') as f:
    json.dump(aa, f, default=lambda obj: obj.__dict__)
  # 以上是存储到文件，存储到变量也是类似操作。
  ```

- shelve模块

  ```Python
  # 还有一个模块，不太常用，通常使用一个open就好。shelve以键值对的形式存储数据。
  with shelve.open('aa') as f:
    f['person'] = {'age': 23, 'job': 'student'}
    f['person']['age'] = 44 # 这里试图改变原来的年龄23
    f['numbers'] = [i for i in range(10)]
   
  with shelve.open('aa') as f:
    person = f['person']
    print(person) # {'age': 23, 'job': 'student'}
    nums = f['numbers']
    print(nums) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      
  '''
  文件不要有后缀名，在windows下会生成aa.bak, aa.dat, aa.dir三个文件（有点# 多）。其中bak和dir文件是可以查看的（貌似两个文件内容一样）在下面这个例子中生成这样的数据。
  '''
  'person', (0, 44)
  'numbers', (512, 28)
  
  '''允许写回--writeback
  
  有个细节，我们读取键person时候，发现age还是23岁，f['person']['age'] = 44后并没有变成44。下面的写法
  '''
  with shelve.open('aa', writeback=True) as f:
    dic = {'age': 23, 'job': 'student'}
    f['person'] = dic
    dic['age'] = 44
    f['person'] = dic
  '''
  相当于赋值了两次，这种方法是可以改变值的。
  默认情况下直接使用f['person']改变其中的值之后，不会更新已存储的值，也就是没有把更新写回到文件，即使是文件被close后。如果有此需要，在open函数中添加一个参数writeback=True。再次运行下看看年龄就被改变了'''
  
  # 写入自定义对象
  
  # 依然使用上面的Person对象
  with shelve.open('aa') as f:
    f['class'] = Person
     
  # 写入类本身
  with shelve.open('aa') as f:
    Person = f['class']
    a = Person('Bob', 23, 'Student')
    a.work()
  
  # 上面的例子说明shelve也可以序列化类本身。当然序列化实例肯定可以。
  with shelve.open('aa') as f:
    a = Person('God', 100, 'watch')
    f['class'] = a
   
  with shelve.open('aa') as f:
    god = f['class']
    god.work()
  
  '''注意，由于我们使用with open打开，故不用写close语句，此模块是有close函数的，如果不是with方法打开的一定要记得主动close。'''
  ```

  



