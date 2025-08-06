# PY-CPP tools

These are my python scripts which helps me automating grueling tasks my clients gave me. For example: `Converting .hpp to .h files`.

## Table of contents

* `flatten.py` - Convert a recursive src directory to a flat directory.
* `hpp_to_h.py` - Convert all .hpp files to .h and fix the includes,
* `mock_maker.py` - Make mock files based on a directory,
* `replacer.py` - Replace a string with another in a directory recursively.
* `scan.py` - Find a string in files from a folder recursively.
* `todo_finder.py` - Find //TODO-s in a src folder.

## flatten.py

Can be used to flatten a src directory.
You can change these values to fine-tune the script for your needs.

`src_directory = './src' #The source folder (recursive)`
`dest_directory = './flattened' #The destination folder`

## hpp_to_h.py

Can be used to convert all the file and includes of .hpp files to .h files.

### Arguments
`project_directory`: The path of your src folder.

After running the script it will replace your source folder with the modifications so it is recommended to make a backup of your source folder in case something fails.

## mock_maker.py

Can be used to create mock files from a directory. This means that if you need testing but you don't want to include all the images/sounds/any big files you are using in your main project, you can create mock files.

These mock files:
- Mimic the name and extension of the files in the source folders.
- Have 0 content in them, they are just mock files.
- Mimic the relative location of the original files.

These mock files can serve as a replacement for your original files in your testing environment.

### Arguments
`source`: The directory where the original files are being located.
`destination`: The destination directory where the mock files will be created.

## replacer.py

Can be used to find and replace a string in all files of a directory.

### Input
`input_dir`: The directory to scan.
`search_str`: The string to find.
`repl_str`: The string which will replace the original string.
`html_only`: If "y" then only .php and .html files will be scanned.

## scan.py

Can be used to find a string in all files of a directory.

### Input
`input_dir`: The directory to scan.
`search_str`: The string to find.
`html_only`: If "y" then only .php and .html files will be scanned.

## todo_finder.py

Find `//TODO`-s in a src folder.

### Input
`folder_path`: The directory where the TODO comments need to be listed.