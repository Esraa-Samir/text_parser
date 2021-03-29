import sys
from Factory import ObjectParser


if __name__ == '__main__':
    format = (sys.argv[1]).upper()
    files = sys.argv[2:]

    parser = ObjectParser()
    parser.parse(files, format)


