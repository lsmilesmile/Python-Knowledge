# Python简介

## 1 - Python的特点

- **Python是免费的自由的软件**

  ​	Python遵循GPL协议，是自由软件，这是Python流行的原因之一。用户使用Python进行开发和发布自己编写的程序不需要支付任何费用，不用担心版权问题，即使作为商业用途，Python也是免费的。开源自由软件正成为软件行业的一种发展趋势。作为自由软件，最令人鼓舞的就是可以很方便地获取源代码。

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

### 3.1 Windows上安装Python

- 首先进入Pytho[官网](https://www.python.org/)

  ![](.\images\1-1.png)

- 到页面底部点击Download

  ![](.\images\1-2.png)

- 这里有许多版本，找到想要的版本点击Download

  ![](.\images\1-3.png)

- 下载后可以看到安装程序，点击安装

  ![](.\images\1-5.png)

- 安装过程

  ![](.\images\1-6.png)

  ![1-7](.\images\1-7.png)

  点击next后选择安装位置

  ![](.\images\1-8.png)

  点击install等待安装完成

- 测试Python是否安装好

  在命令行下输入如下：

  ![](.\images\1-9.png)

- 启动Python并运行一行代码

  ![](.\images\1-10.png)

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

  


