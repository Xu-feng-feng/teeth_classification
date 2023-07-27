import os
import shutil

# 创建文件夹
for i in range(1, 17):
    folder_name = str(i)
    os.makedirs(folder_name, exist_ok=True)

# 移动文件到相应的文件夹
for file_name in os.listdir('.'):
    if file_name.endswith('.txt') and any(str(num) in file_name for num in range(1, 17)):
        prefix = ''.join(filter(str.isdigit, file_name))
        folder_name = str(int(prefix))
        shutil.move(file_name, folder_name)

# import os
# import shutil

# # 原始文件夹路径
# source_folder = 'C:\\dataset\\imu_demo\\train_v1\\data\\2023_7_18'

# # 目标文件夹路径
# target_folder = 'C:\\dataset\\imu_demo\\train_v1\\data\\2023_7_20'

# # 遍历原始文件夹中的子文件夹
# for root, dirs, files in os.walk(source_folder):
#     for file in files:
#         if file.endswith('.txt') and file.startswith('extracted_new_output_'):
#             # 构建新的文件路径
#             new_file_path = os.path.join(target_folder, root, file)
#             # print(new_file_path)
            
#             # 检查源文件和目标文件是否相同
#             if not os.path.samefile(os.path.join(root, file), new_file_path):
#                 # 复制文件到目标文件夹中的相同目录结构
#                 shutil.copy2(os.path.join(root, file), new_file_path)




# # 原始文件夹路径
# source_folder = 'C:\\dataset\\imu_demo\\train_v1\\data\\2023_7_18'

# # 目标文件夹路径
# target_folder = 'C:\\dataset\\imu_demo\\train_v1\\data\\2023_7_20'

