# 时间日期和模块

> [TOC]
>
> 
>

## 1 - 模块os

- os模块 - 在这个模块中给我们封装好了系统操作的功能函数(方法)。

- 相关操作

  ```Python
  import os  # 导入该模块
  
  # 获取当前操作系统
  # windows-nt  posix->linux,unix 或者mac os x
  print(os.name)
  
  # 查看当前操作系统的详细信息,但是不支持windows操作系统
  print(os.uname())
  
  # 获取当前操作系统的环境变量,返回一个dict
  print(os.environ)
  print(os.environ.keys())
  print(os.environ.values())
  
  # 获取指定的环境变量
  print(os.environ.get('APPDATA'))
  
  # 获取当前目录   例子:curPage 当前页码数
  print(os.curdir)
  
  # 获取当前的工作目录
  # 获取的是绝对路径
  print(os.getcwd())
  
  # 在windows下,写路径尽量写成/
  print(os.listdir('C:/Users/lsmi/Desktop/day'))
  # 直接报错,不能传递文件路径
  print(os.listdir('C:/Users/lsmi/Desktop/day/模块.py'))
  
  # 在当前目录下创建新的目录
  os.mkdir('C:/Users/lsmi/Desktop/day/lx')
  os.mkdir('./goods')
  
  
  # 删除目录, 只能删除空目录
  os.rmdir('goods')
  
  
  # 对文件进行重命名
  os.rename('goods', 'bad')
  
  
  # 获取文件的属性
  print(os.stat('1-os模块.py'))
  
  
  # 删除文件
  os.remove('./bad/hello.py')
  os.remove('test.txt')
  
  # 路径拼接
  path1 = 'C:/Users/lsmi/Desktop/day/'
  path2 = '/lx'
  # 注意:在参数二处尽量不要写/
  print(os.path.join(path1, path2))
  
  # 拆分路径
  print(os.path.split('C:/Users/lsmi/Desktop/day'))
  print(os.path.split('C:/Users/lsmi/Desktop/day/模块.py'))
  
  
  # 拆分文件的扩展名
  path1 = 'C:/Users/lsmi/Desktop/day/os模块.py'
  print(os.path.splitext(path1))
  
  # 判断是否是目录,是返回True  否返回False
  print(os.path.isdir(path1))
  
  # 判断目录存在不存在
  print(os.path.exists(path1))
  
  # 判断s是否是文件
  print(os.path.isfile(path1))
  
  # 获取文件的大小
  print(os.path.getsize(path1))
  
  # 获取当前文件的目录
  print(os.path.dirname(path1))
  
  # 获取当前文件名
  print(os.path.basename(path1))
  
  ```

## 2 - 使用标准的模块

```Python
使用标准的模块即是系统内置的模块
例如:
import os
import time
import random
import sys
```

## 3 - 使用自定义模块

```Python
方式一:
引入自定义模块:
import 文件名
[注意]:文件名后边不要加后缀
用法: 模块名.函数名/常量名

方式二:
from...import 语句
作用:从模块中导入一个指定的函数
例子: from lhy import add
    from lhy import add, mul

写法:from 模块名 import func1[, func2 [, func3]]


方式三:
from...import *
from lhy import *

总结:后两种方法在使用时很方便,直接调用即可,前边不需用添加模块名
  
  
例子:
# 如果模块中和引入执行的文件中定义了相同的函数,那么在执行时,执行文件中的函数警徽覆盖模块中的函数
def mul(num1, num2, num3):
    print(num1 * num2 *num3)

mul(3, 5, 7)
```

## 4 - name属性

```Python
'''
在python中,每一个脚本执行都会有一个__name__属性
1.如果当前脚本独立运行,则其name属性的值为__main__
2.如果当前脚本引入模块,则模块中的names属性值是当前模块名,而执行脚本的name属性值是__main__

'''
if __name__ == '__main__':
    # print('当前自动执行该文件')
    def func1():
        return 111

else:
    # print('bbb' + __name__)
    # print('这是引入模块后所执行')
    def func1():
        return 222


# print(func1())
```

## 5 - 包

