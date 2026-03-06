# ==========================================
# Python基础 第四天作业代码实现
# ==========================================
# 

import os
import re
# ==========================================
# 准备工作：执行 Linux 命令获取网卡信息
# ==========================================
# 尝试执行 ifconfig 命令获取 ens33 的信息
result = os.popen("ifconfig ens33").read()

# ==========================================
# 第一步：用正则表达式提取 IP、掩码、广播地址、MAC
# ==========================================
# 使用正则表达式进行匹配抓取
ip_match = re.search(r'inet\s+(\d+\.\d+\.\d+\.\d+)', result)
mask_match = re.search(r'netmask\s+(\d+\.\d+\.\d+\.\d+)', result)
broadcast_match = re.search(r'broadcast\s+(\d+\.\d+\.\d+\.\d+)', result)
mac_match = re.search(r'ether\s+([0-9a-fA-F:]+)', result)

ip = ip_match.group(1) if ip_match else None
mask = mask_match.group(1) if mask_match else None
broadcast = broadcast_match.group(1) if broadcast_match else None
mac = mac_match.group(1) if mac_match else None

# 使用 format() 函数进行排版对齐（左对齐占用11个字符宽度）
print("="*40)
print("{:<11}: {}".format("IP", ip))
print("{:<11}: {}".format("Netmask", mask))
print("{:<11}: {}".format("Broadcast", broadcast))
print("{:<11}: {}".format("MAC", mac))
print("="*40)

# ==========================================
# 第二步：获取网关并 Ping 测试
# ==========================================
if ip != "None":
     # 以点为分隔符切割 IP 地址
    ip_parts = ip.split('.')
    # 拼接前三段，并将最后一段固定为 1，得到网关地址
    gateway = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.1"
    print("假设网关为: {}".format(gateway))
    print(f"正在进行 Ping 测试，请稍候...")

    # 用 os.popen 执行 ping 测试
    # 参数说明：-c 1 发送 1 个数据包，-W 1 设置超时时间为 1 秒 (Linux标准参数)
    ping_cmd = f"ping -c 1 -W 1 {gateway}"
    ping_result = os.popen(ping_cmd).read()

    # 根据 ping 命令的输出中是否含有 "ttl="（返回包的时间生存期）来判断是否可达
    if "ttl=" in ping_result:
        print("网关 {} 可达！".format(gateway))
    else:
        print("网关 {} 不可达！".format(gateway))
else:
    print("未获取到有效的 IP 地址，无法进行 Ping 测试。")   