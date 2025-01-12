def main():
    book_path: str = "books/frankenstein.txt"
    book_text: str = get_book_text(book_path)
    count: int = count_words(book_text)
    char_count: dict = count_characters(book_text)
    sorted_char_count: list = dict_to_be_sorted(char_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    for char in sorted_char_count:
        if not char["char"].isalpha():
            continue                
        print(f"The {char['char']} character was found {char['num']} times")
    print("--- End report ---")


def get_book_text(file: str):
    with open(file) as f:
        return f.read()


def count_words(text: str):
    words: list = text.split()
    return len(words)


def count_characters(text: str):
    characters: dict = {}
    for c in text:
        lowercase = c.lower()
        if lowercase in characters:
            characters[lowercase] += 1
        else:
            characters[lowercase] = 1
    return characters


def sorted_on(dictionary: dict):
    return dictionary["num"]


def dict_to_be_sorted(characters: dict):
    sorted_list: list = []
    for key in characters:
        sorted_list.append({"char": key, "num": characters[key]})
    sorted_list.sort(reverse=True, key=sorted_on)
    return sorted_list
    

if __name__ == "__main__":
    main()