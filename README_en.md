# Catalogue for Obsidian

**Language** 

[English](README.md)  [Chinese](README_zh.md)

## News

🚀Jul. 31, 2024: `v0.2.1` added some optimizations.

🚀Jun. 09, 2024: `v0.2.0` fixed some bugs and optimized code.

🔧May. 10, 2024: `v0.1.1` added LICENSE.



## Effect Gif

<img src="./assert/output.gif" style="border-radius: 10px;">



## Description

**What can it do?**

Quickly generate the catalogue of a specified folder (only for the display of relationship graph in `Obsidian`)



> What's Obsidian?

A note-taking software.



## The Structure of The Project

`main.py` : Where to Get Start.

`retrieve.py` : Recursive scan file function module.



## Let's Get Start!

Open `main.py` ，modify the parameters below `if __name__ == "__main__":` 

- `folder_path` : The absolute path of folder to be used for generate catalogue.

- `catalogue_path` : The absolute path to output the catalogue. (The path should be a empty folder, or it will create automatically)

- `ignore_folders` : The files not to be scanned recursively.

The console will output the directory structure of `folder_path` and generate a catalogue in the `catalogue_path` path that is compatible with the Obsidian note-taking software for automatically creating a relationship graph.

