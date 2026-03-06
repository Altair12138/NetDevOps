# ==========================================
# Python基础 第三天作业代码实现
# ==========================================
# 
import re

print("--- 第1题：解析mac地址表 ---")
# 原始字符串
mac_table = '166    54a2.74f7.0326    DYNAMIC    Gi1/0/11'

# 正则表达式解释：
# (\d+)       : 第1组，匹配一个或多个数字 (VLAN ID)
# \s+         : 匹配一个或多个空格
# ([0-9a-f.]+) : 第2组，匹配MAC地址(包含数字、小写a-f和点)
# \s+         : 匹配空格
# (\w+)       : 第3组，匹配单词字符 (Type)
# \s+         : 匹配空格
# (\S+)       : 第4组，匹配非空字符 (Interface)
pattern = r'(\d+)\s+([0-9a-f.]+)\s+(\w+)\s+(\S+)'

# 执行匹配
match = re.search(pattern, mac_table)

if match:
    # 提取分组数据
    vlan = match.group(1)
    mac = match.group(2)
    type_ = match.group(3)
    interface = match.group(4)

    # 使用 format() 进行格式化打印
    # <7 表示左对齐，占用7个字符宽度，保证冒号对齐
    print("-" * 30)
    print("作业 1 结果：")
    print("{0:<7} : {1}".format('VLAN', vlan))
    print("{0:<7} : {1}".format('MAC', mac))
    print("{0:<7} : {1}".format('Type', type_))
    print("{0:<7} : {1}".format('Port', interface))

print("\n--- 第2题：解析接口状态 ---")

# 原始字符串
conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
# 正则表达式解释：
# ^(\w+)      : 第1组，匹配开头的单词 (Protocol, e.g., TCP)
# \s+server\s+ : 匹配空格和"server"关键字（不捕获）
# ([\d.]+)    : 第2组，匹配IP地址 (Server IP)
# :           : 匹配冒号
# (\d+)       : 第3组，匹配数字 (Server Port)
# \s+localserver\s+ : 匹配空格和"localserver"关键字
# ([\d.]+)    : 第4组，匹配IP地址 (Client IP)
# :           : 匹配冒号
# (\d+)       : 第5组，匹配数字 (Client Port)
pattern = r'^(\w+)\s+server\s+([\d.]+):(\d+)\s+localserver\s+([\d.]+):(\d+)'

# 执行匹配
match = re.search(pattern, conn)

if match:
    # 提取分组数据
    protocol = match.group(1)
    server_ip = match.group(2)
    server_port = match.group(3)
    client_ip = match.group(4)
    client_port = match.group(5)

    # 使用 format() 进行格式化打印
    # <13 表示左对齐，占用13个字符宽度（基于最长的"Client Port"长度调整）
    print("-" * 30)
    print("作业 2 结果：")
    print("{0:<13} : {1}".format('Protocol', protocol))
    print("{0:<13} : {1}".format('Server IP', server_ip))
    print("{0:<13} : {1}".format('Server Port', server_port))
    print("{0:<13} : {1}".format('Client IP', client_ip))
    print("{0:<13} : {1}".format('Client Port', client_port))