```Python
这里的包其实就是文件夹(目录),在使用import到入包时,或者使用from...import导入时,都可以使用包1.包:在python中其实就是一个目录.
2.再引入的时候包.模块[.函数]
3.当引入的模块出现同名的时候,我们可以起一个别名来解决同名的问题
包作用:一般在项目中会出现功能类似导致模块名相同时.并且在引用的过程中就会出现冲突的问题.这时我们可以很好通过包来解决这个问题
```

## 6 - time模块

- **基础知识**

```Python
UTC:协调世界时，又称世界统一时间、世界标准时间、国际协调时间
在中国来说是UTC+8
时间的形式：
1、时间戳
以整型或浮点型表示时间的一个以秒为单位的时间间隔。
这个时间间隔的基础值是从1970年1月1日领带开始算起
2.元组
一种Python的数据结构表示，这个元组有9个整型内容
year
month
day
hours
minutes
seconds
weekday
Julia day
flag  (1 或 -1 或0)
3.格式化字符串
%a  本地（locale）简化星期名称
%A  本地完整星期名称
%b  本地简化月份名称
%B  本地完整月份名称
%c  本地相应的日期和时间表示
%d  一个月中的第几天（01 - 31）
%H  一天中的第几个小时（24小时制，00 - 23）
%I  第几个小时（12小时制，01 - 12）
%j  一年中的第几天（001 - 366）
%m  月份（01 - 12）
%M  分钟数（00 - 59）
%p  本地am或者pm的相应符
%S  秒（01 - 61）
%U  一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周
%w  一个星期中的第几天（0 - 6，0是星期天）
%W  和%U基本相同，不同的是%W以星期一为一个星期的开始。
%x  本地相应日期
%X  本地相应时间
%y  去掉世纪的年份（00 - 99）
%Y  完整的年份
%Z  时区的名字（如果不存在为空字符）
%%  ‘%’字符
```

- 代码示例

  ```Python
  import time
  
  # 时间戳 1970-1-1 00:00:00, 以浮点形式显示
  time1 = time.time()
  # print(time1)
  
  # 将时间戳转换成UTC时间
  time2 = time.gmtime(time1)
  # print(time2)
  
  
  # 将时间戳转换成本地时间
  time3 = time.localtime(time1)
  # print(time3)
  
  
  # 将时间格式转换成时间戳 单位是S,  返回一个浮点数
  time4 = time.mktime(time3)
  # print(time4)
  
  # 将时间格式转换成用户可读的时间形式  ,并且返回的是一个字符串
  time5 = time.asctime(time3)
  # print(time5)
  # print(type(time5))
  
  # 将时间戳转换成用户可读的时间.
  time6 = time.ctime(time1)
  # print(time6)
  # print(type(time6))
  
  # 字符串的格式化输出,一般展示给你的亲爱的用户来看
  time7 = time.strftime('%Y-%m-%d %X', time2)
  time8 = time.strftime('%Y-%m-%d %X', time3)
  # print(time7)
  # print(time8)
  
  # 将字符串的时间格式转换成元祖类型的时间格式
  time9 = time.strptime(time7,'%Y-%m-%d %X')
  print(time9)
  ```

  ## 7 - datatime模块

  ```Python
  import datetime
  
  
  date1 = datetime.datetime.now()
  # print(date1)
  # print(type(date1))
  
  # 获取指定的时间
  date2 = datetime.datetime(2028, 6, 6, 10, 23, 34, 234)
  # print(date2)
  
  date3 = date1.strftime('%Y-%m-%d %X')
  # print(date3)
  
  
  date4 = datetime.datetime.strptime(date3, '%Y-%m-%d %X')
  print(date4)
  
  
  
  date5 = datetime.datetime(2020, 2, 7, 0, 0, 0, 456787)
  date6 = datetime.datetime.now()
  date7 = date5 - date6
  print(date7)
  # print(type(date7))
  print(date7.days)
  print(date7.seconds)
  ```

  

## 8 - calendar模块

```Python
import calendar
'''
日历模块
'''
# 获取指定的月份
# print(calendar.month(2018, 5))

# 获取指定的年份
# print(calendar.calendar(2018))
#

# 参数一返回上个月的最后一天对应的星期
# 参数二返回当月的天数
# print(calendar.monthrange(2018, 6))

# 返回一个二级列表, 并且每个单独的二级列表是以周为单位
# print(calendar.monthcalendar(2018, 4))
```

