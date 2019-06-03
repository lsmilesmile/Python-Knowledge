# 多线程编程



## 1 - 简介

​	多线程编程对于具有如下特点的编程任务而言是非常理想的：本质上是异步的；需要多 个并发活动；每个活动的处理顺序可能是不确定的，或者说是随机的、不可预测的。这种编 程任务可以被组织或划分成多个执行流，其中每个执行流都有一个指定要完成的任务。根据 应用的不同，这些子任务可能需要计算出中间结果，然后合并为最终的输出结果。    



## 2 - 进程和线程

### 2.1 进程

​	计算机程序只是存储在磁盘上的可执行二进制（或其他类型）文件。只有把它们加载到 内存中并被操作系统调用，才拥有其生命期。 进程（有时称为重量级进程）则是一个执行中 的程序。每个进程都拥有自己的地址空间、内存、数据栈以及其他用于跟踪执行的辅助数据。采用进程间通信（IPC）的方式共享信息。    

### 2.2 线程

​	线程（有时候称为轻量级进程）与进程类似，不过它们是在同一个进程下执行的，并 共享相同的上下文。可以将它们认为是在一个主进程或“主线程”中并行运行的一些“迷 你进程”。 

​	线程包括开始、执行顺序和结束三部分。它有一个指令指针，用于记录当前运行的上下 文。当其他线程运行时，它可以被抢占（中断）和临时挂起（也称为睡眠） ——这种做法叫 做让步。

 	一个进程中的各个线程与主线程共享同一片数据空间，因此相比于独立的进程而言，线 程间的信息共享和通信更加容易。线程一般是以并发方式执行的，正是由于这种并行和数据 共享机制，使得多任务间的协作成为可能。当然，在单核 CPU 系统中，因为真正的并发是不 可能的，所以线程的执行实际上是这样规划的：每个线程运行一小会儿，然后让步给其他线 程（再次排队等待更多的 CPU 时间）。在整个进程的执行过程中，每个线程执行它自己特定 的任务，在必要时和其他线程进行结果通信。 

​	当然，这种共享并不是没有风险的。如果两个或多个线程访问同一片数据，由于数据访 问顺序不同，可能导致结果不一致。这种情况通常称为竞态条件。幸运的是， 大多数线程库都有一些同步原语，以允许线程管理器控制执行和访问。    

### 2.3 线程和Python

​	Python 代码的执行是由 Python 虚拟机（又名解释器主循环）进行控制的。尽管Python 解释器中可以运行多个线程，但是在任意给定时刻只有一个线程会被解释器执行。    

​	对 Python 虚拟机的访问是由全局解释器锁（GIL）控制的。这个锁就是用来保证同时只 能有一个线程运行的。在多线程环境中， Python 虚拟机将按照下面所述的方式执行：

```
1. 设置 GIL。
2. 切换进一个线程去运行。 
3. 执行下面操作之一：
   -  指定数量的字节码指令。 
   - 线程主动让出控制权（可以调用 time.sleep(0)来完成）。
4. 把线程设置回睡眠状态（切换出线程）。 
5. 解锁 GIL。 
6. 重复上述步骤     
```

### 2.4 在Python中使用线程

#### 2.4.1 不使用线程的情况

```Python
from time import sleep, ctime

def loop0():
    print('Start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())

def loop1():
    print('Start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())

def main():
    print('Start at:', ctime())
    loop0()
    loop1()
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
    
'''
Start at: Fri Oct  5 22:38:00 2018
Start loop 0 at: Fri Oct  5 22:38:00 2018
loop 0 done at: Fri Oct  5 22:38:04 2018
Start loop 1 at: Fri Oct  5 22:38:04 2018
loop 1 done at: Fri Oct  5 22:38:06 2018
all DONE at: Fri Oct  5 22:38:06 2018
'''
```

loop0和loop1两个睡眠操作按顺序执行，执行时间是两个睡眠时间的总和。

#### 2.4.2 Python的多线程模块

​	Python中支持多线程编程的模块：thread、threading和Queue等。

