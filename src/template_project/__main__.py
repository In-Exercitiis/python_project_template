'''Python project main entry point. Typically where argparse or config
parsing would happen.

'''

from argparse import ArgumentParser


def script_fn(param=None):
    parser = ArgumentParser()
    parser.parse_args()
    print parser
    if param:
        raise Exception('no params!')
    return 1
