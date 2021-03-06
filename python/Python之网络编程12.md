# 网络编程



## 1 - 简介

### 1.1 客户端服务器架构

​	什么是客户端/服务器架构？服务器就 是一系列硬件或软件，为一个或多个客户端（服务的用户）提供所需的“服务”。它存在唯一 目的就是等待客户端的请求，并响应它们（提供服务），然后等待更多请求。    

![](.\images\12-1.png)

#### 1.1.1 硬件客户端/服务器架构

- 打印机
- 文件服务器

#### 1.1.2 软件客户端/服务器架构

- 软件服务器

  - Web服务器

    一个这样的服务器的工作就是接受客户端请求，并向（Web）客户端（即 用户计算机上的浏览器）回送 Web 页面，然后等待下一个客户端的请求。    

  - 数据库服务器

    它们接受客户端的存储或检索请求，响应请 求，然后等待更多的事务。    

  - 窗体服务器

    它们运行在一台附带（外接）显示设备（如显示器）的计算机上。窗体客 户端其实就是一些程序，这些程序需要一个窗口化的环境来运行。这些通常被当作图形用户 界面（GUI）应用程序。如果在没有窗体服务器的情况下执行它们，也即意味着在一个基于 文本的环境中，如 DOS 窗口或一个 UNIX shell 中，那么将无法启动它们。

#### 1.1.3 客户端/服务器网络编程

​	在服务器响应客户端请求之前，必须进行一些初步的设置流程来为之后的工作做准备。 首先会创建一个通信端点，它能够使服务器监听请求。一旦一个通信端点已经建立，监听服务器就可以进入无限循 环中，等待客户端的连接并响应它们的请求。    

​	客户端所需要做的只是创建它的单一通信端点，然后建立一个到服务器的 连接。然后，客户端就可以发出请求，该请求包括任何必要的数据交换。一旦请求被服务器 处理，且客户端收到结果或某种确认信息，此次通信就会被终止。

​     

## 2 - 套接字：通信端点

类型：

- 基于文件
- 面向网络

### 2.1 套接字

​	套接字是计算机网路数据结构，在任何类型的通信开始之前，网络应用程序必须创建套接字。可以将它们比作电话插孔，没有它将无法进行通信。

**套接字家族：**

- 第一个家族：UNIX套接字，名字：AF_UNIX，代表地址家族：UNIX，缩写：AF；

  因为两个进程运行在同一台计算机上，所以这些套接字都是基于文件的，这意味着文件 系统支持它们的底层基础结构。因为文件系统是一个运行在同一主机上 的多个进程之间的共享常量。   

  第二种类型的套接字是基于网络的，它也有自己的家族名字 AF_INET，或者地址家族： 因特网。另一个地址家族 AF_INET6 用于第 6 版因特网协议（IPv6）寻址。

- 第二个家族：Python 2.5 中引入了对特殊类型的 Linux 套接字的支持。套接字的AF_NETLINK 家族允许使用标准的 BSD 套接字接口进行用户级别和内核级别代码之间的 IPC。

  针对 Linux 的另一种特性（Python 2.6 中新增）就是支持透明的进程间通信（TIPC）协 议。 TIPC 允许计算机集群之中的机器相互通信，而无须使用基于 IP 的寻址方式。 Python 对 TIPC 的支持以 AF_TIPC 家族的方式呈现。    

Python 只支持 AF_UNIX、 AF_NETLINK、 AF_TIPC 和 AF_INET 家族。    

### 2.2 套接字地址：主机-端口对

​	如果一个套接字像一个电话插孔——允许通信的一些基础设施，那么主机名和端口号就 像区号和电话号码的组合。 

**有效的端口号范围为 0～65535（尽管小于 1024 的端口号预留给了系统）。**  

#### 2.2.1 面向连接的套接字和无连接的套接字

##### 2.2.1.1 面向连接的套接字

​	实现这种连接类型的主要协议是传输控制协议（更为人熟知的是它的缩写 TCP）。为 了 创建 TCP 套接字，必须使用 SOCK_STREAM 作为套接字类型。 TCP 套接字的名字 SOCK_STREAM 基于流套接字的其中一种表示。因为这些套接字（AF_INET）的网络版本 使用因特网协议（IP）来搜寻网络中的主机，所以整个系统通常结合这两种协议（TCP 和 IP） 来进行（当然，也可以使用 TCP 和本地[非网络的 AF_LOCAL/AF_UNIX]套接字，但是很明 显此时并没有使用 IP）。    

