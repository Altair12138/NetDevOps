# ==========================================
# Python基础 第二天作业代码实现
# ==========================================
# 

print("--- 第1题：字符串拼接 ---")
date = "2026-03-03"
hostname = "SW-Core-01"
level = "CRITICAL"
message = "%LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down"

# 方法1：使用加号 (+) 进行传统字符串拼接，记得中间补上空格
syslog_contact = date+" "+hostname+" "+level+" "+message
print(syslog_contact)
# 方法2: 使用f-string格式化，代码更简洁（推荐）
syslog_fstring=f"{date} {hostname} {level} {message}"
# print(syslog_fstring)


print("\n--- 第2题：切片 ---")
interface = "GigabitEthernet0/0/1"

# "GigabitEthernet" 一共包含15个字符，索引从 0 到 14。
# 切片语法 [start:end]，包含 start，但不包含 end。
if_type=interface[:15]
if_num=interface[15:]
print(f"接口类型：{if_type}")
print(f"接口编号：{if_num}")


print("\n--- 第3题：字符串方法 ---")
version_raw = " Cisco IOS XE Software, Version 17.03.04 "
version_stripped=version_raw.strip()
version_upper=version_stripped.upper()
version_replaced=version_upper.replace("17.03.04", "17.06.01")
print(version_stripped)
print(version_upper)
print(version_replaced)


print("\n--- 第4题：format格式化 ---")
# 假设定义了以下接口状态变量：
if_name = "GigabitEthernet0/1"
admin_status = "UP"
oper_status = "UP"
ip_address = "192.168.1.254"

# 使用 format() 方法填入花括号 {} 中
report_tem="接口：{0:<5} | 管理状态：{1} | 运行状态{2} | IP地址：{3}"
final_report=report_tem.format(if_name, admin_status, oper_status, ip_address)
print(">> 接口状态巡检报告 <<")
print(final_report)

# 或者更优雅的命名参数方式，如下<20代表左对齐并预留20个字符位置
# report_template = "接口 {name:<20} | 状态: {status:<4} | IP: {ip}"
# print(report_template.format(name=if_name, status=oper_status, ip=ip_address))

