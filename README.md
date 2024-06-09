# Catalogue for Obsidian

## News

🚀Jun. 09, 2024: v0.2.0 released, fixed some bugs and optimized code.

🚀May. 10, 2024: v0.1.1 released, added LICENSE.



## Description

**What can it do?**

Quickly generate the directory of the specified folder (only for `Obsidian` view of the relationship graph)

快速生成指定文件夹的目录（仅用于 `Obsidian` 查看关系图谱）



> What's Obsidian?

A note-taking software.

一个笔记软件。



**The Structure of The Project**

`main.py` : Where to Get Start.

`retrieve.py` : Recursive scan file function module.



## Get Started

打开 `main.py` 文件，修改 `if __name__ == "__main__":` 下方的相应参数

- `directory_path` : The absolute path of directory to be used for generate catalogue.

- `catalogue_directory` : The absolute path to output catalogue.

- `ignore_directories` : The files not to be scanned recursively.

The console will output the directory structure of `directory_path` and generate a catalogue in the `catalogue_directory` path that is compatible with the Obsidian note-taking software for automatically creating a relationship graph.

控制台将输出 `directory_path` 的目录结构，并在 `catalogue_directory` 路径下生成 `Obsidian` 笔记软件能够使用的目录，用于自动生成关系图谱。

