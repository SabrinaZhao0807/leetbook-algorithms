import os
import re
from collections import defaultdict

# 设置题目根目录
ROOT_DIR = "by-topic"

# 初始化分类统计结构
stats = defaultdict(lambda: {"简单": 0, "中等": 0, "困难": 0})

# 递归遍历所有 .md 文件
for root, _, files in os.walk(ROOT_DIR):
    for filename in files:
        if filename.endswith(".md"):
            path = os.path.join(root, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

                # 匹配类型（支持多个类型用斜杠分隔，如 "数组 / 双指针"）
                type_match = re.search(r"类型：(.+)", content)
                if not type_match:
                    continue
                types = [t.strip() for t in type_match.group(1).split("/")]

                # 匹配难度
                diff_match = re.search(r"难度：([简单中等困难]+)", content)
                if not diff_match:
                    continue
                difficulty = diff_match.group(1)

                # 每种类型计入一次
                for t in types:
                    stats[t][difficulty] += 1

# 计算总数
total_easy = sum(v["简单"] for v in stats.values())
total_medium = sum(v["中等"] for v in stats.values())
total_hard = sum(v["困难"] for v in stats.values())
total_all = total_easy + total_medium + total_hard

# 输出 Markdown 表格
print("| 分类 | 简单 | 中等 | 困难 | 总计 |")
print("|------|------|------|------|------|")
for key in sorted(stats):
    easy = stats[key]["简单"]
    medium = stats[key]["中等"]
    hard = stats[key]["困难"]
    total = easy + medium + hard
    print(f"| {key} | {easy} | {medium} | {hard} | {total} |")
print(f"| **总计** | **{total_easy}** | **{total_medium}** | **{total_hard}** | **{total_all}** |")
