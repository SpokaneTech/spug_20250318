# calc is the entry point for the CLI application.
import argparse
import sys

from utils import add, divide, multiply, subtract


def main():
    """Main entry point for the CLI application, which parses the arguments and calls the appropriate function."""
    parser = argparse.ArgumentParser(description="CLI Calculator")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument(
        "operator",
        choices=["add", "subtract", "multiply", "divide"],
        help="Operation to perform",
    )
    args = parser.parse_args()

    if args.operator == "add":
        result = add(args.num1, args.num2)
    elif args.operator == "subtract":
        result = subtract(args.num1, args.num2)
    elif args.operator == "multiply":
        result = multiply(args.num1, args.num2)
    elif args.operator == "divide":
        try:
            result = divide(args.num1, args.num2)
        except ValueError as e:
            print(e)
            return

    print(f"Result: {result}")


if __name__ == "__main__":
    """This block of code is executed when the script is run from the command line."""
    sys.exit(main())
