import subprocess
import os
import sys
import argparse
from pathlib import Path

RAR_LOCATION = r"C:/Program Files/WinRAR"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", 
                        help="The directory with files to be compressed. If no directory is " \
                        "provided the script will use current working directory", 
                        type=Path)

    parser.add_argument("-f", "--file",
                        help="The file to be compressed. Wildcards can be used to filter between filename or extension." \
                        "Ex: python winrarer.py --file *.txt",
                        type=str)

    parser.add_argument("rar_name",
                        help="Resulting rar file name",
                        type=str)

    args = parser.parse_args()


    dir_to_compress = args.dir or os.getcwd()



    if not os.path.isdir(RAR_LOCATION):
        print('rar command not found. Verify it is installed on your system', file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(dir_to_compress):
        print(f"Directory not found {dir_to_compress}", file=sys.stderr)
        sys.exit(1)

    os.chdir(dir_to_compress)


    if args.file is not None and not os.path.exists(args.file):
        print(f"File not found {args.file}", file=sys.stderr)
        sys.exit(1)


    archivo = ''
    if args.rar_name.endswith(".rar"):
        archivo = args.rar_name
    elif args.rar_name.endswith('.'):
        archivo = "".join([args.rar_name[:-1], ".rar"])    
    else:
        archivo = "".join([args.rar_name, ".rar"])


    subprocess.run(['rar', 'a', archivo, args.file or ''])
if __name__ == "__main__":
    main()

