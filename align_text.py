# ==========================================
# 任务3（完美对齐版）：打印带有中文的IP地址规划表
# ==========================================

# 💡 提前送你一个后面才会学的“函数”工具（就像自己造了一个小机器）
# 这个工具的作用：无论你塞进去中文还是英文，它都能精准计算屏幕宽度，并补齐正确的空格！
def align_text(text, total_width):
    # 将输入转为字符串
    text = str(text)
    # len(text.encode('gbk')) 这一步是魔法！它能算出中文字符占2个位置，英文占1个位置
    real_display_width = len(text.encode('gbk'))
    # 计算需要补多少个英文空格
    space_to_add = total_width - real_display_width
    # 返回：原本的文字 + 缺失的空格数
    return text + " " * space_to_add

# 1. 定义设备变量（顺便把你截图里第三行写错的“核心交换机”改回“无线控制器”啦）
dev1_name, dev1_ip, dev1_role = "CoreSwitch", "10.1.1.1", "核心交换机"
dev2_name, dev2_ip, dev2_role = "Firewall", "10.1.1.2", "防火墙"
dev3_name, dev3_ip, dev3_role = "WLC", "10.1.1.3", "无线控制器"

print("====================IP地址规划表====================")

# 2. 我们不再依赖 Python 自带的 <15，而是全部交给我们刚刚写的 align_text 工具来处理！
# 每个格子强行设定真实显示宽度为 16
title_1 = align_text("IP地址规划表", 16)
title_2 = align_text("管理地址", 16)
title_3 = align_text("角色", 16)
print(f"| {title_1} | {title_2} | {title_3} |")

print("|------------------|------------------|------------------|")

# 第一行数据
col1 = align_text(dev1_name, 16)
col2 = align_text(dev1_ip, 16)
col3 = align_text(dev1_role, 16)
print(f"| {col1} | {col2} | {col3} |")

# 第二行数据
col1 = align_text(dev2_name, 16)
col2 = align_text(dev2_ip, 16)
col3 = align_text(dev3_role, 16)  # 注意：上一代防火墙角色在这里
print(f"| {col1} | {col2} | {col3} |")

# 第三行数据
col1 = align_text(dev3_name, 16)
col2 = align_text(dev3_ip, 16)
col3 = align_text(dev3_role, 16)
print(f"| {col1} | {col2} | {col3} |")

print("====================================================")