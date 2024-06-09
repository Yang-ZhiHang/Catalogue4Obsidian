# Catalogue for Obsidian

## News

🚀Jun. 09, 2024: v0.2.0 released, fixed some bugs and optimized code.

🚀May. 10, 2024: v0.1.1 released, added LICENSE.



## Description

**What can it do?**

Quickly generate the directory of the specified folder (only for `Obsidian` view of the relationship graph)



> What's Obsidian?

A note-taking software.



## The Structure of The Project

`main.py` : Where to Get Start.

`retrieve.py` : Recursive scan file function module.



## Get Started

Open `main.py` ，modify the parameters below `if __name__ == "__main__":` 

- `directory_path` : The absolute path of directory to be used for generate catalogue.

- `catalogue_directory` : The absolute path to output catalogue.

- `ignore_directories` : The files not to be scanned recursively.

The console will output the directory structure of `directory_path` and generate a catalogue in the `catalogue_directory` path that is compatible with the Obsidian note-taking software for automatically creating a relationship graph.

