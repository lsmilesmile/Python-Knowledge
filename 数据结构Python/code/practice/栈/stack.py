# 结点类
class LNode(object):

    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

# 错误类
class StackUnderflow(ValueError):
    pass

# 栈 - 顺序表实现
class SStack(object):
    
    def __init__(self):
        # 首段为栈底，尾端为栈顶
        self._elems = []  # 用list对象_elems存储栈中元素，所有操作都映射到list操作

    def is_empty(self):
        return self._elems == []

    # 取得栈顶元素的值，不删除
    def top(self):
        if self._elems == []:
            raise StackUnderflow("无元素")
        return self._elems[-1]

    # 向栈顶压入元素
    def push(self, elem):
        self._elems.append(elem)

    # 弹出栈顶元素，删除
    def pop(self):
        if self._elems == []:
            raise StackUnderflow('无元素')
        return self._elems.pop()

# 栈 - 单链表实现，LNode作为结点
class LStack(object):

    def __init__(self):
        # 栈顶
        self._top = None

    def is_empty(self):
        return self._top is None

    # 得到栈顶元素
    def top(self):
        if self._top is None:
            raise StackUnderflow('空表')
        return self._top.elem

    # 元素进栈 - 头插法
    def push(self, elem):
        self._top = LNode(elem, self._top)

    # 弹出元素
    def pop(self):
        if self._top is None:
            raise StackUnderflow('空表')
        # p指向要删除的结点
        p = self._top
        self._top = p.next
        return p.elem
