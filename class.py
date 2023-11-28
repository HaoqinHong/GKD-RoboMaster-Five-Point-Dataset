import os
import re

# 设置要遍历的文件夹路径
folder_path = "E:/ProgrammingProjects/PythonProjects/DeepLearning/SWU-GKD-RMUC/_test/labels"

class_label = []


# 遍历文件夹
for filename in os.listdir(folder_path):
    # 判断文件是否是txt文件
    if filename.endswith(".txt"):
        # 打开文件
        with open(os.path.join(folder_path, filename), "r") as f:
            # 遍历文件的每一行
            for line in f:
                # 从每一行中提取第一个数字
                match = re.search(r"\d+", line)
                if match:
                    first_number = int(match.group())
                    # 这里可以对第一个数字进行处理，例如打印出来
                    if first_number not in class_label:
                        class_label.append(first_number)
print(class_label)
print(len(class_label))