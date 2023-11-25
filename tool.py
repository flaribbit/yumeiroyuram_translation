import sys


def split(filepath):
    f1 = open("1.txt", "w", encoding="utf8")
    f2 = open("2.txt", "w", encoding="utf8")
    f3 = open(filepath, "r", encoding="utf8")
    for line1, line2 in zip(f3, f3):
        f1.write(line1)
        f2.write(line2)
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


def subset(filepath, current_fontpath, fallback_fontpath):
    from fontTools.ttLib import TTFont
    from fontTools.subset import Subsetter

    charset = set()
    missing = []
    with open(filepath, "r", encoding="utf8") as f1:
        for _, line in zip(f1, f1):
            for c in line:
                charset.add(c)

    # check missing chars
    font = TTFont(current_fontpath)
    cmap = font.getBestCmap()
    for c in charset:
        if ord(c) not in cmap:
            missing.append(c)
    font.close()
    missing_text = "".join(missing)
    print(f"missing text: {missing_text}")

    # generate fallback font
    font = TTFont(fallback_fontpath)
    subsetter = Subsetter()
    subsetter.populate(text=missing_text)
    subsetter.subset(font)
    font.save("missing.otf")


def main():
    args = sys.argv
    if args[1] == "split":
        split(args[2])
    elif args[1] == "merge":
        merge(args[2])
    elif args[1] == "subset":
        subset(args[2], args[3], args[4])


if __name__ == "__main__":
    main()
