# 正则表达式

[TOC]



## 1 - 特殊符号和字符

​	常见的特殊符号和字符，即所谓的元字符，正式它给予正则表达式强大的功能和灵活性。

**常见正则表达式符号和特殊字符**

|    表 示 法    |                            描 述                             |     正则表达式示例      |
| :------------: | :----------------------------------------------------------: | :---------------------: |
|      符号      |                                                              |                         |
|    literal     |                匹配文本字符串的字面值 literal                |           foo           |
|    re1\|re2    |                 匹配正则表达式 re1 或者 re2                  |        foo\|bar         |
|       .        |                 匹配任何字符（除了\n 之外）                  |           b.b           |
|       ^        |                      匹配字符串起始部分                      |          ^Dear          |
|       $        |                      匹配字符串终止部分                      |        /bin/*sh$        |
|       *        |            匹配 0 次或者多次前面出现的正则表达式             |      [A-Za-z0-9]*       |
|       +        |            匹配 1 次或者多次前面出现的正则表达式             |       [a-z]+\.com       |
|       ?        |            匹配 0 次或者 1 次前面出现的正则表达式            |          goo?           |
|      {N}       |                匹配 N 次前面出现的正则表达式                 |        [0-9]{3}         |
|     {M,N}      |               匹配 M～N 次前面出现的正则表达式               |       [0-9]{5,9}        |
|      […]       |                 匹配来自字符集的任意单一字符                 |         [aeiou]         |
|   [..x-y..]    |                匹配 x～y 范围中的任意单一字符                |     [0-9], [A-Za-z]     |
|      [^…]      | 不匹配此字符集中出现的任何一个字符，包括某一范围的字符（如果在此字符集中出现） | [^aeiou], [^A-Za-z0-9]  |
| (*\|+\|?\|{})? | 用于匹配上面频繁出现/重复出现符号的非贪婪版本（*、 +、 ?、 {}） |        .*?[a-z]         |
|      (…)       |             匹配封闭的正则表达式，然后另存为子组             | ([0-9]{3})?,f(oo\|u)bar |

|     表 示 法      |                            描 述                             |  正则表达式示例   |
| :---------------: | :----------------------------------------------------------: | :---------------: |
|     特殊字符      |                                                              |                   |
|        \d         | 匹配任何十进制数字，与[0-9]一致（\D 与\d 相反，不匹配任何非数值型的数字） |    data\d+.txt    |
|        \w         |   匹配任何字母数字字符，与[A-Za-z0-9_]相同（\W 与之相反）    |   [A-Za-z_]\w+    |
|        \s         |     匹配任何空格字符，与[\n\t\r\v\f]相同（\S 与之相反）      |      of\sthe      |
|        \b         |               匹配任何单词边界（\B 与之相反）                |      \bThe\b      |
|        \N         |              匹配已保存的子组 N（参见上面的(…))              |    price: \16     |
|        \c         | 逐字匹配任何特殊字符 c（即，仅按照字面意义匹配，不匹配特殊含义） |    \., \\, \*     |
|      \A(\Z)       |        匹配字符串的起始（结束）（另见上面介绍的^和$）        |      \ADear       |
|    扩展表示法     |                                                              |                   |
|     (?iLmsux)     | 在正则表达式中嵌入一个或者多个特殊“标记” 参数（或者通过函数/方法） | （?x），（？ im） |
|       (?:…)       |                  表示一个匹配不用保存的分组                  |    (?:\w+\.)*     |
|   (?P\<name>…)    |     像一个仅由 name 标识而不是数字 ID 标识的正则分组匹配     |    (?P\<data>)    |
|     (?P=name)     |         在同一字符串中匹配由(?P<name)分组的之前文本          |     (?P=data)     |
|       (?#…)       |                  表示注释，所有内容都被忽略                  |    (?#comment)    |
|       (?=…)       | 匹配条件是如果…出现在之后的位置，而不使用输入字符串；称作正向前视断言 |     (?=.com)      |
|       (?!…)       | 匹配条件是如果…不出现在之后的位置，而不使用输入字符串；称作负向前视断言 |     (?!.net)      |
|      (?<=…)       | 匹配条件是如果…出现在之前的位置，而不使用输入字符串；称作正向后视断言 |     (?<=800-)     |
|      (?<!…)       | 匹配条件是如果…不出现在之前的位置，而不使用输入字符串；称作负向后视断言 |  (?<!192\.168\.)  |
| (?(id/name)Y\|N ) | 如果分组所提供的 id 或者 name（名称）存在，就返回正则表达式的条件匹配 Y，如 果不存在，就返回 N； \|N 是可选项 |    (?(1)y\|x)     |

###  1.1 使用择以匹配符号匹配多个正则表达式模式

​	表示择一匹配的管道符号（|），也就是键盘上的竖线，表示一个“从多个模式中选择其 一”的操作。它用于分割不同的正则表达式。     

|  正则表达式模式   |  匹配的字符串   |
| :---------------: | :-------------: |
|    at \| home     |    at、 home    |
|   r2d2 \| c3po    |   r2d2、 c3po   |
| bat \| bet \| bit | bat、 bet、 bit |

###  1.2 匹配任意单个字符

​	点号或者句点（.） 符号匹配除了换行符\n 以外的任何字符（Python 正则表达式有一个编译标记[S 或者 DOTALL]，该标记能够推翻这个限制，使点号能够匹配换行符）。无论字母、 数字、空格（并不包括“\n”换行符）、可打印字符、不可打印字符，还是一个符号，使用点 号都能够匹配它们。    

 

| 正则表达式模式 |                         匹配的字符串                         |
| :------------: | :----------------------------------------------------------: |
|      f.o       | 匹配在字母“f”和“o”之间的任意一个字符；例如 fao、 f9o、 f#o 等 |
|       ..       |                         任意两个字符                         |
|      .end      |             匹配在字符串 end 之前的任意一个字符              |

 **注：要显式匹配一个句点符号本身，必须使用反斜线转义句点符号的功能，例如“\\.”。**    

### 1.3 从字符串起始或者结尾或者单词边界匹配

​	还有些符号和相关的特殊字符用于在字符串的起始和结尾部分指定用于搜索的模式。如 果要匹配字符串的开始位置，就必须使用脱字符（^）或者特殊字符\A（反斜线和大写字母 A）。 后者主要用于那些没有脱字符的键盘（例如，某些国际键盘）。同样，美元符号（$）或者\Z 将用于匹配字符串的末尾位置。    

| 正则表达式模式 |                匹配的字符串                 |
| :------------: | :-----------------------------------------: |
|     ^From      |        任何以 From 作为起始的字符串         |
|   /bin/tcsh$   |      任何以/bin/tcsh 作为结尾的字符串       |
| ^Subject: hi$  | 任何由单独的字符串 Subject: hi 构成的字符串 |

 	特殊字符\b 和\B 可以用来匹配字符边界。而两者的区别在于\b 将用于匹配一个单词的边 界，这意味着如果一个模式必须位于单词的起始部分，就不管该单词前面（单词位于字符串 中间）是否有任何字符（单词位于行首）。同样， \B 将匹配出现在一个单词中间的模式（即， 不是单词边界）。    

| 正则表达式模式 |             匹配的字符串              |
| :------------: | :-----------------------------------: |
|      the       |         任何包含 the 的字符串         |
|     \bthe      |        任何以 the 开始的字符串        |
|    \bthe\b     |           仅仅匹配单词 the            |
|     \Bthe      | 任何包含但并不以 the 作为起始的字符串 |

###  1.4 创建字符集

​	尽管句点可以用于匹配任意符号，但某些时候，可能想要匹配某些特定字符。正因如此， 发明了方括号。该正则表达式能够匹配一对方括号中包含的任何字符。    

 

|   正则表达式模式    |                         匹配的字符串                         |
| :-----------------: | :----------------------------------------------------------: |
|      b[aeiu]t       |                    bat、 bet、 bit、 but                     |
| \[cr]\[23]\[dp][o2] | 一个包含四个字符的字符串，第一个字符是“c”或“r”，然后是“2”或“3”，后面 是“d”或“p”，最后要么是“o”要么是“2”。例如， c2do、 r3p2、 r2d2、 c3po 等 |

###  1.5 限定范围和否定

​	除了单字符以外，字符集还支持匹配指定的字符范围。方括号中两个符号中间用连字符 （-）连接，用于指定一个字符的范围；例如， A-Z、 a-z 或者 0-9 分别用于表示大写字母、小 写字母和数值数字。这是一个按照字母顺序的范围，所以不能将它们仅仅限定用于字母和十 进制数字上。另外，如果脱字符（^）紧跟在左方括号后面，这个符号就表示不匹配给定字符 集中的任何一个字符。  

|   正则表达式模式   |                         匹配的字符串                         |
| :----------------: | :----------------------------------------------------------: |
|      z.[0-9]       |        字母“z”后面跟着任何一个字符，然后跟着一个数字         |
| \[r-u]\[env-y][us] | 字母“r”、“s”、“t”或者“u”后面跟着“e”、“n”、“v”、“w”、“x”或者“y”，然后跟着“u”或者“s” |
|      [^aeiou]      |  一个非元音字符（练习：为什么我们说“非元音”而不是“辅音”？）  |
|      [^\t\n]       |                      不匹配制表符或者\n                      |
|       [“-a]        | 在一个 ASCII 系统中，所有字符都位于“”和“a”之间，即 34~97 之间 |

###  1.6 使用闭包操作符实现存在性和频数匹配

​	符号*、 +和？，所有这些都可以用于匹配一 个、 多个或者没有出现的字符串模式。星号或者星号操作符（*）将匹配其左边的正则表达式 出现零次或者多次的情况（在计算机编程语言和编译原理中，该操作称为 Kleene 闭包）。加 号（+）操作符将匹配一次或者多次出现的正则表达式（也叫做正闭包操作符），问号（？） 操作符将匹配零次或者一次出现的正则表达式。 

​	还有大括号操作符（{}），里面或者是单个值或者是一对由逗号分隔的值。这将最终精 确地匹配前面的正则表达式 N 次（如果是{N}）或者一定范围的次数；例如， {M， N}将匹 配 M～N 次出现。这些符号能够由反斜线符号转义； \*匹配星号，等等。 注意，在之前的表格中曾经多次使用问号（重载），这意味着要么匹配 0 次，要么匹配 1 次，或者其他含义：如果问号紧跟在任何使用闭合操作符的匹配后面，它将直接要求正则表 达式引擎匹配尽可能少的次数。 

​	“尽可能少的次数”是什么意思？当模式匹配使用分组操作符时，正则表达式引擎将试图 “吸收”匹配该模式的尽可能多的字符。这通常被叫做贪婪匹配。问号要求正则表达式引擎去 “偷懒”，如果可能，就在当前的正则表达式中尽可能少地匹配字符，留下尽可能多的字符给 后面的模式（如果存在）。    

|          正则表达式模式          |                         匹配的字符串                         |
| :------------------------------: | :----------------------------------------------------------: |
|             [dn]ot?              | 字母“d”或者“n”，后面跟着一个“o”，然后是最多一个“t”，例如， do、 no、 dot、 not |
|             0?[1-9]              | 任何数值数字， 它可能前置一个“0”，例如，匹配一系列数（表示从 1～9 月的数值），不 管是一个还是两个数字 |
|           [0-9]{15,16}           |           匹配 15 或者 16 个数字（例如信用卡号码）           |
|            </?[^>]+>             |             匹配全部有效的（和无效的） HTML 标签             |
| \[KQRBNP]\[a-h][1-8]-\[a-h][1-8] | 在“长代数”标记法中，表示国际象棋合法的棋盘移动（仅移动，不包括吃子和将军）。 即“K”、“Q”、“R”、“B”、“N”或“P”等字母后面加上“a1”～“h8”之间的棋盘坐标。 前面的坐标表示从哪里开始走棋，后面的坐标代表走到哪个位置（棋格）上 |

###  1.7 表示字符集的特殊字符

​	我们还提到有一些特殊字符能够表示字符集。与使用“0-9”这个范围表示十进制数相比， 可以简单地使用 d 表示匹配任何十进制数字。另一个特殊字符（\w） 能够用于表示全部字母 数字的字符集，相当于[A-Za-z0-9_]的缩写形式， \s 可以用来表示空格字符。这些特殊字符的 大写版本表示不匹配；例如， \D 表示任何非十进制数（与[^0-9]相同）， 等等。 使用这些缩写，可以表示如下一些更复杂的示例。    

 

|  正则表达式模式   |                       匹配的字符串                       |
| :---------------: | :------------------------------------------------------: |
|      \w+-\d+      |  一个由字母数字组成的字符串和一串由一个连字符分隔的数字  |
|    [A-Za-z]\w*    | 第一个字符是字母；其余字符（如果存在）可以是字母或者数字 |
| \d{3}-\d{3}-\d{4} |  美国电话号码的格式，前面是区号前缀，例如 800-555-1212   |
|   \w+@\w+\.com    |        以 XXX@YYY.com 格式表示的简单电子邮件地址         |

###  1.8 使用圆括号指定分组

​	我们不仅想要知道整个字符串是否匹配我们的标准， 而且想要知道能否提取任何已经成功匹配的特定字符串或者子字符串。    

​	当使用正则表达式时，一对圆括号可以实现以下任意一个（或者两个）功能： 

- 对正则表达式进行分组； 
- 匹配子组。

		为什么匹配子组这么重要呢？主要原因是在很多时候除了进行匹配操作以外，我们还想 要提取所匹配的模式。例如，如果决定匹配模式\w+-\d+，但是想要分别保存第一部分的字母 和第二部分的数字，该如何实现？我们可能想要这样做的原因是， 对于任何成功的匹配，我 们可能想要看到这些匹配正则表达式模式的字符串究竟是什么。 如果为两个子模式都加上圆括号，例如(\w+)-(\d+)，然后就能够分别访问每一个匹配 子组。我们更倾向于使用子组，这是因为择一匹配通过编写代码来判断是否匹配，然后执行另一个单独的程序（该程序也需要另行创建）来解析整个匹配仅仅用于提取两个部分。

|          正则表达式模式          |                         匹配的字符串                         |
| :------------------------------: | :----------------------------------------------------------: |
|           \d+(\.\d*)?            | 表示简单浮点数的字符串；也就是说，任何十进制数字，后面可以接一个小数点和零个或 者多个十进制数字，例如“0.004”、“2”、“75.”等 |
| (Mr?s?\.)?\[A-Z][a-z]*[A-Za-z-]+ | 名字和姓氏，以及对名字的限制（如果有，首字母必须大写，后续字母小写），全名前可以 有可选的“Mr.”、“Mrs.”、“Ms.”或者“M.”作为称谓，以及灵活可选的姓氏，可以有多 个单词、 横线以及大写字母 |

###  1.9 拓展表示法

| 正则表达式模式  |                         匹配的字符串                         |
| :-------------: | :----------------------------------------------------------: |
|   (?:\w+\.)*    | 以句点作为结尾的字符串，例如“google.”、“twitter.”、“facebook.”，但是这些匹配不会保存下来 供后续的使用和数据检索 |
|   (?#comment)   |                 此处并不做匹配，只是作为注释                 |
|    (?=.com)     | 如果一个字符串后面跟着“.com”才做匹配操作，并不使用任何目标字符串 |
|    (?!.net)     |         如果一个字符串后面不是跟着“.net”才做匹配操作         |
|    (?<=800-)    | 如果字符串之前为“800-”才做匹配，假定为电话号码，同样，并不使用任何输入字符串 |
| (?<!192\.168\.) | 如果一个字符串之前不是“192.168.”才做匹配操作，假定用于过滤掉一组 C 类 IP 地址 |
|   (?(1)y\|x)    | 如果一个匹配组 1（\1）存在， 就与 y 匹配； 否则，就与 x 匹配 |



## 2 - 正则表达式和Python

### 2.1 re模块：核心函数和方法

| 函数/方法                                            | 描 述                                                        |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| **仅仅是 re 模块函数**                               |                                                              |
| compile(pattern， flags = 0)                         | 使用任何可选的标记来编译正则表达式的模式，然后返回一个正则表达式对象 |
| **re 模块函数和正则表达式对象的方法**                |                                                              |
| match(pattern， string， flags=0)                    | 尝试使用带有可选的标记的正则表达式的模式来匹配字符串。如果匹配成功，就返回 匹配对象； 如果失败，就返回 None |
| search(pattern， string， flags=0)                   | 使用可选标记搜索字符串中第一次出现的正则表达式模式。如果匹配成功，则返回匹 配对象； 如果失败，则返回 None |
| findall(pattern， string [, flags] )                 | 查找字符串中所有（非重复）出现的正则表达式模式，并返回一个匹配列表 |
| finditer(pattern， string [, flags] )                | 与 findall()函数相同，但返回的不是一个列表，而是一个迭代器。对于每一次匹配，迭代器都返回一个匹配对象 |
| split(pattern， string， max=0)                      | 根据正则表达式的模式分隔符， split 函数将字符串分割为列表，然后返回成功匹配的 列表，分隔最多操作 max 次（默认分割所有匹配成功的位置） |
| **re 模块函数和正则表达式对象方法**                  |                                                              |
| sub(pattern， repl， string， count=0)               | 使用 repl 替换所有正则表达式的模式在字符串中出现的位置，除非定义 count， 否则就 将替换所有出现的位置（另见 subn()函数，该函数返回替换操作的数目） |
| purge()                                              | 清除隐式编译的正则表达式模式                                 |
| **常用的匹配对象方法**                               |                                                              |
| group(num=0)                                         | 返回整个匹配对象，或者编号为 num 的特定子组                  |
| groups(default=None)                                 | 返回一个包含所有匹配子组的元组（如果没有成功匹配，则返回一个空元组） |
| groupdict(default=None)                              | 返回一个包含所有匹配的命名子组的字典，所有的子组名称作为字典的键（如果没有 成功匹配，则返回一个空字典） |
| **常用的模块属性（用于大多数正则表达式函数的标记）** |                                                              |
| re.I、 re.IGNORECASE                                 | 不区分大小写的匹配                                           |
| re.L、 re.LOCALE                                     | 根据所使用的本地语言环境通过\w、 \W、 \b、 \B、 \s、 \S 实现匹配 |
| re.M、 re.MULTILINE                                  | ^和$分别匹配目标字符串中行的起始和结尾，而不是严格匹配整个字符串本身的起始 和结尾 |
| re.S、 rer.DOTALL                                    | “.”（点号）通常匹配除了\n（换行符）之外的所有单个字符；该标记表示“.”（点号） 能够匹配全部字符 |
| re.X、 re.VERBOSE                                    | 通过反斜线转义， 否则所有空格加上#（以及在该行中所有后续文字）都被忽略，除非 在一个字符类中或者允许注释并且提高可读性 |

 **注：在模式匹配发生之前，正则表达式模式必须编译 成正则表达式对象。由于正则表达式在执行过程中将进行多次比较操作，因此强烈建议使 用预编译。而且，既然正则表达式的编译是必需的，那么使用预编译来提升执行性能无疑 是明智之举。 re.compile()能够提供此功能。 其实模块函数会对已编译的对象进行缓存，所以不是所有使用相同正则表达式模 式的 search()和 match()都需要编译。即使这样，你也节省了缓存查询时间，并且不必 对于相同的字符串反复进行函数调用。**    

### 2.2 匹配对象以及group()和groups()方法

​	当处理正则表达式时，除了正则表达式对象之外，还有另一个对象类型：匹配对象。这 些是成功调用 match()或者 search()返回的对象。匹配对象有两个主要的方法： group()和 groups()。 

​	group()要么返回整个匹配对象，要么根据要求返回特定子组。 groups()则仅返回一个包含 唯一或者全部子组的元组。如果没有子组的要求，那么当group()仍然返回整个匹配时，groups() 返回一个空元组。    

###  2.3 使用match()方法匹配字符串

​	match() 函数试图从字符串的起始部分对模式进行匹配。如果匹配成功，就返回一个匹配对象；如果 匹配失败，就返回 None，匹配对象的 group()方法能够用于显示那个成功的匹配。

```Python
import re

m = re.match('felix', 'felixoo')
print(m)
if m is not None:
    print(m.group())

m = re.match('felix', 'oofelix')
print(m)

print(re.match('felix', 'felix,nihao').group())
    
'''
<_sre.SRE_Match object; span=(0, 5), match='felix'>
felix
None
felix
'''
```

 span()指的是匹配成功后的位置，取前不取后。

### 2.4 使用search()在一个字符串中查找模式

​	search()的工作方式与 match()完全一致，不 同之处在于 search()会用它的字符串参数，在任意位置对给定正则表达式模式搜索第一次出现 的匹配情况。如果搜索到成功的匹配，就会返回一个匹配对象； 否则， 返回 None。

   

```Python
import re

# match()
m = re.match('felix', 'hello,felix')
# 匹配失败
print(m)

# search()
m = re.search('felix', 'hello,felix')
# 搜索成功
print(m)

'''
None
<_sre.SRE_Match object; span=(6, 11), match='felix'>
'''
```

###  2.5 匹配多个字符串

择一匹配（|）

```Python
import re

model = 'bat|bet|bit'
# 匹配成功
m = re.match(model, 'bat')
print(m)
print(m.group())
# 匹配失败
m = re.match(model, 'blt')
print(m)
# print(m.group())
# 匹配失败
m = re.match(model, 'He bit me')
print(m)
# print(m.group())
# 搜索成功
m = re.search(model, 'He bit me')
print(m)
print(m.group())

'''
<_sre.SRE_Match object; span=(0, 3), match='bat'>
bat
None
None
<_sre.SRE_Match object; span=(3, 6), match='bit'>
bit
'''
```

### 2.6 匹配任何单个字符

#### 2.6.1 ‘.’不能匹配换行符和空字符

```Python
import re

model = '.end'
m = re.match(model, 'bend')
print(m)
print(m.group())

# 不能匹配换行符或者非字符，即空字符
m = re.match(model, 'end')
print(m)
m = re.match(model, '\nend')
print(m)

# 搜索中匹配
m = re.search('.end', 'The end.')
print(m.group())

'''
<_sre.SRE_Match object; span=(0, 4), match='bend'>
bend
None
None
 end
'''
```

#### 2.6.2 匹配小数点，转义

```Python
import re

model1 = '3.14'  # 这里的点是匹配任意单个字符
model2 = '3\.14'  # 这里匹配小数点

m = re.match(model1, '3.14')
print(m.group())
m = re.match(model2, '3.14')
print(m.group())
m = re.match(model2, '3914')
# 这里因为model2匹配的小数点，所以匹配失败
print(m)
# 点号匹配0
m = re.match(model1, '3914')
print(m.group())
# 点号匹配‘.’
m = re.match(model1, '3.14')
print(m.group())

'''
3.14
3.14
None
3914
3.14
'''
```

###  2.7 创建字符集

\[cr]\[23]\[dp][o2]与 r2d2|c3po

```Python
import re

m = re.match('[cr][23][dp][o2]', 'c3po')
print(m.group())
m = re.match('[cr][23][dp][o2]', 'c2do')
print(m.group())
# 匹配失败
m = re.match('r2d2|c3po', 'c2do')
print(m)
# 匹配成功
m = re.match('r2d2|c3po', 'c3po')
print(m.group())

'''
c3po
c2do
None
c3po
'''
```

### 2.8 重复、特殊字符以及分组

​	简单电子邮件地址的 正则表达式（\w+@\w+\.com）。或许我们想要匹配比这个正则表达式所允许的更多邮件地址。 为了在域名前添加主机名称支持，例如 www.xxx.com，仅仅允许 xxx.com 作为整个域名，必须 修改现有的正则表达式。为了表示主机名是可选的，需要创建一个模式来匹配主机名（后面跟 着一个句点），使用“？ ”操作符来表示该模式出现零次或者一次，然后按照如下所示的方式， 插入可选的正则表达式到之前的正则表达式中： \w+@(\w+\.)?\w+\.com。

```Python
import re

model = '\w+@(\w+\.)?\w+\.com'
print(re.match(model, 'nobody@xxx.com').group())
print(re.match(model, 'nobody@www.xxx.com').group())

'''
nobody@xxx.com
nobody@www.xxx.com
'''
```

用以下模式来进一步扩展该示例，允许任意数量的中间子域名存在：

```Python
import re

model = '\w+@(\w+\.)*\w+\.com'
print(re.match(model, 'nobody@www.xxx.yyy.zzz.com').group())

'''
nobody@www.xxx.yyy.zzz.com
'''
```

上述正则表达式不能匹配诸如 xxx-yyy.com 的域名或者使用非单 词\W 字符组成的域名。 												

​	使用圆括号来匹配和保存子组，以便于后续处理，而不是确定一个正则表达式匹配之后，在一个单独的子程序里面手动编码来解析字符串。修改之前讨论过的正则表达式，使该正则表达式能够提取字母数字字符串和数 字。如下所示，请注意如何使用 group()方法访问每个独立的子组以及 groups()方法以获取一 个包含所有匹配子组的元组。

代码1：

```Python
import re

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
# 完成匹配
print(m.group())
# 子组1
print(m.group(1))
# 子组2
print(m.group(2))
# 全部子组
print(m.groups())

'''
abc-123
abc
123
('abc', '123')
'''
```

代码2：

```Python
import re

m = re.match('ab', 'ab')  # 没有子组
print(m.group())  # 完整匹配
print(m.groups())  # 所有字组

m = re.match('(ab)', 'ab')  # 一个子组
print(m.group())  # 完整匹配
print(m.group(1))  # 子组1
print(m.groups())  # 全部子组

m = re.match('(a)(b)', 'ab')  # 两个子组
print(m.group())  # 完整匹配
print(m.group(1))  # 子组1
print(m.group(2))  # 子组2
print(m.groups())  # 全部子组

m = re.match('(a(b))', 'ab')  # 两个子组
print(m.group())  # 完整匹配
# 最外面的括号里的字符算子组1
print(m.group(1))  # 子组1
print(m.group(2))  # 子组2
print(m.groups())  # 全部子组

'''
ab
()
ab
ab
('ab',)
ab
a
b
('a', 'b')
ab
ab
b
('ab', 'b')
'''
```

### 2.9 匹配字符串的起始和结尾以及单词边界

​	介绍显示位置的正则表达式操作符。该操作更多的表示搜索，而不是从开始位置匹配。

```Python
import re

m = re.search('^The', 'The end.')
print(m.group())

m = re.search('^The', 'end.The')
print(m)

m = re.search(r'\bthe', 'bite the dog')  # 在边界
print(m.group())

m = re.search(r'the\b', 'bite theo dog')  # 有边界
print(m)

m = re.search(r'\bthe', 'bite othe dog')  # 有边界
print(m)

m = re.search(r'\bthe', 'bite theo dog')  # 在边界
print(m.group())

m = re.search(r'the\b', 'bite othe dog')  # 在边界
print(m.group())

m = re.search(r'\bthe\b', 'bite the dog')  # 仅匹配the
print(m.group())

# 匹配任何包含但不以the作为起始的字符串
m = re.search(r'\Bthe', 'bitetheo dog')  # 在边界
print(m.group())

'''
The
None
the
None
None
the
the
the
the
'''
```

### 2.10 使用findall()和finditer()查找每一次出现的位置

- **findall()**	

  ​	findall()查询字符串中某个正则表达式模式全部的非重复出现情况。这与 search()在执行 字符串搜索时类似，但与 match()和 search()的不同之处在于， findall()总是返回一个列表。如 果 findall()没有找到匹配的部分，就返回一个空列表，但如果匹配成功，列表将包含所有成 功的匹配部分（从左向右按出现顺序排列）。    

  ```Python
  import re
  
  m = re.findall('car', 'car')
  print(m)
  
  m = re.findall('car', 'scary')
  print(m)
  
  m = re.findall('car', 'carry the barcard to the car')
  print(m)
  
  m = re.findall('car', 'hello')
  print(m)
  
  '''
  ['car']
  ['car']
  ['car', 'car', 'car']
  []
  '''
  ```

- **finditer()**

  finditer()在匹配对象中迭代。 

  ```Python
  import re
  
  s = 'This and that'
  
  m = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
  print(m)
  print(m.__next__())
  
  m = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
  print(m.__next__().group())
  m = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
  print(m.__next__().group(1))
  m = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
  print(m.__next__().group(2))
  
  m = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
  print(m.__next__().groups())
  
  print([g.groups() for g in re.finditer(r'(th\w+) and (th\w+)', s, re.I)])
  
  '''
  <callable_iterator object at 0x00000214A8E64860>
  <_sre.SRE_Match object; span=(0, 13), match='This and that'>
  This and that
  This
  that
  ('This', 'that')
  [('This', 'that')]
  '''
  ```

  单个字符串中执行单个分组的多重匹配：

  ```Python
  import re
  
  s = 'This and that'
  
  m = re.findall(r'(th\w+)', s, re.I)
  print(m)
  
  iter_temp = re.finditer(r'(th\w+)', s, re.I)
  print(iter_temp)
  g = iter_temp.__next__()
  print(g)
  print(g.groups())
  print(g.group(1))
  g = iter_temp.__next__()
  print(g)
  print(g.groups())
  print(g.group(1))
  
  print([g.group(1) for g in re.finditer(r'(th\w+)', s, re.I)])
  
  '''
  ['This', 'that']
  <callable_iterator object at 0x00000253CE7798D0>
  <_sre.SRE_Match object; span=(0, 4), match='This'>
  ('This',)
  This
  <_sre.SRE_Match object; span=(9, 13), match='that'>
  ('that',)
  that
  ['This', 'that']
  '''
  ```

### 2.11 使用sub()和subn()搜索与替换

​	有两个函数/方法用于实现搜索和替换功能： sub()和 subn()。两者几乎一样，都是将某字 符串中所有匹配正则表达式的部分进行某种形式的替换。用来替换的部分通常是一个字符串， 但它也可能是一个函数，该函数返回一个用来替换的字符串。 subn()和 sub()一样，但 subn() 还返回一个表示替换的总数，替换后的字符串和表示替换总数的数字一起作为一个拥有两个 元素的元组返回。    

```Python
import re

m = re.sub('X', 'Mr.Smith', 'attn:X\n\nDear X,\n')
print(m)

m = re.subn('X', 'Mr.Smith', 'attn:X\n\nDear X,\n')
print(m)

m = re.sub('[ae]', 'X', 'abcdef')
print(m)

m = re.subn('[ae]', 'X', 'abcdef')
print(m)

'''
attn:Mr.Smith

Dear Mr.Smith,

('attn:Mr.Smith\n\nDear Mr.Smith,\n', 2)
XbcdXf
('XbcdXf', 2)
'''
```

### 2.12 修饰符

| 修饰符 |                             描述                             |
| :----: | :----------------------------------------------------------: |
|  re.I  |                     使匹配对大小写不敏感                     |
|  re.L  |                       做本地化识别匹配                       |
|  re.M  |                      多行匹配，影响^和$                      |
|  re.S  |               使.匹配包括换行符在内的所有字符                |
|  re.U  |    根据Unicode字符集解析字符。这个标志影响\w、\W、\b和\B     |
|  re.X  | 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解 |



#### 2.12.1 re.I/IGNORECASE

```Python
import re

# 不区分大小写
m = re.findall(r'(?i)yes', 'yes? Yes. YES!')
print(m)
m = re.findall(r'(?i)yes.', 'yes? Yes. YES!')
print(m)
m = re.findall(r'(?i)th\w+', 'The quickest way is through this tunnel.')
print(m)

# 在目标字符串中实现跨行搜索
m = re.findall(r'(?im)(^th[\w ]+)', """
This line is the first,
another line,
that line, it is the best
""")
print(m)

'''
['yes', 'Yes', 'YES']
['yes?', 'Yes.', 'YES!']
['The', 'through', 'this']
['This line is the first', 'that line']
'''
```

#### 2.12.2 re.I/DOTALL

​	该标记表明点号（.） 能够用来表示\n 符号（反之其通常 用于表示除了\n 之外的全部字符）：

```Python
import re

m = re.findall(r'th.+', """
... The first line
... the second line
... the third line
... """)
print(m)

m = re.findall(r'(?s)th.+', """
... The first line
... the second line
... the third line
... """)
print(m)

'''
['the second line', 'the third line']
['the second line\n... the third line\n... ']
'''
```

#### 2.12.3 re.X/VERBOSE

​	re.X/VERBOSE 标记非常有趣；该标记允许用户通过抑制在正则表达式中使用空白符（除 了在字符类中或者在反斜线转义中）来创建更易读的正则表达式。此外，散列、注释和井号 也可以用于一个注释的起始，只要它们不在一个用反斜线转义的字符类中。

```Python
import re

m = re.search(r'''(?x)
\((\d{3})\) # 区号
[ ] 
(\d{3})
-
(\d{4})
''', '(800) 555-1212').groups()
('800', '555', '1212')
print(m)

'''
('800', '555', '1212')
'''
```

### 2.15 (?…)

​	(?:…)符号将更流行；通过使用该符号，可以对部分正则表达式进行分组，但是并不会保 存该分组用于后续的检索或者应用。当不想保存今后永远不会使用的多余匹配时，这个符号就非常有用。

```Python
import re

m = re.findall(r'http://(?:\w+\.)*(\w+\.com)',
               'http://google.com http://www.google.com http://code.google.com')
print(m)

m = re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})','(800) 555-1212').groupdict()
print(m)

'''
['google.com', 'google.com', 'google.com']
{'areacode': '800', 'prefix': '555'}
'''
```

   	可以同时一起使用 (?P\<name>) 和 (?P=name)符号。前者通过使用一个名称标 识符而不是使用从 1 开始增加到 N 的增量数字来保存匹配，如果使用数字来保存匹配结 果，我们就可以通过使用\1,\2 ...,\N \来检索。如下所示，可以使用一个类似风格的\g<name> 来检索它们：

```Python
import re

m = re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})','(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212')
print(m)

'''
(800) 555-xxxx
'''
```

 	使用后者，可以在一个相同的正则表达式中重用模式，而不必稍后再次在（相同） 正则表达式中指定相同的模式。 例如， 在本示例中，假定让读者验证一些电话号码的规 范化。如下所示为一个丑陋并且压缩的版本，后面跟着一个正确使用的 (?x)， 使代码变 得稍许易读。

```Python
import re

m = bool(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number)1(?P=areacode)(?P=prefix)(?P=number)',
'(800) 555-1212 800-555-1212 18005551212'))
print(m)

m = bool(re.match(r'''(?x)
# match (800) 555-1212, save areacode, prefix, no.
\((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})

[ ]  # space

# match 800-555-1212
(?P=areacode)-(?P=prefix)-(?P=number)
# space
[ ]# match 180055512121(?P=areacode)(?P=prefix)(?P=number)''', '(800) 555-1212 800-555-1212 18005551212'))
print(m)

'''
False
True

'''
```

​	可以使用 (?=...) 和 (?!…)符号在目标字符串中实现一个前视匹配，而不必实际上使 用这些字符串。下一个示例中，让我们忽略以“noreply”或者 “postmaster”开头的 e-mail 地址。   

```Python
import re

m = re.findall(r'\w+(?= van Rossum)',
'''
Guido van Rossum
Tim Peters
Alex Martelli
Just van Rossum
Raymond Hettinger''')
print(m)

m = re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
'''
sales@phptr.com
postmaster@phptr.com
eng@phptr.com
noreply@phptr.com
admin@phptr.com''')
print(m)

m = ['%s@aw.com' % e.group(1) for e in \
re.finditer(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
'''
sales@phptr.com
postmaster@phptr.com
eng@phptr.com
noreply@phptr.com
admin@phptr.com
''')]
print(m)

'''
['Guido', 'Just']
['sales']
['sales@aw.com']
'''
```

​	假定我们拥有另一个特殊字符，它仅 仅包含字母“x”和“y”，我们此时仅仅想要这样限定字符串：两字母的字符串必须由一 个字母跟着另一个字母。换句话说，你不能同时拥有两个相同的字母；要么由“x”跟着 “y”，要么相反。

```Python
import re
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx')))
'''
True
False
'''
```



## 3 - 贪婪与非贪婪

​	寻找三个由连字符分隔的整数，所以可以创建自己的正则表达式来说明这 一需求： \d+-\d+-\d+。该正则表达式的含义是，“任何数值的数字（至少一个）后面跟着一个 连字符，然后是多个数字、 另一个连字符，最后是一个数字集。”我们现在将使用 search()来 测试该正则表达式：    

```Python
import re

data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '\d+-\d+-\d+'
m = re.match(patt, data)
print(m)

'''
None
'''
```

​	需要被匹配的数 值位于字符串的末尾。可以使 用惰性匹配，即使用“.+”来表明一个任意字符集跟在我们真正感兴趣的部分之后。    

```Python
import re

data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '.+\d+-\d+-\d+'
m = re.search(patt, data).group()
print(m)

'''
Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8
'''
```

​	但是我们只想要末尾的数字字段，而并不是整个字符串，因 此不得不使用圆括号对想要的内容进行分组。    

```Python
import re

data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '.+(\d+-\d+-\d+)'
m = re.search(patt, data).group(1)
print(m)

'''
4-6-8
'''
```

​	我们将提取 1171590364-6-8，而不仅仅是 4-6-8。第一个整数的其余部分在哪 儿？问题在于正则表达式本质上实现贪婪匹配。这就意味着对于该通配符模式，将对正则表达 式从左至右按顺序求值，而且试图获取匹配该模式的尽可能多的字符。在之前的示例中，使用 “.+”获取从字符串起始位置开始的全部单个字符，包括所期望的第一个整数字段。 \d+仅仅需 要一个数字，因此将得到“4”，其中.+匹配了从字符串起始部分到所期望的第一个数字的全部 内容： “Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::117159036”。

​	其中的一个方案是使用“非贪婪”操作符“?”。可以在“*”、“+”或者“?”之后使 用该操作符。该操作符将要求正则表达式引擎匹配尽可能少的字符。    

```Python
import re

data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '.+?(\d+-\d+-\d+)'
m = re.search(patt, data).group(1)
print(m)

'''
1171590364-6-8
'''
```

