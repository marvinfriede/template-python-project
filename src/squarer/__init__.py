"""
Entry point for command line interface.
"""

import argparse
import sys
from .maths import square_a_number as square
from .__version__ import __version__

def main() -> None:
    
    # get command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "number",
        type=float,
        help="Number to square."
    )
    args = parser.parse_args()
    
    
    print(square(args.number))
    


if __name__ == '__main__':
    sys.exit(main())