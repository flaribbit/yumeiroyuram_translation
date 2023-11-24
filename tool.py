import sys


def split(filepath):
    f1 = open("1.txt", "w", encoding="utf8")
    f2 = open("2.txt", "w", encoding="utf8")
    f3 = open(filepath, "r", encoding="utf8")
    while True:
        line = f3.readline()
        if not line:
            break
        f1.write(line)
        line = f3.readline()
        f2.write(line)
    f1.close()
    f2.close()
    f3.close()


def merge(filepath):
    f1 = open("1.txt", "r", encoding="utf8")
    f2 = open("2.txt", "r", encoding="utf8")
    f3 = open(filepath, "w", encoding="utf8")
    for line1, line2 in zip(f1, f2):
        f3.write(line1)
        f3.write(line2)
    f1.close()
    f2.close()
    f3.close()


def main():
    args = sys.argv
    if len(args) != 3:
        print("Usage: python tool.py split/merge filepath")
        print("Example: python tool.py split Talk.txt")
        print("    split `Talk.txt` into `1.txt` and `2.txt`")
        print("Example: python tool.py merge Talk.txt")
        print("    merge `1.txt` and `2.txt` into `Talk.txt`")
        sys.exit(1)
    if args[1] == "split":
        split(args[2])
    elif args[1] == "merge":
        merge(args[2])


if __name__ == "__main__":
    main()
