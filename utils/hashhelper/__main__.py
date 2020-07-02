import argparse

from . import alphabetical, combine

# create the top-level parser
parser = argparse.ArgumentParser(
    description="HashHelper by Denver 'DrTexx'", prog="hashhelper"
)
# parser.add_argument("--foo", action="store_true", help="foo help")
subparsers = parser.add_subparsers(help="sub-command help", dest="command")

parser_a = subparsers.add_parser("sort", help="sort help")
parser_a.add_argument("filepath", type=str, help="filepath to filelist")

parser_b = subparsers.add_parser("check", help="conflict checker help")
parser_b.add_argument("filepath", type=str, help="filepath to filelist")

parser_c = subparsers.add_parser("combine", help="combine help")
parser_c.add_argument("filepath", type=str, help="filepath to filelist")
parser_c.add_argument("filepath2", type=str, help="filepath to second filelist")

# parse some argument lists
# parser.parse_args(['a', '12'])
# parser.parse_args(['--foo', 'b', '--baz', 'Z'])

args = parser.parse_args()
print(args)

command = args.command

if command == "sort":
    print("sorting...")
    alphabetical.do_sort(args.filepath)

elif command == "check":
    print("checking for conflicts...")

elif command == "combine":
    print("combining...")
    combine.do_combine(args.filepath, args.filepath2)

else:
    print("invalid command!")
