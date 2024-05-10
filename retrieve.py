import os


def _show_file_in_dir(
        directory_path: str,
        output_dir: str,
        n: int = 2
) -> None:
    """
    根据给定的文件夹路径输出文件夹中的文件（不包括文件夹）
    如果给定的文件夹目录下有文件夹，则对每个文件夹调用 show_file_in_dir 方法
    :param directory_path: 给定的文件夹路径
    :param output_dir: 输出目录的路径，需要手动创建好
    :param n: 递归查询次数
    :return:
    """
    if n == 2:
        if not os.path.exists("{}\\Second-Level-Catalogue".format(output_dir)):
            os.mkdir("{}\\Second-Level-Catalogue".format(output_dir))
        output_file_path = "{}\\Second-Level-Catalogue\\{}.md".format(output_dir,
                                                                      directory_path.split("\\")[-1])
    elif n == 3:
        if not os.path.exists("{}\\Second-Level-Catalogue\\Third-Level-Catalogue".format(output_dir)):
            os.mkdir("{}\\Second-Level-Catalogue\\Third-Level-Catalogue".format(output_dir))
        output_file_path = ("{}\\Second-Level-Catalogue\\Third-Level"
                            "-Catalogue\\{}.md").format(output_dir, directory_path.split("\\")[-1])
    elif n == 4:
        if not os.path.exists("{}\\Second-Level-Catalogue\\Third-Level-Catalogue"
                              "\\Forth-Level-Catalogue".format(output_dir)):
            os.mkdir("{}\\Second-Level-Catalogue\\Third-Level-Catalogue\\Forth"
                     "-Level-Catalogue".format(output_dir))
        output_file_path = ("{}\\Second-Level-Catalogue\\Third-Level"
                            "-Catalogue\\Forth-Level-Catalogue\\{}.md").format(output_dir,
                                                                               directory_path.split("\\")[-1])
    else:
        output_file_path = None

    if directory_path.split("\\")[-1] == "images":
        pass
    else:
        try:
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                # 遍历根目录下的所有文件夹和文件，输出文件
                for file in os.listdir(directory_path):
                    file_path = os.path.join(directory_path, file)

                    if file == "images":
                        pass
                    else:
                        output_file.write("[[{}]]\n".format(file))

                    if os.path.isfile(file_path):
                        print("\t" * n + "|- " + file)

                    # 如果遇到文件夹继续输出其中的文件
                    elif os.path.isdir(file_path):
                        print("\t" * n + "|- " + file + "(" + directory_path.split("\\")[-1] + ")")
                        a = n + 1
                        _show_file_in_dir(file_path, output_dir, a)
        except Exception as e:
            print(f"An error occurred: {e}")


def _show_all_in_dir(
        first_level_directory_path: str,
        ignore_files: list,
        output_dir: str
) -> None:
    """
    在一级文件夹中寻找二级文件夹，并对每个二级文件夹调用 show_file_in_dir 方法
    :param first_level_directory_path: 一级文件夹路径
    :param ignore_files: 需要忽略的文件列表
    :param output_dir: 输出目录的路径，需要手动创建好
    :return:
    """
    with open("{}\\Catalogue.md".format(output_dir), "w", encoding="utf-8") as f:
        pass
    f.close()
    output_file_path = "{}\\Catalogue.md".format(output_dir)

    try:
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            for file in os.listdir(first_level_directory_path):
                # 判断是否需要忽略
                if file in ignore_files:
                    continue

                file_path = os.path.join(first_level_directory_path, file)  # 文件路径，此时还不能判断是文件夹还是文件

                # 判断是否为文件夹
                if os.path.isdir(file_path):
                    second_level_directory_path = file_path

                    # 输出文件夹名称，追加父级目录到括号中
                    print("\t|- " + second_level_directory_path.split("\\")[-1] + "(" +
                          first_level_directory_path.split("\\")[
                              -1] + ")")

                    if second_level_directory_path.split("\\")[-1] == "images":
                        pass
                    else:
                        output_file.write("[[{}]]\n".format(second_level_directory_path.split("\\")[-1]))

                    # 输出该文件夹下的文件
                    _show_file_in_dir(second_level_directory_path, output_dir)
                elif os.path.isfile(file_path):
                    second_level_directory_path = file_path

                    # 输出文件夹名称，追加父级目录到括号中
                    print("\t|- " + second_level_directory_path.split("\\")[-1] + "(" +
                          first_level_directory_path.split("\\")[
                              -1] + ")")
                    if second_level_directory_path.split("\\")[-1] == "images":
                        pass
                    else:
                        output_file.write("[[{}]]\n".format(second_level_directory_path.split("\\")[-1]))

    except Exception as e:
        print(f"An error occurred: {e}")


def generate_catalogue(
        first_level_directory_path: str,
        ignore_files: list,
        output_dir: str
) -> None:
    """
    :param first_level_directory_path: 一级文件夹路径
    :param ignore_files: 需要忽略的文件列表
    :param output_dir: 输出目录的路径，需要手动创建好
    :return:
    """
    print(first_level_directory_path.split("\\")[-1])
    _show_all_in_dir(first_level_directory_path, ignore_files, output_dir)
