import argparse
import sys


def get_argparse():
    """ Returns arguments submited by running a .py file.
        Ex: `python3 sample.py -f image.jpg -p book.pdf --verbose`
    """
    parser = argparse.ArgumentParser(description=__doc__)

    # Set an optional flag that defaults to a value.
    parser.add_argument("-a", default="abc")

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
    return parser.parse_args()
