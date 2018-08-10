# Python简介

[TOC]

## 1 - Python的特点

- **Python是免费的自由的软件**

  ​	Python遵循GPL协议，是自由软件，这是Python流行的原因之一。Python是一种解释性,面向对象型,动态数据库类型的高级编程语言。用户使用Python进行开发和发布自己编写的程序不需要支付任何费用，不用担心版权问题，即使作为商业用途，Python也是免费的。开源自由软件正成为软件行业的一种发展趋势。作为自由软件，最令人鼓舞的就是可以很方便地获取源代码。

- **Python是跨平台的**

  ​	跨平台和良好的可移植性是C语言成为经典编程语言的额关键，而Python正是用可移植的ANSI C编写的。这意味着Python也具有良好的跨平台特性，也就是说，在Windows下编写的Python程序可以轻易地运行在Linux下。

- **Python功能强大**

  ​	Python强大的功能也是很多用户支持Python的最重要原因，从字符串处理到复杂的3D图形编程，Python借助拓展模块都可以轻易完成。实际上，Python的核心模块就已经提供了足够强大的功能，使用Python精心设计的蘖枝模块可以完成许多强大的操作，更重要的是Python还有许多丰富的开源的第三方库，可支持大量的不同应用。

- **Python语言清晰优雅**

  ​	Python语言语法简单，写出的程序必须遵守其缩进规则，其语句块的标志就是由缩进来决定的，这使得Python程序格式清晰、易写、易度。Python设计的哲学是“优雅”、“明确”、“简单”。

## 2 - Python的用武之地

- **开发网站**

  ​	Python有许多Web框架，如Django、Flask等，使用Python搭建网站，后台服务会比较容易维护，当需要增加新功能，用Python可以比较容易地实现。而且用Python开发网站最大的一个特点就是开发速度快，主要因为Python的Web框架已经帮助我们做了许多事。

- **自动化运维**

  ​	我们发现，现在越来越多的运维开始倾向于自动化，批量处理大量的运维任务。Python在系统管理上的优势在于强大的开发能力和完整的工具链。

- **数据分析**

- **开发游戏**

- **自动化测试**

- **人工智能与大数据**

- **网络爬虫**

## 3 - 环境的搭建

python有两个版本:  python2.x  和python3.x

作用: 运行python代码

```Python
1.安装python的时候,一定要将python添加到环境变量中
2.打开doc命令, 输入python,即可查看到python的版本内容信息
3.退出: exit()   quit()
4.pip  是python安装第三方工具的一个类库
   输入: pip  -V     #查看有没有pip这个库
```



### 3.1 Windows上安装Python

