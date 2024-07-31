from retrieve import generate_catalogue

if __name__ == "__main__":
    folder_path = "D:\\Documents\\AAANotes"  # The path to convert into catalogue
    catalogue_path = "D:\\Documents\\AAANotes\\AAACatalogue"  # The output path
    ignore_folders = [".git", ".obsidian", "AAACatalogue", "images", "Information"]  # The files to ignore

    generate_catalogue(
        first_level_directory_path=folder_path,
        ignore_directories=ignore_folders,
        output_directory=catalogue_path
    )
