'''循环双链表'''

from DLList import DLNode
from LList import LList

class LCDList(LList):

    def __init__(self):
        LList.__init__(self)


    # 表的长度
    def length(self):
        # 如果是空表
        if self._head is None:
            return 0
        else:
            # 初始化cursor指向头结点，且count这时取1
            cursor = self._head
            count = 1
            # 如果cur.next不是head，说明cur目前不是最后一个元素，那么count就1，再让cur后移一位
            while cursor.next is not self._head:
                count += 1
                cursor = cursor.next
            return count

    # 头插法
    def prepend(self, elem):
        node = DLNode(elem)
        # 如果是空表
        if self._head is None:
            self._head = node
            # 头尾都指向自己
            node.next = node
            node.prev = node    
        # 不为空      
        else:
            # 先设置结点的前后指针域
            node.next = self._head  # p的next设为现在的head指向的结点
            node.prev = self._head.prev  # p的prev为head的prev
            # 再设置原来的头尾结点的prev和next指针域
            self._head.prev.next = node # 原来的尾结点的next为新结点p
            self._head.prev = node  # 原来的头结点的prev为新结点p
            # 更改头指针指向p
            self._head = node

    # 尾插法
    def append(self, elem):
        # 如果是空表，就可以用头插法
        if self._head is None:
            self.prepend(elem)
        else:
            node = DLNode(elem)
            # 先设置新结点的prev和next指针
            node.next = self._head # 原来的头结点
            node.prev = self._head.prev  # 原来的尾结点
            self._head.prev.next = node  # 原来尾结点的next指向新结点
            self._head.prev = node  # 头指针指向尾结点，即新增加的结点

    # 在位置pos插入结点
    def insert(self, pos, item):
        # 如果插入位置<0，采用头插法
        if pos < 0:
            self.prepend(item)
        # 如果位置是最后一个元素或者更大
        elif pos > self.length() - 1:
            self.append(item)
        # 如果插入位置在链表中间
        else:
            index = 0  # 计数，记录向后移动了多少部
            cursor = self._head  # cursor记录当前位置
            #让index每次自增1 ，cur后移，当index=pos-1的时候说明cur在要插入位置的前一个元素，这时候停下
            while index < pos - 1:
                index += 1
                cur = cur.next
            #跳出循环，cur在要插入位置的前一个元素，将node插入到cur的后面
            node = DLNode(item)  # 新建一个节点
            node.next = cursor.next  # node的后继设为cur的后继
            node.prev = cursor  # node的前驱设为cur
            cursor.next.prev = node  # cur后继的前驱改为node
            cursor.next = node  # cur后继改为node

    # 删除元素
    def remove(self, item):
        # 如果是空表，不操作
        if self.is_empty():
            return
        # 不为空
        else:
            # 扫描指针，从头开始
            cursor = self._head
            # 如果头结点就是要删除的结点
            if cursor.elem == item:
                # 如果只有一个结点，链表就空了
                if self.length() == 1:
                    self._head = None
                # 如果有多个元素
                else:
                    self._head = cursor.next  # 头指针指向cursor的下一个元素
                    cursor.next.prev = cursor.prev  # cursor后继的前驱改为cursor的前驱
                    cursor.prev.next = cursor.next  # cursor前驱的后继改为cursor的后继
            # 头结点不是要删除的结点
            else:
                cursor = cursor.next
                while cursor is not self._head:
                    # 如果找到了要删除的结点
                    if cursor.elem == item:
                        cursor.prev.next = cursor.next  # cursor的前驱的后继改为cursor的后继
                        cursor.next.prev = cursor.prev  # cursor的后继的前驱改为cursor的前驱
                    cursor = cursor.next

    #搜索节点是否存在
    def search(self, item):
    #如果链表是空的一定不存在
        if self.is_empty():
            return False
        #否则链表不空
        else:
            cursor = self.__head #设置临时cur从头开始
            # cursor不断后移，一直到尾节点为止
            while cur.next is not self.__head:
                #如果期间找到了就返回一个True 结束运行
                if cur.item == item:
                    return True
                cur = cur.next
            # 从循环跳出来cursor就指向了尾元素 看一下为元素是不是要找的 是就返回True
            if cur.item ==item:
                return True
        #所有元素都不是 就返回False 没找到
        return False








    '''遍历'''
    # 操作链表的每个元素，把函数作为参数传入函数
    def for_each(self, func):
        # 如果为空
        if self._head is None:
            return
        # 循环指针，初始化为链表的头部
        cursor = self._head
        while cursor.next is not self._head:
            func(cursor.elem)
            cursor = cursor.next
         # 跳出循环时，cursor走到了最后一个结点，于是cursor.next=self._head
         # 导致最后一个结点没有得到打印，则跳出循环后把它打印出来
        print(cursor.elem)
