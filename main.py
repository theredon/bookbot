def main(file):
    with open(file) as f:
        file_contents = f.read()
    print(file_contents)
    f.close()


if __name__ == "__main__":
    main("books/frankenstein.txt")