##### 2.2.1.2 无连接的套接字

​	实现这种连接类型的主要协议是用户数据报协议（更为人熟知的是其缩写 UDP）。为 了 创建 UDP 套接字，必须使用 SOCK_DGRAM 作为套接字类型。因为这些套接字也使用因特网协议来寻找网络中的主机，所以这个系统也有一个更加普通的名字，即这两种协议（UDP 和 IP） 的组合名字，或 UDP/IP。  



## 3 - 利用Python进行网络编程

主要模块：**socket()**

### 3.1 socket()函数模块

要创建套接字，必须使用 socket.socket()函数，它一般的语法如下：

```Python
socket(socket_family, socket_type, protocol=0)
```

socket_family - AF_UNIX或AF_INET

socket_type - SOCK_STREAM或SOCKET_DGRAM

protocol - 通常省略，默认为0

- 创建TCP/IP套接字

  ```Python
  tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  ```

- 创建UDP/IP套接字

  ```Python
  udp_socket = socket.sock(sock.AF_INET, socket.SOCK_DGRAM)
  ```

### 3.2 套接字对象（内置）方法

- **服务器套接字方法**

  |    名称    |                        描述                         |
  | :--------: | :-------------------------------------------------: |
  |  s.bind()  |      将地址（主机名、端口号对）绑定到套接字上       |
  | s.listen() |                 设置并启动TCP监听器                 |
  | s.accept() | 被动接受TCP客户端连接，已知等待知道连接到达（阻塞） |

- **客户端套接字方法**

  |      名称      |                             方法                             |
  | :------------: | :----------------------------------------------------------: |
  |  s.connect()   |                    主动发起TCP服务器连接                     |
  | s.connect_ex() | connect()的扩展版本，此时会以错误码的形式返回问题， 而不是抛出一个异常 |

- **普通套接字方法**

  |       方法        |                        描述                        |
  | :---------------: | :------------------------------------------------: |
  |     s.recv()      |                    接收TCP消息                     |
  |   s.recv_into()   |             接收TCP消息到指定的缓冲区              |
  |     s.send()      |                    发送TCP消息                     |
  |    s.sendall()    |                 完成地发送TCP消息                  |
  |   s.recvfrom()    |                    接收UDP消息                     |
  | s.recvfrom_into() |             接收UDP消息到指定的缓冲区              |
  |    s.sendto()     |                    发送UDP消息                     |
  |  s.getpeername()  |           连接到套接字（TCP）的远程地址            |
  |  s.getsockname()  |                  当前套接字的地址                  |
  |  s.getsockopt()   |               返回给定套接字选项的值               |
  |  s.setsockopt()   |               设定给定套接字选项的值               |
  |   s.shutdown()    |                      关闭连接                      |
  |     s.close()     |                     关闭套接字                     |
  |    s.detach()     | 在未关闭文件描述的情况下关闭套接字，返回文件描述符 |
  |     s.ioctl()     |         控制套接字的模式（仅支持Windows）          |

- **面向阻塞的套接字方法**

  |      方法       |             描述             |
  | :-------------: | :--------------------------: |
  | s.setblocking() | 设置套接字的阻塞或非阻塞模式 |
  | s.settimeout()  | 设置阻塞套接字操作的超时时间 |
  | s.gettimeout()  | 获取阻塞套接字操作的超时时间 |

- **面向文件的套接字方法**

  |     方法     |            描述            |
  | :----------: | :------------------------: |
  |  s.fileno()  |     套接字的文件描述符     |
  | s.makefile() | 创建与套接字关联的文件对象 |

- **数据属性**

  |   方法   |    描述    |
  | :------: | :--------: |
  | s.family | 套接字家族 |
  |  s.type  | 套接字类型 |
  | s.proto  | 套接字协议 |


### 3.3 创建TCP服务器

​	所有套接字都是通过使用 socket.socket()函数来创建的。因为服务器需要占用一个端口并 等待客户端的请求，所以它们必须绑定到一个本地地址。因为 TCP 是一种面向连接的通信系 统，所以在 TCP 服务器开始操作之前，必须安装一些基础设施。特别地， TCP 服务器必须监 听（传入）的连接。

​	调用 accept()函数之后，就开启了一个简单的（单线程）服务器，它会等待客户端的连接。 默认情况下， accept()是阻塞的，这意味着执行将被暂停，直到一个连接到达。另外，套接字 确实也支持非阻塞模式。

