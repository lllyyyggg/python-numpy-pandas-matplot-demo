# import copy
#
# a = [1, 2, 3, [4, 5]]
#
# b = copy.deepcopy(a)
# print(a)
# print(b)



import re


pattern1 = 'cat'
s = "This runs a cat"
# print(pattern1 in s)
# print(re.search(pattern1, s))


ptn = r'r[au]n'
ptn = r'r[0-9]n'
ptn = r'r[a-z]n'
ptn = r'r[A-Z]n'
ptn = r'r[0-9a-z]n'
ptn = r'r\dn'   # 数字
ptn = r'r\Dn'   # 非数字
ptn = r'r\sn'   # 空格
ptn = r'r\Sn'   # 非空格
ptn = r'r\wn'   # 字母
ptn = r'r\Wn'   # 非字母
ptn = r'r\bn'   # 空字符串
ptn = r'r\Bn'   # 非空字符
ptn = r'r.n'    # 任意字符
ptn = r'^dog'   # 句头匹配
ptn = r'dog$'   # 句尾匹配
ptn = r'dog*'   # 0或多次
ptn = r'dog+'   # 1或多次
ptn = r'dog{2, 10}'   # 2到10次
ptn = r'(\d+)'   # group
# match = re.search(ptn, s)
# print(match.group()) 所有group
# print(match.group(1))
# print(match.group(2))

ptn = r'?P<id>(\d+)'   # group命名
ptn = r'r[au]n'
print(re.findall(ptn, s)) # 查找全部

# re.sub(ptn, "replacement", s) # 替换
# re.split(ptn, s) # 分裂
# re.compile(ptn) # 编译












print(re.search(ptn, s))