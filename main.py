import sys
from ssvepbox import *


def main():
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "file")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        text = f.read()

if __name__ == "__main__":
    main()
