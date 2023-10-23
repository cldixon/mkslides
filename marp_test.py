import subprocess


def main():
    sp = subprocess.run(
        ["marp", "decks/my-example-deck.md"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )
    print(sp)
    return 


if __name__ == '__main__':
    main()