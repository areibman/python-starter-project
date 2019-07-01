#!/usr/bin/env python3
"""
Docstring goes here. Is stored as __doc__
"""


import argparse
import sys
import os

# When importing python files from other directories
repo_path = os.path.expanduser(os.environ.get('PATH_TO_REPOS', '~/axio'))
sys.path.insert(0, os.path.expanduser(
    os.path.join(repo_path, 'data-science', 'c2m2_analytics', 'src')))


def foo():
    """Example function with types documented in the docstring.
    Args:
        param1 (int): The first parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)

    # When flag is used, stores as true
    parser.add_argument("-s", "--sample",
                        action='store_true', help='Sample arg')

    # When flag is used, stores number set in const. Otherwise, defaults to const.
    parser.add_argument("-n", "--number",
                        action='store_const', help='Number arg', const=42)

    # Flag is required to be used
    parser.add_argument("-a", "--assessments json", type=str,
                        required=True, help="Required string flag")

    # Flag is optional
    parser.add_argument("-o", "--optional arg", type=str, required=False)

    # Non-optional arguments save to value
    parser.add_argument('-v', '--value', action="store", dest="val")

    # create our group of mutually exclusive arguments
    mutually_exclusive = parser.add_mutually_exclusive_group()
    mutually_exclusive.add_argument("--foo", help="foo excludes bar")
    mutually_exclusive.add_argument("--bar", help="bar excludes foo")

    # When no arguments are provided, print the help string.
    # Place just before parser.parse_args()
    if len(sys.argv[1:]) == 0:
        parser.print_help()

    # Assigning variables to args
    args = parser.parse_args()

    if args.__dict__.get('optional arg'):
        optional = args.optional_arg
    else:
        pass