​	一旦服务器接受了一个连接，就会返回（利用 accept()）一个独立的客户端套接字，用来 与即将到来的消息进行交换。使用新的客户端套接字类似于将客户的电话切换给客服代表。 当一个客户电话最后接进来时，主要的总机接线员会接到这个电话，并使用另一条线路将这 个电话转接给合适的人来处理客户的需求。

​	 这将能够空出主线（原始服务器套接字），以便接线员可以继续等待新的电话（客户请求）， 而此时客户及其连接的客服代表能够进行他们自己的谈话。同样地，当一个传入的请求到达 时，服务器会创建一个新的通信端口来直接与客户端进行通信，再次空出主要的端口，以使 其能够接受新的客户端连接。 

​	一旦创建了临时套接字，通信就可以开始，通过使用这个新的套接字，客户端与服务器 就可以开始参与发送和接收的对话中，直到连接终止。当一方关闭连接或者向对方发送一个 空字符串时，通常就会关闭连接。    

**伪代码**

```Python
ss = socket() # 创建服务器套接字
ss.bind() # 套接字与地址绑定
ss.listen() # 监听连接
inf_loop: # 服务器无限循环
	cs = ss.accept() # 接受客户端连接
	comm_loop: # 通信循环
		cs.recv()/cs.send() # 对话（接收/发送）
	cs.close() # 关闭客户端套接字
ss.close() # 关闭服务器套接字#（可选）
```

**TCP服务器代码**

```Python
from socket import *
import time

HOST = ''  # IP地址，表示它可以使用任何可用的地址
PORT = 23412  # 随机端口号
BUFSIZ = 1024  # 缓冲区大小
ADDR = (HOST, PORT)  # 服务器地址

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建TCP服务器套接字
tcpSerSock.bind(ADDR)  # 绑定服务器地址
tcpSerSock.listen(5)  # 开启监听

# 发消息
def send_data():
    ser_data = input('>')
    # 把将要发送的消息编码一下再发送
    tcpCliSock.send(ser_data.encode('utf-8'))

# 收消息
def recv_data():
    recv_time1 = bytes(time.ctime(), 'utf-8')
    cli_data = tcpCliSock.recv(BUFSIZ)
    # 把接收的消息解码，然后打印出来
    content = '[%s] %s' % (recv_time1, cli_data.decode('utf-8'))
    print(content)

while True:
    print('waiting for connecting...')
    # 等待一个客户端连接
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)
    # 对话进入无线循环中
    while True:
        send_data()
        recv_data()
    tcpCliSock.close()
tcpSerSock.close()

```

### 3.4 创建TCP客户端

**伪代码**

```Python
cs = socket() # 创建客户端套接字
cs.connect() # 尝试连接服务器
comm_loop: # 通信循环
	cs.send()/cs.recv() # 对话（发送/接收）
cs.close() # 关闭客户端套接字
```

**TCP客户端代码**

```Python
from socket import *
import threading
import time

HOST = '127.0.0.1'  # 'localhost'  # 本机
PORT = 23412  # 与服务器设置的端口一样
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 客户端套接字
tcpCliSock.connect(ADDR)  # 创建一个到服务器的连接


# 发消息
def send_data():
    cli_data = input('>')
    tcpCliSock.send(cli_data.encode('utf-8'))

# 收消息
def recv_data():
    ser_data = tcpCliSock.recv(BUFSIZ)
    content = '[%s] %s' % (bytes(time.ctime(), 'utf-8'), ser_data.decode('utf-8'))
    print(content)


while True:
    send_data()
    recv_data()
tcpCliSock.close()

```

### 3.5 创建UDP服务器

**伪代码**

```Python
ss = socket() # 创建服务器套接字
ss.bind() # 绑定服务器套接字
inf_loop: # 服务器无限循环
	cs = ss.recvfrom()/ss.sendto() # 关闭（接收/发送）
ss.close()
```

**UDP服务器伪代码**

```Python
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
'''
因为 UDP 是无连接的，所以这里没有调用“监听传入的连接”。
'''

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(data, addr)
    print('...received from and return to:', addr)
udpSerSock.close()
```

### 3.6 创建UDP客户端

**伪代码**

```Python
cs = socket() # 创建客户端套接字
comm_loop: # 通信循环
	cs.sendto()/cs.recvfrom() # 对话（发送/接收）
cs.close() # 关闭客户端套接字
```

