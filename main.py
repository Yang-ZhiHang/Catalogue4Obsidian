from retrieve import generate_catalogue

if __name__ == "__main__":
    directory_path = "D:\\Documents\\AAANotes"  # The path to convert into catalogue
    catalogue_dir = "D:\\Documents\\AAANotes\\AAACatalogue"  # The output path
    ignore_directories = [".git", ".obsidian", "AAACatalogue", "images"]  # The files to ignore

    generate_catalogue(
        first_level_directory_path=directory_path,
        ignore_directories=ignore_directories,
        output_dir=catalogue_dir
    )
