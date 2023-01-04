import glob
import os
import shutil

# 获取自定义需重命名的目录以及文件
input_dir = input("请输入需要重命名的文件夹路径：")
input_ext = input("请输入需要重命名的文件后缀：")
input_name = input("请输入文件类型：")

# 获取当前目录中，以input_ext为扩展名的文件
filenames = glob.glob(os.path.join(input_dir, "*." + input_ext))
format_str = input_name + "_%03d." + input_ext

# 遍历文件列表，重命名每个文件
for i, filename in enumerate(filenames):
  # 使用 format_str 格式化文件名
  new_name = format_str % (i + 1)
  # 重命名文件
  os.rename(filename, new_name)
  # 移动文件到input_dir文件夹中
  shutil.move(new_name, input_dir)
