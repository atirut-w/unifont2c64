from argparse import ArgumentParser


def main(args: dict[str, any]) -> None:
    characters: dict[int, int] = {}

    try:
        with open(args.input, "r") as f:
            for line in f:
                codepint, bitmap = line.strip().split(":")
                characters[int(codepint, 16)] = int(bitmap[:16], 16)
    except FileNotFoundError:
        print(f"File not found: {args.input}")
        exit(1)

    if len(characters) > 128:
        print(f"Warning: {len(characters)} characters found, only 128 will be used")

    with open(args.output, "wb") as f:
        for i in range(128):
            character: int

            match args.encoding:
                case "ascii":
                    character = characters.get(i, 0)
                case _:
                    print(f"Unknown encoding: {args.encoding}")
                    exit(1)

            f.seek(i * 8)
            f.write(character.to_bytes(8, "big"))
        
        for i in range(128, 256):
            character = characters.get(i - 128, 0) ^ 0xffffffffffffffff
            f.seek(i * 8)
            f.write(character.to_bytes(8, "big"))
        
        print("TODO: alternate character set")
        f.write(b"\x00" * 2048)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="unifont2c64", description="convert Unifont .hex to C64 character ROM"
    )
    parser.add_argument("input", help="input file")
    parser.add_argument("-o", "--output", help="output file", default="font.bin")
    parser.add_argument("-e", "--encoding", help="text encoding", default="ascii")

    main(parser.parse_args())
