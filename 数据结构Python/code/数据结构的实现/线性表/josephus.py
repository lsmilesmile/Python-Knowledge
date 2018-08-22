from LCList import LCList

class Josephus(object):

    def __init__(self, value1, value2, value3):
        self.n = value1
        self.k = value2
        self.m = value3

    # 数组思想实现
    def josephus_A(self):
        # 创建n个人的列表
        people = list(range(1, self.n + 1))

        # 找到第k个人，i表示数组下标
        i = self.k - 1
        # 因为游戏的最终结局是所有的人都退出，所以循环n此
        for num in range(self.n):
            # 计数
            count = 0
            while count < self.m:
                # 如果该报数的人的那个位置还有人，即没有退出的话
                if people[i] > 0:
                    count += 1
                # 报到m的人退出
                if count == self.m:
                    print(people[i], end="")
                    # 这个人退出了则该位置的值设为0
                    people[i] = 0
                # 下一轮从下一个人开始报数
                i = (i + 1) % self.n
            # 如果还有人没退出，打一个逗号留着输出下一个退出的人
            if num < self.n - 1:
                print(", ", end="")
            else:
                print("")
        return

    # 顺序表的解
    def josephus_L(self):
        people = list(range(1, self.n+1))

        num, i = self.n, self.k-1
        for num in range(self.n, 0, -1):
            i = (i+self.m-1) % num
            print(people.pop(i),
                end=(", " if num > 1 else "\n"))
        return

# 循环单链表解决
class Josephus1(LCList):
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop(),
                end=("\n" if self.is_empty() else ", "))


if __name__ == '__main__':
    j1 = Josephus(50, 7, 4)
    j2 = Josephus1(50, 7, 4)
    j1.josephus_A()
    j1.josephus_L()
