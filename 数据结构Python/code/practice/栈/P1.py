from stack import SStack

'''栈的应用'''

'''括号匹配问题
    处理过程：
    1、顺序扫描被检查正文里的一个个字符
    2、检查中跳过无关字符
    3、遇到开括号时将其压入栈
    4、遇到闭括号时弹出当时的栈顶元素与之匹配
    5、如果匹配成功则继续，发现不匹配时检查以失败结束
    '''
def check_parens(text):
    parens = "()[]{}"  # 括号字符
    open_parens = "([{"  # 开括号字符
    opposite = {')' : '(', ']' : '[', '}' : '{'}  # 表示匹配关系的字典

    def parantheses(text):
        # 括号生成器，每次调用返回text里的下一括号及其位置
        i, text_len = 0, len(text)
        while True:
            # 从位置0开始扫描字符串，如果不是括号的符号就继续向后扫描
            while i < text_len and text[i] not in parens:
                i += 1
            # 扫描完整个字符串，则结束
            if i >= text_len:
                return
            # 以上都不符合，那么就是扫描到了括号，返回一个括号符号
            yield text[i], i
            i += 1  # 继续扫描下一个

    st = SStack()  # 保存括号的栈

    for pr, i in parantheses(text):  # 对text里的各括号和位置迭代
        if pr in open_parens:  # 从括号生成器中拿出来的括号符号是开括号，压进栈并继续
            st.push(pr)
        # 不是开括号就是闭括号，这时弹出栈里面的括号，看是否和当前括号匹配
        elif st.pop() != opposite[pr]:
            print('Unmatching is found at', i, 'for', pr)
            return False
        # else:  # 成功的匹配，啥也不做，继续
    print('All parentheses are correctly matched.')
    return True


'''表达式计算
    中缀表达式：(3-5)*(6+17*4)/3
    前缀表达式：/ * - 3 5+ 6 * 17 4 3 （）
    后缀表达式：3 5 - 6 17 4 * + * 3 /（数字入栈，是运算符就把栈中的前两个元素拿出来计算）
'''
'''1、后缀表达式的计算'''
    # 由于1、如果占中元素不足两个，那么操作失败；
    # 2、处理完表达式时，栈里应该只剩下计算结果。
    # 以上两个操作要知道栈的深度，所以定义扩充功能的栈类，增加此方法，继承自LLstack
class  ESStack(SStack):
    def depth(self):
        return len(self._elems)

def suf_exp_evaluator(exp):  # exp是一个含有算术各项的列表，被处理过的
    operation = "+-*/"  # 运算符号，这里只讨论这四种
    st = ESStack()  # 定义扩充了求栈深度的功能的栈类对象

    for x in exp:
        # 如果x不是运算符，则转换成浮点数入栈
        if x not in operation:
            st.push(float(x))  # 不能转换将自动引发异常
            continue
        # 上面取得的是运算符，就看栈中的数字是不是少于两个，如果栈中元素少于两个，出错
        if st.depth() < 2:
            raise SyntaxError('Short of operand(s).')
        # x是运算符，则取出栈中的顶端的两个数字计算
        a = st.pop()  # 取出第二个运算对象
        b = st.pop()  # 取出第一个运算对象

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        else:  # 不可能出现该情况，只是为了格式清晰
            break

        # 把计算结果压入栈
        st.push(c)

        # 经过上面过程后，如果栈中只剩一个元素，则就是计算结果，弹出
        if st.depth() == 1:
            return st.pop()
        # 如果上面过程都经历了，且最后剩下的元素个数不止一个，也报错
        raise SyntaxError('Extra operand(s)')

# 后缀表达式 - 模拟交互式
def suffix_exp_calculator():
    while True:
        try:
            line = input("请输入后缀表达式：")
            if line == "end":
                return
            # 当我们输入后缀表达式时，为了不让几个数字连在一起，就会用空格隔开，
            # 所以用split()函数去空格，把空格隔开每个字符串放入列表中
            line_list = line.split()
            res = suf_exp_evaluator(line_list)
            print(res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)

'''中缀表达式 - > 后缀表达式'''
priority = {'(':1, '+':3, '-':3, '*':5,, '/':5}
infix_operatios = '+-*/()'  # 运算符，把'(',')'也看做特殊的运算符

def trans_infix_suffix(line):
    st = SStack()
    exp = []  # 记录转换得到的后缀表达式，采用项表的形式

    for x in token(line):
        if x not in infix_operatios:
            pass

# 本函数不能处理一元运算符，也不能处理带符号的浮点数
def tokens(line):
    # 生成器函数，逐一生成line中的一个个项，项是浮点数或者运算符
    i, llen = 0, len(line)
    while i < llen:
        while lline[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operatios:
            yield line[i]
            i += 1
            continue

        j = i + 1

        while (j < llen and not line[j].isspace() and
            line[j] not in infix_operatios):
            if ((line[j] == 'e' or line[j] == 'E')
                and j + 1 < llen and line[j+1] == '-'):
                j += 1
            j += 1
        yield line[i:j]
        i = j








if __name__ == '__main__':

    # 括号匹配
    # text = '{faf[da(1,2,3),5]},3'
    # check_parens(text)

    # 后缀表达式 - 模拟交互式
    suffix_exp_calculator()




