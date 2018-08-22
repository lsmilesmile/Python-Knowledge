'''增加了尾结点引用的单链表，继承自一般的单链表类LList'''
from LList import LList, LNode, LinkedListUnderflow

class LList1(LList):
    
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    # 头插法
    def prepend(self, elem):
        if self._head is None:  # 如果是空表
            # LNode(elem, self._head) - 先让新结点的引用域指向原来头指针指向的地方
            # 再让头指针指向新的结点
            self._head = LNode(elem, self._head)
            # 头指针和尾结点的指针都指向新的结点
            self._rear = self._head
        # 不是空表
        else:
            self._head = LNode(elem, self._head)

    # 尾插法
    def append(self, elem):
        # 如果是空表
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            # 先让尾结点的引用域指向新增加的结点
            # 再让尾结点指针指向新的结点
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    # 弹出第一个元素
    def pop(self):
        # 如果是空表
        if self._head is None:
            raise LinkedListUnderflow('该表中没有元素')
        # 不是空表
        # 如果只有一个元素，则头指针和尾指针都指向None
        elif self._head.next == None:
            self._head = self._head.next
            self._rear = self._head
        # 不只一个元素，丢弃第一个结点
        else:
            self._head = self._head.next
    
    def deltail(self):
        # 如果是空表
        if self._head is None:
            raise LinkedListUnderflow('该表中没有元素')
        # 扫描指针
        p = self._head
        # 表中只有一个元素
        if self._head.next is None:
            e = p.elem
            self._head = None
            return e
        # 找到最后一个结点
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e




if __name__ == '__main__':

    # 创建空的链表
    llist1 = LList1()

    # 头插法插入数据
    for i in range(1, 4):
        llist1.prepend(i)

    # 尾插法插入数据
    for i in range(4, 7):
        llist1.append(i)

    # 打印所有数据，用LList类的for_each()函数
    llist1.for_each(print)

    # 删除表尾元素
    llist1.deltail()

    llist1.for_each(print)  

    print(llist1.length())