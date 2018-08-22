import random

from seq_list import seq_list
from LList import LList

class sort(object):

    # 顺序表的排序
    def for_seq(self, seq):
        for i in range(1, seq.num):
            x = seq.data[i]
            j = i
            while j > 0 and seq.data[j-1] > x:
                seq.data[j] = seq.data[j-1]
                j -= 1
            seq.data[j] = x

    # 单链表排序 - 调成元素
    def for_llist(self, llist):
        if llist._head is None:
            return
        crt = llist._head.next  # 从首结点之后的位置开始处理
        while crt is not None:
            x = crt.elem
            p = llist._head
            while p is not crt and p.elem <= x:  # 跳过小元素
                p = p.next
            while p is not crt:  # 倒换大元素，完成元素的插入工作
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next

    # 单链表排序 - 调整结点
    def for_list1(self, llist):
        p = llist._head
        if p is None or p.next is None:
            return

        rem = p.next
        p.next = None
        while rem is not None:
            p = llist._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                llist._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p


if __name__ == '__main__':

    # 创建顺序表对象
    seq1 = seq_list()
    # 创建单链表对象
    llist = LList()
    # 创建排序对象
    sort_temp = sort()

    # 向顺序表中插入数据
    for i in range(seq1.max):
        seq1.append(random.randint(1, 50))

    # 向单链表中插入数据
    for i in range(10):
        llist.append(random.randint(1, 100))

    # 输出顺序表数据
    # seq1.showall()

    # 输出单链表数据
    llist.show_all()

    # 排序后输出顺序表
    # sort_temp.for_seq(seq1)
    # seq1.showall()

    # 排序后输出单链表数据
    sort_temp.for_list1(llist)
    llist.show_all()

