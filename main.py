def main(file):
    with open(file) as f:
        file_contents = f.read()
    # print(file_contents)
    count_words(file_contents)
    f.close()

def count_words(text: str):
    words = text.split()
    count = len(words)
    print(count)

if __name__ == "__main__":
    main("books/frankenstein.txt")