import argparse

parser = argparse.ArgumentParser(description='ROSE Online asset extractor')
parser.add_argument('idx_file', type=argparse.FileType('rb'), help='The path to the IDX file of an installation of ROSE')
parser.add_argument('dest_dir', type=str, help='The path to a folder to dump the build configuration')


def main():
    import os
    from portship.portship import generate_ninja

    args = parser.parse_args()

    if not os.path.isdir(args.dest_dir):
        raise Exception('path is not a directory: {}'.format(args.dest_dir))

    generate_ninja(idx=args.idx_file, dest=args.dest_dir)


if __name__ == '__main__':
    main()
