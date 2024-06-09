import os


def _show_files_in_directory(
        directory_path: str,
        ignore_directories: list,
        output_directory: str,
        n: int = 2
) -> None:
    """
    Output all files in a directory based on the given directory path.
    if there are subdirectory in the given directory, call self for each subdirectory.
    :param directory_path: the given directory path
    :param output_directory: the output directory path
    :param n: the time of recursive retrieve
    :return:
    """
    if n == 2:
        if not os.path.exists("{}\\Second-Level-Catalogue".format(output_directory)):
            os.mkdir("{}\\Second-Level-Catalogue".format(output_directory))
        output_file_path = "{}\\Second-Level-Catalogue\\{}.md".format(
            output_directory, directory_path.split("\\")[-1]
        )
    elif n == 3:
        if not os.path.exists("{}\\Second-Level-Catalogue\\Third-Level-Catalogue".format(output_directory)):
            os.mkdir("{}\\Second-Level-Catalogue\\Third-Level-Catalogue".format(output_directory))
        output_file_path = "{}\\Second-Level-Catalogue\\Third-Level-Catalogue\\{}.md".format(
            output_directory, directory_path.split("\\")[-1]
        )
    elif n == 4:
        if not os.path.exists("{}\\Second-Level-Catalogue\\Third-Level-Catalogue"
                              "\\Forth-Level-Catalogue".format(output_directory)):
            os.mkdir("{}\\Second-Level-Catalogue\\Third-Level-Catalogue\\Forth-Level-Catalogue".format(output_directory))
        output_file_path = "{}\\Second-Level-Catalogue\\Third-Level-Catalogue\\Forth-Level-Catalogue\\{}.md".format(
            output_directory, directory_path.split("\\")[-1]
        )
    else:
        output_file_path = None

    if directory_path.split("\\")[-1] in ignore_directories:
        pass
    else:
        try:
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                # Iterate through all files and directories in root directory path, and output files
                for file in os.listdir(directory_path):
                    file_path = os.path.join(directory_path, file)

                    if file in ignore_directories:
                        pass
                    else:
                        output_file.write("[[{}]]\n".format(file))

                    if os.path.isfile(file_path):
                        print("\t" * n + "|- " + file)

                    # Continues seeking files in directory
                    elif os.path.isdir(file_path):
                        print("\t" * n + "|- {}({})".format(file, directory_path.split("\\")[-1]))
                        a = n + 1
                        _show_files_in_directory(file_path, ignore_directories, output_directory, a)

        except Exception as e:
            print(f"An error occurred: {e}")


def _show_all_in_dir(
        first_level_directory_path: str,
        ignore_directories: list,
        output_directory: str
) -> None:
    """
    find the second level files in the first level directory and call _show_file_in_dir() to show all the files in
    the second directory
    :param first_level_directory_path: first level directory path
    :param ignore_directories: the files to ignore
    :param output_directory: the output directory path
    :return:
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    with open("{}\\Catalogue.md".format(output_directory), "w", encoding="utf-8") as f:
        f.close()
    output_file_path = "{}\\Catalogue.md".format(output_directory)

    try:
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            for file in os.listdir(first_level_directory_path):
                # whether to be ignored
                if file in ignore_directories:
                    continue

                file_path = os.path.join(first_level_directory_path, file)
                # The file path, you don't know whether it is directory or file

                second_level_directory_path = file_path

                # Output the filename, and put the father directory into bracket
                print("\t|- {}({})".format(
                    second_level_directory_path.split("\\")[-1], first_level_directory_path.split("\\")[-1]
                ))

                if second_level_directory_path.split("\\")[-1] in ignore_directories:
                    pass
                else:
                    output_file.write("[[{}]]\n".format(second_level_directory_path.split("\\")[-1]))

                if os.path.isdir(file_path):
                    # output files in directory
                    _show_files_in_directory(second_level_directory_path, ignore_directories, output_directory)

    except Exception as e:
        print(f"An error occurred: {e}")


def generate_catalogue(
        first_level_directory_path: str,
        ignore_directories: list,
        output_directory: str
) -> None:
    """
    :param first_level_directory_path: first level directory path
    :param ignore_directories: the files to ignore
    :param output_directory: the output directory
    :return:
    """
    print(first_level_directory_path.split("\\")[-1])
    _show_all_in_dir(first_level_directory_path, ignore_directories, output_directory)
