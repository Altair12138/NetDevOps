# ==========================================
# Python基础 第一天作业代码实现
# ==========================================
# 
import random

print("--- 第一题：打印一台网络设备的基本信息 ---")
# 1. 定义变量
hostname = "C8Kv1"
ip = "192.168.1.1"
vendor = "Cisco"
model = "C8000v"
os_version = "IOS-XE 17.3.4"

# 2. 使用字符串拼接（+）打印卡片，该方法打印出来每一行的内容都是平铺
print("==========设备信息==========")
print("设备名称：{0}".format(hostname))
print("管理地址：{0}".format(ip))
print("厂　　商：{0}".format(vendor))  
print("型　　号：{0}".format(model))  
print("系统版本：{0}".format(os_version))
print("===========================\n")


print("--- 任务2：生成随机IP地址 ---")

# 1. 使用 random.randint() 随机生成 4 个 0-255 的整数
octet1 = random.randint(0, 255)
octet2 = random.randint(0, 255)
octet3 = random.randint(0, 255)
octet4 = random.randint(0, 255)

random_ip=str(octet1)+"."+str(octet2)+"."+str(octet3)+"."+str(octet4)
print("随机生成的IP是："+random_ip)
print(f"随机生成的IP是：{octet1}.{octet2}.{octet3}.{octet4}")


print("--- 任务3：打印IP地址规划表 ---")

# 1. 定义设备变量
dev1_name, dev1_ip, dev1_role = "CoreSwitch", "10.1.1.1", "核心交换机"
dev2_name, dev2_ip, dev2_role = "Firewall", "10.1.1.2", "防火墙"
dev3_name, dev3_ip, dev3_role = "WLC", "10.1.1.3", "无线控制器"

# 2. 使用刚才学的排版知识 < 强制左对齐并固定宽度！
# 定义一个统一的模板，保证竖线能对齐
row_template = "| {0:<12} | {1:<12} | {2:<10} |"

print("====================IP地址规划表====================")
print(row_template.format("IP地址规划表", "管理地址", "角色"))
print("|--------------|--------------|------------|")
print(row_template.format(dev1_name,dev1_ip,dev1_role))
print(row_template.format(dev2_name,dev2_ip,dev2_role))
print(row_template.format(dev3_name,dev3_ip,dev1_role))

print("=====================================================")