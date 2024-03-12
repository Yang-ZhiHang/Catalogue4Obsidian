import os


def write_to_catalogue(directory):
    directory_path = 'D:\\ABitResource\\AAANotes\\' + directory
    output_file_path = 'D:\\ABitResource\\AAANotes\\AAACatalogue\\Second-Level-Catalogue\\' + directory + '.md'
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # 只遍历根目录下的所有文件夹和文件
            for file in os.listdir(directory_path):
                if os.path.isfile(os.path.join(directory_path, file)):
                    output_file.write('[[' + file + ']]\n')
                # elif os.path.isdir(os.path.join(directory_path, file)):
                #     output_file.write()
        print(f"File names have been successfully written to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def show_file_in_dir(directory_path, n=2):
    """
    根据给定的文件夹路径输出文件夹中的文件（不包括文件夹）
    如果给定的文件夹目录下有文件夹，则对每个文件夹调用 show_file_in_dir 方法
    :param n:
    :param directory_path: 给定的文件夹路径
    :return:
    """
    # 遍历根目录下的所有文件夹和文件，输出文件
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            print('\t' * n + '|- ' + file)

        # 如果遇到文件夹继续输出其中的文件
        elif os.path.isdir(file_path):
            print('\t' * n + '|- ' + file + '(' + directory_path.split('\\')[-1] + ')')
            a = n + 1
            show_file_in_dir(file_path, a)


def show_all_in_dir(first_level_directory_path, ignore_file: list):
    """
    在一级文件夹中寻找二级文件夹，并对每个二级文件夹调用 show_file_in_dir 方法
    :param ignore_file: 需要忽略的文件列表
    :param first_level_directory_path: 一级文件夹路径
    :return:
    """
    for file in os.listdir(first_level_directory_path):
        # 判断是否需要忽略
        if file in ignore_file:
            continue

        file_path = os.path.join(first_level_directory_path, file)  # 文件路径，此时还不能判断是文件夹还是文件

        # 判断是否为文件夹
        if os.path.isdir(file_path):
            second_level_directory_path = file_path

            # 输出文件夹名称，追加父级目录到括号中
            print('\t|- ' + second_level_directory_path.split('\\')[-1] + '(' + first_level_directory_path.split('\\')[
                -1] + ')')

            # 输出该文件夹下的文件
            show_file_in_dir(second_level_directory_path)


if __name__ == '__main__':
    directory_path = 'D:\\ABitResource\\AAANotes'  # 要查看目录的文件夹路径
    ignore_file = ['.git', '.obsidian', 'AAACatalogue']  # 需要忽略的文件名（包括文件夹和文件）

    print(directory_path.split('\\')[-1])

    show_all_in_dir(directory_path, ignore_file)

    # write_to_catalogue('NLP')
