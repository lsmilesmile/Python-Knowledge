'''给LList增加一个元素计数值域
自定义函数__len__(),来求元素个数'''

# 操作的错误类
class LinkedListUnderflow(ValueError):
    pass
# 结点类
class LNode(object):

    def __init__(self, elem=0, next_=None):
        self.elem = elem
        self.next = next_

class LList(object):

    def __init__(self, lnode):
        # 初始化链表有一个头指针和计数结点
        self.num_node = lnode
        self._head = self.num_node

    # 求长度
    def __len__(self):
        p, n = self._head.next, 0
        while p is not None:
            n += 1
            p = p.next
        return n

    # 尾插法
    def append(self, elem):
        if self._head.next is None:
            self._head.next = LNode(elem)
            self.num_node.elem += 1
            return
        p = self.num_node
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
        self.num_node.elem += 1

    # 打印出表的所有元素
    def show_all(self):
        # p是循环指针
        p = self._head.next
        # 如果是空表
        if p is None:
            raise LinkedListUnderflow('该表是空表')
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(',', end='')
            p = p.next
        print('')

if __name__ == '__main__':

    lnode = LNode()
    llist = LList(lnode)
    for i in range(1, 11):
        llist.append(i)
    llist.show_all()
    print(llist.num_node.elem)
    print(len(llist))