```
thread - 提供基本的线程和锁定支持；
threading - 级别比thread更高，提供功能更全面的线程管理；
Queue - 用户可以创建一个队列数据结构，用于在多线程之间进行共享。
```

###### thread模块

1. thread模块的函数

   |                     函数                      |                             描述                             |
   | :-------------------------------------------: | :----------------------------------------------------------: |
   | start_new_thread(finction, args, kwargs=None) | 派生一个新的线程，使用给定的args和可选的kwargs来执行function |
   |                allocate_lock()                |                      分配LockType锁对象                      |
   |                    exit()                     |                        给线程退出指令                        |

2. LockType锁对象的方法

   |        函数        |                   描述                    |
   | :----------------: | :---------------------------------------: |
   | acquire(wait=None) |              尝试获取锁对象               |
   |      locked()      | 如果获取了锁对象则返回True，否则返回False |
   |     release()      |                  释放锁                   |

3. 用多线程解决上面的睡眠的例子

   ```Python
   import _thread as thread
   from time import sleep, ctime
   
   def loop0():
       print('Start loop 0 at:', ctime())
       sleep(4)
       print('loop 0 done at:', ctime())
   
   
   def loop1():
       print('Start loop 1 at:', ctime())
       sleep(2)
       print('loop 1 done at:', ctime())
   
   
   def main():
       print('Starting at:', ctime())
       # 该函数必须传递两个参数，如果函数没有参数，则传递一个空元祖
       thread.start_new_thread(loop0, ())  
       thread.start_new_thread(loop1, ())
       sleep(6)  # 模拟线程同步同步，即等到所有线程结束再向下继续执行
       print('all done at:', ctime())
   
   
   if __name__ == '__main__':
       main()
   
   '''
   Starting at: Fri Oct  5 23:04:10 2018
   Start loop 0 at: Fri Oct  5 23:04:10 2018
   Start loop 1 at: Fri Oct  5 23:04:10 2018
   loop 1 done at: Fri Oct  5 23:04:12 2018
   loop 0 done at: Fri Oct  5 23:04:14 2018
   all done at: Fri Oct  5 23:04:16 2018
   '''
   ```

   上面模拟线程同步还是需要等待6秒，并没有什么好处，可以用锁来处理线程同步机制：

   ```Python
   import _thread as thread
   from time import sleep, ctime
   
   loops = [4, 2]
   
   def loop(nloop, nsec, lock):
       print('start loop', nloop, 'at:', ctime())
       sleep(nsec)
       print('loop', nloop, 'done at:', ctime())
       lock.release()
   
   
   def main():
       print('starting at:', ctime())
       locks = []  # 存放锁
       nloops = range(len(loops))
       for i in nloops:
           lock = thread.allocate_lock()  # 分配锁对象
           lock.acquire()  # 获取锁对象
           locks.append(lock)  # 将锁对象加入锁列表
   
       # 多线程执行loop()函数
       for i in nloops:
           thread.start_new_thread(loop, (i, loops[i], locks[i]))
   
       # 暂停主线程，直到所有锁都被释放之后才会继续执行
       for i in nloops:
           while locks[i].locked():
               pass
       print('all done at:', ctime())
   
   if __name__ == '__main__':
       main()
   
   ```



###### threading模块

**threading模块的对象**

|       对象       |                             描述                             |
| :--------------: | :----------------------------------------------------------: |
|      Thread      |                    表示执行一个线程的对象                    |
|       Lock       |             锁原语对象（和thread模块中的锁一样）             |
|      RLock       |        可重入锁对象，使单一线程可以再次获得已持有的锁        |
|    Condition     |   条件变量对象，使得一个线程等待另一个线程满足特定的“条件”   |
|      Event       | 条件变量的通用版本，任意数量的线程等待某个事件的发生，在该事件发生后所有线程将被激活 |
|    Semaphore     | 为线程间共享的有限资源提供一个计数器，如果没有可用资源时会被阻塞 |
| BounderSemaphore |           与Semaphore相似，不过它不允许超过初始值            |
|      Timer       |          与Thread相似，不过它要在运行前等待一段时间          |

**守护线程**

