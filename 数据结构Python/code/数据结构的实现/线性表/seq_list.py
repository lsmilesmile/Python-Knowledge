#顺序表类
class seq_list(object):
    #顺序表的最大容量、元素个个数、存放数据的数组
    def __init__(self, max = 10):
        self.max = max
        self.num = 0
        self.data = [None] * self.max
        #self.data = [''] * self.max

    #输出线性表中的数据
    def __str__(self):
        return " ".join((str(self.max), str(self.num), str(self.data)))

    #判断空
    def is_empty(self):
        return self.num is 0

    #判断是否满了
    def is_full(self):
        return self.num is self.max

    #获取线性表的长度，既元素 个数
    def count(self):
        return self.num


    #在线性表的末尾增加一个元素
    def append(self, element):
        #先判断表是否满了
        if self.num == self.max:
            print("表已经满了！操作失败！")
            return
        else:
            self.data[self.num] = element
            self.num += 1

    #在线性表下表为loc的位置添加元素，而不是插在第几个
    def insert(self, loc, value):
        #判断表是否满了
        if self.is_full():
            print('表已经满了！')
            return
        elif loc < 0:
            raise IndexError('下标错误')
        else:
           for i in range(self.num, loc, -1):
               self.data[i] = self.data[i-1]
           self.data[loc] = value
           self.num += 1

    #查找
    #查找所有值为value的元素并返回下标，把下标放在列表里
    def search(self, value):
        for i in range(0, self.num):
            if self.data[i] == value:
                yield i
    #查找第一个元素值为value的值的下标并返回
    def search(self, value):
        for i in range(0, self.num):
            if self.data[i] == value:
                return i


    #删除
    #删除下表为loc的元素
    def delete_l(self, loc):
        if loc < 0 or loc > self.num - 1:
            raise IndexError
        else:
            for i in range(loc, self.num):
                self.data[i] = self.data[i+1]
            self.num -= 1

    #删除所有值为value的元素
    def delete_v(self, value):
        j = 0 #记录删除的个数
        #先看值是否存在
        for i in range(self.num):
            if self.data[i] == value:
                self.delete_l(i)
                j += 1
        if j == 0:
            return '不存在该'

    # 顺序表反转
    def reverse(self):
        # 扫描指针，分别放在首尾
        i, j = 0, self.num - 1
        while i < j:
            self.data[i], self.data[j] = self.data[j], self.data[i]
            i, j = i + 1, j - 1

    # 输出元素
    def showall(self):
        for i in range(self.num):
            if i < self.num - 1:
                print(self.data[i], end=',')
        print(self.data[i])
        print()





seq = seq_list()
# print(seq)
# print(seq.is_empty())
# print(seq.is_full())
# for i in range(5):     #加入元素
#     seq.append(i)
# 在c语言的顺序表中一个表中 只能放类型相同的元素，在这可以放各种不同的元素
# seq.append([x * x for x in range(3)])
# seq.append('felix')
# print(seq.count())     #统计个数

# 插入元素
# seq.insert(2, 4)
#
# seq.showall()
#
# print('-' * 10)
#
# seq.reverse()
# for j in range(seq.num):  #输出目前的元素
#     print(seq.data[j])
# print(seq.count())
# seq.delete_l(2)
# for j in range(seq.num):
#     print(seq.data[j])
# print(seq.count())
# print(type(seq.data[2]))
# print(seq.search('two'))
# print(list(seq.search(4)))