'''单链表类'''

# 操作的错误类
class LinkedListUnderflow(ValueError):
    pass

# 结点类
class LNode(object):

    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

# 单链表类
class LList(object):

    def __init__(self):
        self._head = None

    # 判断是否为空
    def is_empty(self):
        return self._head is None

    # 求表的长度
    def length(self):
        p, n = self._head, 0
        while p is not  None:
            n += 1
            p = p.next
        return n

    # 打印出表的所有元素
    ## 方式一
    def show_all(self):
        # p是循环指针
        p = self._head
        # 如果是空表
        if p is None:
            raise LinkedListUnderflow('该表是空表')
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(',', end='')
            p = p.next
        print('')

    ## 方式二
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def showall(self):
        for x in self.elements():
            print(x, end=',')
        print()

    '''插入'''
    # 头插法
    def prepend(self, elem):
        # 分两步：
        # 1.LNode(elem, self._head) - 该结点的链接域先指向self._head指向的结点；
        # 2.self._head指向新加的这个结点
        self._head = LNode(elem, self._head)

    # 尾插法
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    # 任意位置插入
    # 将数值value插入到第i个元素后面
    def insert_i(self, value, i):
        lnode = LNode(value)
        p, n = self._head, i-1
        while p is not None and n > 0:
            p = p.next
            n -= 1
        lnode.next = p.next
        p.next = lnode

    # 将value插入到第一个值为value1的结点的后面
    def insert_value(self, value, value1):
        if self._head is None:
            raise LinkedListUnderflow('该表是空表')
        p = self._head
        while p is not None:
            if p.elem == value1:
                lnode = LNode(value)
                lnode.next = p.next
                p.next = lnode
                return
            p = p.next
        return '不存在该值，操作失败'


    '''删除'''
    # 删除表头结点，并返回该结点的数据域中的值
    def pop(self):
        # 无结点情况
        if self._head is None:
            raise LinkedListUnderflow("表中无结点")
        # 有结点
        value = self._head.elem
        self._head = self._head.next

    # 删除表尾结点
    def deltail(self):
        # 如果是空链表
        if self._head == None:
            raise LinkedListUnderflow('该表是空表，非法操作')
        #如果链表只有一个结点，那就是删除头结点
        p = self._head
        if p.next == None:
            e = p.elem
            self._head = None
            return e
        else:
            # 检查当前p指向的下一个结点的下一个结点是否是最后一个结点
            while p.next.next is not None:
                p = p.next
            # 如果p.next.next是None，说明p.next所指的结点就是最后一个结点
            e = p.next.elem
            p.next = None
            return e

    # 删除任意位置结点
    # 删除表中第k个结点
    def delete_k(self, k):
        if k < 0 or k == 0: 
            raise LinkedListUnderflow('请输入大于0的数字！')
        elif k == 1:
            self.pop()
        else:
            p, n = self._head, k-1
            # n>1是为了找到第k个结点的前一个结点
            while p is not None and n > 1:
                p = p.next
                n -= 1
            p.next = p.next.next

    # 删除链表
    def delete(self):
        self._head = None

    '''修改'''


    '''查找'''
    # 找到满足条件condition的元素
    def filter(self, condition):
        p = self._head
        while p is not None:
            if condition(p.elem):
                yield p.elem
            p = p.next

    '''遍历'''
    # 操作链表的每个元素，把函数作为参数传入函数
    def for_each(self, func):
        p = self._head
        while p is not None:
            func(p.elem)
            p = p.next

    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next  # 摘下原来的首结点
            q.next = p
            p = q  # 将刚摘下的结点加入p引用的结点序列
        self._head = p  # 反转后的结点序列已经做好，重置表头链接
    


    def test1(self, value):
        print(value * 2, end=',')

    def test2(self, value):
        if value == 4:
            return True
        else:
            return False





if __name__ == '__main__':
    # 建立一个空的单链表
    a_List = LList()

    # 把1~13不断地接到单链表上
    for i in range(6):
        a_List.prepend(i)

    # 求表的长度
    print(a_List.length())


    # 打印出单链表a_List的元素
    print(a_List.for_each(a_List.test1))

    # 把'felix'插入到第三个位置
    a_List.insert_i(123, 3)

    # 打印出单链表a_List的元素
    # a_List.show_all()
    a_List.showall()

    # 反转
    a_List.rev()
    a_List.showall()

    # 删除第1个结点
    a_List.delete_k(1)

    # 打印出单链表a_List的元素
    a_List.show_all()

    # 删除最后一个结点
    # a_List.deltail()

    # 删除知道只剩一个结点
    for i in range(a_List.length()-1):
        print(a_List.deltail(), end=',')

    # 打印出单链表a_List的元素
    a_List.show_all()

    # 在表的尾部插入4
    a_List.append(4)
    a_List.show_all()

    # 把3查到4前面
    a_List.insert_value(3, 4)

    a_List.show_all()

    # 筛选生成器(用生成器对象.__next__()  或  next(生成器对象))来输出生成器中的元素
    print(a_List.filter(a_List.test2).__next__())
    print(a_List.filter(a_List.test2).__next__())

    # 删除头结点
    # a_List.pop()
    # print('-' * 10)

    # 删除链表
    # a_List.delete()

    # 判断表是否是空表
    print(a_List.is_empty())
    