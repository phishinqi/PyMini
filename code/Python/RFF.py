import os
from subprocess import run, PIPE
from tqdm import tqdm

# 获取path中的所有文件名
path = input("请输入需要转换的目录：")
filenames = os.listdir(path)

# 获取转换的文件后缀
file_ext_1 = input("请输入待转换的文件后缀：")
file_ext_2 = input("请输入需要转换的文件后缀：")
subfolder = 'converted to ' + file_ext_2
os.mkdir(os.path.join(path, subfolder))

# 判断输入的文件后缀是否存在点号
if not file_ext_1.startswith('.'):
    # 如果不是，就在它的前面添加一个点号
    file_ext_1 = '.' + file_ext_1
# 同上
if not file_ext_2.startswith('.'):
    # 如果不是，就在它的前面添加一个点号
    file_ext_2 = '.' + file_ext_2

# 对于每个文件，使用ffmpeg将其转换为另一格式
with tqdm(total=len(filenames)) as pbar:
    for filename in filenames:
        # 忽略文件夹和非file_ext_1格式文件
        if not os.path.isdir(filename) and filename.endswith(file_ext_1):
            input_path = os.path.join(path, filename)
            output_path = os.path.join(path, subfolder, filename.split('.')[0] + file_ext_2)
            run(['ffmpeg', '-i', input_path, output_path], stdout=PIPE, stderr=PIPE)
        pbar.update(1)