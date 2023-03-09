import os

# 定义文件夹路径
program_dir = os.getcwd()
game_root_dir = os.path.dirname(os.path.abspath(program_dir))
JEI_DIR = game_root_dir + "\.minecraft\\versions\ROR-1.19.3\mods\JEI"
REI_DIR = game_root_dir + "\.minecraft\\versions\ROR-1.19.3\mods\REI"


# 为JEI文件夹中没有“.disabled”后缀的文件添加“.disabled”后缀
for file_name in os.listdir(JEI_DIR):
    if not file_name.endswith(".disabled"):
        os.rename(os.path.join(JEI_DIR, file_name), os.path.join(JEI_DIR, file_name + ".disabled"))
        print("Added:", file_name)

# 为REI文件夹中有“.disabled”后缀的文件取消“.disabled”后缀
for file_name in os.listdir(REI_DIR):
    if file_name.endswith(".disabled"):
        os.rename(os.path.join(REI_DIR, file_name), os.path.join(REI_DIR, file_name[:-9]))
        print("Removed:", file_name)