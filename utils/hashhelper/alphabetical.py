from pathlib import Path


def do_sort(filepath):
    pFilepath = Path(filepath)
    print(pFilepath.absolute())

    sorted = ""

    with open(pFilepath.absolute(), "r+") as f:
        lines = f.readlines()
        lines.sort()
        sorted = "".join(lines)

    with open(str(pFilepath.absolute()) + ".new.txt", "w+") as f:
        f.write(sorted)
