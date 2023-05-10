from argparse import ArgumentParser


def main(args: dict[str, any]) -> None:
    try:
        with open(args.input, "r") as f:
            pass
    except FileNotFoundError:
        print(f"File not found: {args.input}")
        exit(1)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="unifont2c64", description="convert Unifont .hex to C64 character ROM"
    )
    parser.add_argument("input", help="input file")
    parser.add_argument("-o", "--output", help="output file", default="font.bin")
    parser.add_argument("-e", "--encoding", help="text encoding", default="ascii")

    main(parser.parse_args())
