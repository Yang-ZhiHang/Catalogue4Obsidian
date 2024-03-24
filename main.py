from retrieve import generateCatalogue

if __name__ == "__main__":
    directory_path = "D:\\ABitResource\\AAANotes"  # 要生成目录的文件夹的路径
    catalogue_dir = "D:\\ABitResource\\AAANotes\\AAACatalogue"  # 目录的输出路径（要确保路径正确）
    ignore_files = [".git", ".obsidian", "AAACatalogue", "images"]  # 需要忽略的文件名（包括文件夹和文件）

    generateCatalogue(first_level_directory_path=directory_path, ignore_files=ignore_files, output_dir=catalogue_dir)
