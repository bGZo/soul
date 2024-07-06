
# class Regex(object):
#   reg       = ""
#   reg_rule  = ""
#   def __init__(self, reg, reg_rule):
#     self.reg = reg
#     self.reg_rule = reg_rule

# 需要在代码中生命对象，有些多此一举；

# 把正则表达式写在配置文件中
#   - 当选用 YAML 的时候，转义符号在扫描阶段会出现问题，不仅书写有讲究，而且扫描进去会变成两个//

import re

str1 = "- [没关系Bot：“没关系，能主动和hr打招呼已经很厉害了” - 小球飞象](https://toot.mantyke.icu/@dontworry/110868627566767500)"

link = re.sub(r"\[(.*?)\]\((.*?)\)", r"\2", str1)

print(link)