- 首先进入Pytho[官网](https://www.python.org/)

  ![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/1-1.png)

- 到页面底部点击Download

  ![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/1-2.png)

- 这里有许多版本，找到想要的版本点击Download

  ![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/1-3.png)

- 下载后可以看到安装程序，点击安装

  ![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/1-5.png)

- 安装过程

  ![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/1-6.png)

  ![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/1-7.png)

  点击next后选择安装位置

  ![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/1-8.png)

  点击install等待安装完成

- 测试Python是否安装好

  在命令行下输入如下：

  ![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/1-9.png)

- 启动Python并运行一行代码

  ![](https://github.com/lsmilesmile/Python-Knowledge/blob/master/python/images/1-10.png)

### 3.2 linux上安装Python

- **方法一**

1. 首先安装依赖包

   ```
   yum -y groupinstall "Development tools"
   
   yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
   ```

2. 然后根据自己需求下载不同版本的Python3，我下载的是Python3.6.2

   ```
   wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
   
   然后解压压缩包，进入该目录，安装Python3
   
   tar -xvJf  Python-3.6.2.tar.xz
   cd Python-3.6.2
   ./configure --prefix=/usr/local/python3
   make && make install
   ```

3. 最后创建软链接

   ```
   ln -s /usr/local/python3/bin/python3 /usr/bin/python3
   
   ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
   ```

- **方法二**

  ```
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# yum install gcc
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# gunzip Python-3.6.5.tgz
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# ar -xvf Python-3.6.5.tar
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# cd Python-3.6.5
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# ./configure --prefix=/usr/local/python36 --enable-optimizations
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# make && make install
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# ln -s /usr/local/python36/bin/python3.6 /usr/bin/python3
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# python3 --version
  Python 3.6.5
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# python3 -m pip install -U pip
  [root@iZwz97tbgo9lkabnat2lo8Z ~]# pip3 --version
  ```




## 4 - 安装编辑器

### 4.1 编辑器种类

pycharm

sublime

以上两个编辑器的安装网上都有教程

### 4.2 相关命令

```Python
1.dir  #查看当前目录下的所有文件     目录就是文件夹
2.cd  文件夹   #进入文件夹或者目录中
```



## 5 - 计算机相关知识

### 5.1 内存

```Python
内存: 我们可以把内存抽象成一个开关, 有两种状态:  打开和关闭.  一种状态对应1,一种状态对应0. 这时我们可以把一个开关的状态称作"一位"  我们可以同时把八个开关放到一个房间里边.  哪么我们可以这个房间看做"一个字节" 每个房间都有自己的门牌编号. 我们将这个门牌编号称作为"地址".  我们把无数个房间堆叠起来就是一栋大厦,  而这栋大厦就是"内存"
```

### 5.2 单位

```Python
1bit
8bit == 1B(byte)  一个字节
1024B ==  1KB
1024KB == 1MB
1024MB == 1GB
1024GB == 1TB
内存中以二进制的形式来存储数据
```

### 5.3 进制

```Python
二进制:   0     1    逢二进一
0 + 0  = 0
1 + 1 = 10
11 + 1 = 100


八进制: 0 1 2 3 4 5 6 7   逢八进一
3 + 4 = 7
1 + 7 = 10


十进制:  0 1 2 3 4  5 6 7 8 9   逢十进一
3 + 8 = 11
2 + 8 = 10
3 + 6 = 9

十六进制:  0 1 2 3 4  5 6 7 8 9  A b c d e f 逢十六进一
1  + f = 10
```

### 5.4 进制间的转换

```Python
十进制  ->  二进制
#规则:  倒除法,  余数逆序
10(10)->1010(2)


二进制   ->  十进制
#规则: 根据当前数字,乘以2的位数次方,然后相加
1010(2)->10(10)


八进制  -> 二进制
#规则: [一转三位]  八进制的一位相对于二进制的三位,转时按照十进制转二进制进行
65(8)->110101(2)

二进制  -> 八进制
#规则 [三位转一]  二进制的三位相对于八进制的一位,
110101(2)->65(8)
1*2^0+0*2^1+1*2^2 = 5
0*2^0+1*2^1+1*2^2 = 6

十六进制-->二进制
#规则[一位转四位]十六进制的一位相对于二进制的四位,转时按照十进制转二进制进行
a4(16)->10100100(2)

采用8421法

8  4  2  1
0  1  0  0-------4
1  0  1   0------a


二进制  ->  十六进制

#规则[四位转一位]二进制的四位相对于十六进制的一位,
01000011(2)->43(16)
```

| 数字 | 二进制 | 八进制 | 十进制 | 十六进制 |
| ---- | ------ | ------ | ------ | -------- |
| 0    | 0      | 0      | 0      | 0        |
| 1    | 1      | 1      | 1      | 1        |
| 2    | 10     | 2      | 2      | 2        |
| 3    | 11     | 3      | 3      | 3        |
| 4    | 100    | 4      | 4      | 4        |
| 5    | 101    | 5      | 5      | 5        |
| 6    | 110    | 6      | 6      | 6        |
| 7    | 111    | 7      | 7      | 7        |
| 8    | 1000   | 10     | 8      | 8        |
| 9    | 1001   | 11     | 9      | 9        |
| 10   | 1010   | 12     | 10     | a        |
| 11   | 1011   | 13     | 11     | b        |
| 12   | 1100   | 14     | 12     | c        |
| 13   | 1101   | 15     | 13     | d        |
| 14   | 1110   | 16     | 14     | e        |
| 15   | 1111   | 17     | 15     | f        |

### 5.5 数据的存储

```Python
10(10)->1010(2)
1 10   -1
#在存储数据时,最高位表示标识符, 1表示负数, 0表示正数
00000000000000000000000000000001
10000000000000000000000000000001
-----------------------------------------
100000000000000000000000000000010

原码  反码   补码
原码:规定了字节数, 写明了符号位, 就得到原码
 00000000000000000000000000000001
 10000000000000000000000000000001
----------------------------------------
  100000000000000000000000000000010
  
  
 反码: 正数的反码是其原码, 负数的反码是其原码的符号位不变, 其他为取反
  00000000000000000000000000000001
  11111111111111111111111111111110
  -----------------------------------
  11111111111111111111111111111111
  
  
  
  补码:  正数的补码是其原码,负数的补码是其反码加1
    00000000000000000000000000000001
    11111111111111111111111111111111
    -----------------------------------------
    100000000000000000000000000000000
    
    总结:计算机是以补码的形式来存储数据的
```

### 5.6 路径问题

#### 5.6.1 路径问题1

```
windows:
  
C:\Users\刘海艳\Desktop\day03\hello.py
C:/Users/刘海艳/Desktop/day03
  
  
linux:
/root/admin/index/hello.py

总结:在后期开发过程中,无论在windows下边还是linux下边我们写路径做最好使用/
```

#### 5.6.2 路径问题2

```Python
相对路径:(有参照物而言)
  	当前文件: 当前执行的文件就是当前文件.
    当前文件夹: 当前执行文件所在的文件夹就是当前文件夹
    ../lhy.jpg   上一级
    ../../lhy.jpg  上上一级
    ../作业/lhy.jpg
绝对路径:(表示唯一性)   /(目录分隔符或者文件夹分隔符)
  		1.磁盘绝对:C:/Users/刘海艳/Desktop/day03
    	2.站点绝对:https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=398724402,2324394055&fm=200&gp=0.jpg
            
            
linux 操作系统:
/root/admin/index/index.html
第一个/表示:  根目录
往后走目录之间的/表示不:  目录分隔符
  
  
 
http:   默认端口是80-
https: 默认端口443    针对于网络协议更安全可靠,具有加密的功能
  
网站协议组部分:
https://www.baidu.com:80/index.html?name=shilin&sex=nan&height=180
http/https:  网站协议  1.1
www.baidu.com: 域名
80:  端口号      443(https)  21(ftp)  3306(数据库)
文件路径: application/index.html
参数:  之间使用&隔开   键值对的形式存在   name=狗蛋   sex=女   height=160
```