​	避免使用 thread 模块的另一个原因是该模块不支持守护线程这个概念。当主线程退出 时，所有子线程都将终止，不管它们是否仍在工作。如果你不希望发生这种行为，就要引 入守护线程的概念了。

​	 threading 模块支持守护线程，其工作方式是：守护线程一般是一个等待客户端请 求服务的服务器。如果没有客户端请求，守护线程就是空闲的。如果把一个线程设置 为守护线程，就表示这个线程是不重要的，进程退出时不需要等待这个线程执行完成。    

​	如果主线程准备退出时，不需要等待某些子线程完成，就可以为这些子线程设置守护 线程标记。该标记值为真时，表示该线程是不重要的，或者说该线程只是用来等待客户端 请求而不做任何其他事情。    

**Thread类**

threading模块的Thread类是主要的执行对象

**Thread对象的属性**

|  属性  |                 描述                 |
| :----: | :----------------------------------: |
|  name  |                线程名                |
| ident  |             线程的标识符             |
| daemon | 布尔标志，表示这个线程是否是守护线程 |

**Thread对象方法**

|                             属性                             |                             描述                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| __init__(group=None, target=None, name=None, args=(), kwargs={}, verbose=None, daemon-None) | 实例化一个线程对象，需要有一个可调用的target，以及其参数args或kwargs。还可以传递name或group参数 |
|                           start()                            |                        开始执行该线程                        |
|                            run()                             |           定义线程功能的方法（通常在子类中被重写）           |
|                      join(timeout=None)                      | 直至启动的线程终止之前一直挂起；除非给出了timeout（秒），否则会一直阻塞 |
|                          getName()                           |                          返回线程名                          |
|                        setName(name)                         |                          设定线程名                          |
|                          is_alive()                          |               布尔标志，表示这个线程是否还存活               |
|                        thread.daemon                         |           如果是守护线程，返回True，否则返回False            |

**threading模块的Thread实例**

```Python
import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('start at:', ctime())
    threads = []  # 存放线程
    nloops = range(len(loops))  # 保存要执行的线程的数量

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()  # 等待线程列表中的所有线程结束

    print('all done at:', ctime())


if __name__ == '__main__':
    main()

'''
start at: Sat Oct  6 05:18:17 2018
start loop 0 at: Sat Oct  6 05:18:17 2018
start loop 1 at: Sat Oct  6 05:18:17 2018
loop 1 done at: Sat Oct  6 05:18:19 2018
loop 0 done at: Sat Oct  6 05:18:21 2018
all done at: Sat Oct  6 05:18:21 2018
'''
```

实例化 Thread（调用 Thread()）和调用 thread.start_new_thread() 的最大区别是新线程不会立即开始执行。   当所有线程都分配完成之后，通过调用每个线程的 start()方法让它们开始执行，而不是 在这之前就会执行。相比于管理一组锁（分配、获取、释放、检查锁状态等）而言，这里只 需要为每个线程调用 join()方法即可。 join()方法将等待线程结束，或者在提供了超时时间的 情况下，达到超时时间。使用 join()方法要比等待锁释放的无限循环更加清晰（这也是这种锁 又称为自旋锁的原因）。     

**创建Thread的实例，传给它一个可调用的实例**

```Python
import threading
from time import sleep, ctime


loops = [4, 2]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    # 对象可以被调用
    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(
            loop, (i, loops[i]), loop.__name__))
        # loop方法传递给class中的func参数，再给该函数传递两个参数，不需要给Thread对象传递参数
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at:', ctime())


if __name__ == '__main__':
    main()

'''
starting at: Sat Oct  6 06:58:22 2018
start loop 0 at: Sat Oct  6 06:58:22 2018
start loop 1 at: Sat Oct  6 06:58:22 2018
loop 1 done at: Sat Oct  6 06:58:24 2018
loop 0 done at: Sat Oct  6 06:58:26 2018
all done at: Sat Oct  6 06:58:26 2018
'''
```

**子类化Thread**

```Python
import threading
from time import sleep, ctime

loops = (4, 2)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('start at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at:', ctime())


if __name__ == '__main__':
    main()

```







