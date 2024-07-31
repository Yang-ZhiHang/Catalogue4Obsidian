# Catalogue for Obsidian

**语言** 

[English](README.md)  [Chinese](README_zh.md)

## 最新消息

🚀2024年07月31日: `v0.2.1` 做了一些改进。

🚀2024年06月09日: `v0.2.0` 修复了一些 bug，优化了代码。

🚀2024年05月10日: `v0.1.1` 添加了开源许可证。



## 效果展示

<img src="./assert/output.gif" style="border-radius: 10px;">



## 详细

**这个程序能干啥?**

快速生成指定文件夹的目录（仅用于 Obsidian 的 **关系图谱** 展示）



> 什么是 Obsidian?

一款好用的笔记软件。



## 项目结构

`main.py` : 开始程序文件。

`retrieve.py` : 递归扫描文件的功能模块。



## 使用说明

打开 `main.py` 文件，修改 `if __name__ == "__main__":` 下的一些变量参数，以下是参数说明：

- `folder_path` : 你要生成目录的那个文件夹的绝对路径
- `catalogue_path` : 生成目录的输出路径（空文件夹的绝对路径，如果没有会自动创建）
- `ignore_folders` : 屏蔽文件的文件名

控制台会输出 `folder_path` 的文件结构，并在 `catalogue_path` 生成目录文件（用于 Obsidian 软件自动创建关系图谱）