**UDP客户端代码**

```Python
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

udpCliSock.close()

```

### 3.7 socket模块属性

- **数据属性**

  |                    属性                     |               描述               |
  | :-----------------------------------------: | :------------------------------: |
  | AF_UNIX/AF_INET/AF_INET6/AF_NETLINK/AF_TICP |          套接字地址家族          |
  |              SO_STREAM/AF_TIPC              | 套接字类型（TCP=流，UDP=数据报） |
  |                  has_ipv6                   |      是否支持IPv6的布尔标记      |

- **异常**

  |   属性   |        描述        |
  | :------: | :----------------: |
  |  error   |   套接字相关错误   |
  |  herror  | 主机和地址相关错误 |
  | gaierror |    地址相关错误    |
  | timeout  |      超时时间      |

- **函数**

  |              属性               |                             描述                             |
  | :-----------------------------: | :----------------------------------------------------------: |
  |            socket()             | 以给定的地址家族、套接字类型和协议类型（可选）创建一个套接字对象 |
  |          socketpair()           | 以给定的地址家族、套接字类型和协议类型（可选）创建一个套接字对象 |
  |       create_connection()       |       接收一个地址对（主机名、端口号），返回套接字对象       |
  |            fromfd()             |            以打开一个文件描述符创建一个套接字对象            |
  |              ssl()              |      通过套接字启动一个安全套接字层连接；不执行证书验证      |
  |          getaddrinfo()          |               获取一个五元组序列形式的地址信息               |
  |          getnameinfo()          |       给定一个套接字地址，返回（主机名、端口号）二元组       |
  |            getqdn()             |                        返回完整的域名                        |
  |          gethostname()          |                        返回当前主机名                        |
  |         gethostbyname()         |                 将一个主机名映射到它的ip地址                 |
  |       gethostbyname_ex()        |             返回主机名、别名主机集合和IP地址列表             |
  |         gethostbyaddr()         | 将一个IP地址映射到DNS信息；返回与gethostbyname_ex()相同的三元组 |
  | getservbyname()/getservbyport() | 将一个服务名映射到一个端口号，或者反过来；对于任何一个函数来说，协议名都是可选的 |

## 4 - SocketServer模块

**SocketServer模块类**

|                    类                     |                             描述                             |
| :---------------------------------------: | :----------------------------------------------------------: |
|                BaseServer                 | 包含核心服务器功能和mix_in类的钩子；仅用于推导，这样不会创建这个类的实例；可以用TCPServer或UDPServer创建类的实例 |
|            TCPServer/UDPServer            |                 基础的网络同步TCP/UDP服务器                  |
|       UnixStream/UnixDatagramServer       |               基于文件的基础同步TCP/UDP服务器                |
|        ForkingMixIn/ThreadingMixIn        | 核心派出或线程功能；只用作mix-in类与一个服务器配合实现一些异步性；不能直接实例化这个类 |
|     ForkingTCPServer/ForkingUDPServer     |           ForkingMixIn和TCPServer/UDPServer的组合            |
|    ThreadingTCPServer/ThreadUDPServer     |          ThreadingMixIn和TCPServer/UDPServer的组合           |
|             BaseRequestHandle             | 包含处理服务请求的核心功能；仅仅用于推导，这样无法创建这个类的实例；可以使用StreamRequestHandler或DatagramRequestHandler创建类的实例 |
| StreamRequestHandle/DatagramRequestHandle |                实现TCP/UDP服务器的服务处理器                 |

**socketserver tcp服务器**

```Python
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):  #所有请求的交互都是在handle里执行的,
        while True:
            try:
                self.data = self.request.recv(1024).strip()#每一个请求都会实例化MyTCPHandler(socketserver.BaseRequestHandler):
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                self.request.sendall(self.data.upper())#sendall是重复调用send.
            except ConnectionResetError as e:
                print("err ",e)
                break

if __name__ == "__main__":
    HOST, PORT = "", 9999 #windows
    #HOST, PORT = "0.0.0.0", 9999 #Linux
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)   #线程
    server.serve_forever()
```

**socketserver tcp 客户端**

```Python
#客户端
import socket
client = socket.socket() #定义协议类型,相当于生命socket类型,同时生成socket连接对象
client.connect(('localhost',9999))
while True:
    msg = input(">>>").strip()
    if len(msg) ==0:continue
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)#这里是字节1k
    print("recv:>",data.decode('utf-8'))
client.close()
```

