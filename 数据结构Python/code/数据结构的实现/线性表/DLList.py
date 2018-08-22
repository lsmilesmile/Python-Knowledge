'''双链表'''
from LList import LNode, LinkedListUnderflow
from LList1 import LList1

# 双链表结点类
class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev

class DLList(LList1):

    def __init__(self):
        LList1.__init__(self)

    # 头插法
    def prepend(self, elem):
        # 先设置next域，指向head指向的结点
        p = DLNode(elem, None, self._head)
        # 如果是空表
        if self._head is None:
            self._rear = p
        # 不是空表
        else:
            # 再设置之前第一个结点的prev域的值，指向新加入的这个结点
            p.next.prev = p
        self._head = p

    # 尾插法
    def append(self, elem):
        # 先设置prev指针域，让prev指向之前的最后一个结点
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            # 在设置以前最后一个结点的next域，让其指向新的结点
            p.prev.next = p
        self._rear = p

    # 删除第一个结点
    def pop(self):
        # 如果是空表
        if self._head is None:
            raise LinkedListUnderflow('空表')
        # 保存被删除的元素
        e = self._head.elem
        # 让链表的头指针指向第二个结点
        self._head = self._head.next
        if self._head is not None:
            # 把第二个结点的prev指针设为空
            self._head.prev = None
        return e

    # 删除尾结点
    def deltail(self):
        if self._head is None:
            raise LinkedListUnderflow('空表')
        e = self._rear.elem
        # 让表尾指针指向倒数第二个结点
        self._rear = self._rear.prev
        # 如果删除了一个结点后，没有结点了
        if self._rear is None:
            self._head = None
        else:
            # 把倒数第二个结点的next设为None
            self._rear.next = None
        return e


if __name__ == '__main__':

    # 创建双链表对象
    dllist = DLList()

    # 头插法
    for i in range(1, 4):
        dllist.prepend(i)

    # 尾插法
    for i in range(4, 7):
        dllist.append(i)

    # 删除第一个结点
    dllist.pop()

    # 输出所有
    dllist.for_each(print)

