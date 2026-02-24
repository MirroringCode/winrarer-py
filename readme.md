# Winrarer.py

This is a script that I made to practice my skill making CLI utilities with Python. This is a prototype that I'm planning on expanding

## Expected arguments for the Script

**Positional argument**

`rar_name`: Is the chosen name for the resulting compressed file. At this moment all the compressed files will have the `.rar` extension

**Optional arguments**

`-f --file`: The file you wish to compress
`-d --dir`: The directory where that file is located. If no directory is provided the script will use the current directory

## TODO

- Support for wildcards when compressing several files (Ex: `python winrarer.py my_file.rar *.txt` ).
- Allow to choose a different extension other than RAR
- Handle string names with several dots (Ex: `data.sql.bak`, `file_with_dots....` and other script breaking variations).
- Add a confirmation prompt if the user wishes to compress all files if no file was provided in the `-f` arg. This is the current script behavior that if no file was provided it'll compress all files in the directory.
- Make it Linux & Mac friendly. Current script check if WinRAR is installed in the Windows filesystem.
- Possibility to create a password when generating the compressed file.

## Why I made this script?

Because I felt like tinkering with python and because at work I needed to compress a lot of files to `.rar`