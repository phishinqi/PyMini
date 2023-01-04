import os

# 获取自定义需重命名的目录以及文件
target_dir = input("需要处理的文件夹路径：")
target_ext = input("需要重命名的文件的后缀：")
file_type = input("文件类型：")

# 获取当前目录中，以input_ext为扩展名的文件
walker = os.walk(target_dir)
format_str = file_type + "_%03d." + target_ext

for path,dir_list,file_list in walker:
  for i, filename in enumerate(file_list):
    if filename.endswith(target_ext):
      # 使用 format_str 格式化文件名
      new_name = format_str % (i + 1)
      # 重命名文件
      os.rename(filename, new_name)
      # 移动文件到input_dir文件夹中
      os.rename(new_name, os.path.join(target_dir, new_name))
