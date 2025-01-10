def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    count = count_words(book_text)
    print(count)


def get_book_text(file: str):
    with open(file) as f:
        return f.read()


def count_words(text: str):
    words = text.split()
    return len(words)


if __name__ == "__main__":
    main()