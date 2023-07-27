# 批量将文件夹中【子文件】的【txt文件】中每一个数字乘上101.8789144050104，如：6.974240303039551 转换成710.0,保留小数点后一位

import os

# 定义文件夹路径
folder_path = "文件夹路径"

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 遍历每个文件
for file in files:
    # 检查文件是否为txt文件
    if file.endswith(".txt"):
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, file)
        
        # 打开文件并读取内容
        with open(file_path, "r") as f:
            content = f.read()
        
        # 将内容中的数字乘以101.8789144050104
        new_content = ""
        for char in content:
            if char.isdigit() or char == ".":
                new_content += char
            else:
                if new_content != "":
                    new_content = str(round(float(new_content) * 101.8789144050104, 1))
                new_content += char
        
        # 将新的内容写回文件
        with open(file_path, "w") as f:
            f.write(new_content)

