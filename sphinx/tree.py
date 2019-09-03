import glob
import os
from pathlib import Path, PurePosixPath
import argparse
import json

def init_parser():
    parser = argparse.ArgumentParser(description='Documentation tree generator.')

    parser.add_argument('-e', '--ext', default='.md', choices=['.md', '.markdown'], help='documentation file extention.')
    parser.add_argument('-s', '--source', default='.', help='Relative path to the source files.')
    parser.add_argument('-n', '--name', default='tree', help='output file files.')

    return parser

def strip_path(file_path, base_path, ext):
    return str(PurePosixPath(Path(file_path.replace(base_path, '').strip('\\\\').replace(ext, ''))))

def resolve_documentation_path(args):
    script_base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), args.source)

    return str(Path(script_base_path).resolve())

def generate_tree(args, documentation_path):
    glob_path = os.path.join(documentation_path, "**/*%s" % args.ext)

    return [strip_path(f, documentation_path, args.ext) for f in glob.glob(glob_path, recursive=True) if not any(substring in f for substring in ['404', 'index'])]

def save_tree(args, documentation_tree, documentation_path):
    with open(os.path.join(documentation_path, args.name.split('.')[0] + '.json'), 'w') as f:
        json.dump(documentation_tree, f, indent=4)

if __name__ == "__main__":
    args = init_parser().parse_args()
    documentation_path = resolve_documentation_path(args)
    documentation_tree = generate_tree(args, documentation_path)

    save_tree(args, documentation_tree, documentation_path)