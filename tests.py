import pytest
import argparse
import sys
from argparse import

# Setup
@pytest.fixture(scope="session")
def fixture_instance():
    """ Function that runs before all tests. May return a variable that can be
        used as an argument in pytest functions and tests.
    """
    # Manually override CLI arguments
    sys.argv = [sys.argv[0]] + ['-o', 'overriden_arg']

    args = process_pytest_args()
    return ''


def process_pytest_argparse():
    """ Returns arguments submited by running a .py file.
        Ex: `pytest tests.py -v var_name --flag`
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


class TestClassTitle:
    """ Classes are used to group tests of similar nature. This treats all
        tests within a class as a single test. If a single test fails,
        the entire class fails.
    """

    def test_do_something(self, db_instance):
        """ Does something
        """
        pass

    @pytest.mark.parametrize("query_file_path,expected_hits", [
        ('something', 'or other')
    ])
    def test_tags_applied_correctly(self, query_file_path, expected_hits):
        pass
