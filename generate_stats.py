import os
import re
from collections import defaultdict

# 文件路径
PROBLEM_DIR = "by-topic"

# 初始化统计结构
stats = defaultdict(lambda: {"简单": 0, "中等": 0, "困难": 0})

# 遍历所有 Markdown 文件
for filename in os.listdir(BY-TOPIC_DIR):
    if not filename.endswith(".md"):
        continue
    with open(os.path.join(BY-TOPIC_DIR, filename), "r", encoding="utf-8") as f:
        content = f.read()

        # 匹配题目类型
        type_match = re.search(r"类型：(.+)", content)
        if not type_match:
            continue
        types = [t.strip() for t in type_match.group(1).split("/")]

        # 匹配题目难度
        difficulty_match = re.search(r"难度：([简单中等困难]+)", content)
        if not difficulty_match:
            continue
        difficulty = difficulty_match.group(1)

        # 为每个类型 +1
        for t in types:
            stats[t][difficulty] += 1

# 统计总计
total_easy = sum(v["简单"] for v in stats.values())
total_medium = sum(v["中等"] for v in stats.values())
total_hard = sum(v["困难"] for v in stats.values())
total_all = total_easy + total_medium + total_hard

# 输出 Markdown 表格
print("| 分类 | 简单 | 中等 | 困难 | 总计 |")
print("|------|------|------|------|------|")
for key, val in sorted(stats.items()):
    total = val["简单"] + val["中等"] + val["困难"]
    print(f"| {key} | {val['简单']} | {val['中等']} | {val['困难']} | {total} |")
print(f"| **总计** | **{total_easy}** | **{total_medium}** | **{total_hard}** | **{total_all}** |")
