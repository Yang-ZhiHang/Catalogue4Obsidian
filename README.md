# 项目说明

**项目名称**：Catalogue for Obsidian

**项目目的**：快速生成指定文件夹路径的目录，便于使用 `Obsidian` 查看关系图谱

**项目参数**：

`retrieve.py`：递归扫描文件的功能模块

`images` 字符串：指的是一个文件夹中用于存放图片的文件夹



## 使用说明

打开 `main.py` 文件，修改 `if __name__ == "__main__":` 下方的相应参数

`directory_path` ： 文件夹的路径（用于生成该文件夹的目录）

`catalogue_dir` ： 目录的输出路径（要确保路径存在）

`ignore_file` ： 需要忽略的文件的名称（包括文件夹和文件）

控制台会输出 `directory_path` 的目录结构，并在 `catalogue_dir` 路径下生成 `Obsidian` 笔记软件能够使用的目录，用于自动生成关系图谱。

