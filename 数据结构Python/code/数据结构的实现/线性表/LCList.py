from LList import LNode, LinkedListUnderflow

'''循环单链表'''
class LCList(object):

    def __init__(self):
        # 只有一个尾结点指针
        self._rear = None

    # 判断是否是空表
    def is_empty(self):
        return self._rear is None

    # 求表的长度
    def length(self):
        # p - 循环指针，从头开始，n - 计数
        p, n = self._rear.next, 0
        while True:
            if p.next is self._rear.next:
                break
            else:
                n += 1
                p = p.next
        return n + 1

    # 头插法
    def prepend(self, elem):
        # 把要插入的数据放入一个结点
        p = LNode(elem)
        # 如果是空表，建立循环
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    # 尾插法
    def append(self, elem):
        # 由于循环的单链表头尾没有明确的概念，所以先在前面插入一个
        self.prepend(elem)
        # 再将尾结点指向刚才新插入的那个结点
        self._rear = self._rear.next

    # 前端弹出
    def pop(self):
        # 如果是空表
        if self._rear is None:
            raise LinkedListUnderflow('空表')
        # p保存要弹出的结点
        p = self._rear.next
        # 如果只有一个结点
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        # 返回要删除的元素
        return p.elem

    # 尾端弹出
    def deltail(self):
        # 如果是空表
        if self._rear is None:
            raise LinkedListUnderflow('空表')
        # 扫面指针，从头开始
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            while p.next.next is not self._rear.next:
                p = p.next
            # return p.next.elem
            p.next = self._rear.next
            self._rear = p



    # 输出所有元素
    def showall(self):
        if self.is_empty():
            return
        # 循环指针，先放在开头
        p = self._rear.next
        while True:
            # 注意这儿是先打印再判断p到哪了
            print(p.elem)
            # 如果p移动到了结尾
            if p is self._rear:
                break
            p = p.next

if __name__ == '__main__':
    lclist = LCList()

    # 头插
    for i in range(1, 4):
        lclist.prepend(i)

    # 尾插
    for i in range(4, 7):
        lclist.append(i)

    # 从头删除
    lclist.pop()

    # 尾部删除
    lclist.deltail()

    # 输出所有
    lclist.showall()

    print(lclist.length())
