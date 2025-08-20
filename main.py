import sys
from stats import count_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    """Reads the contents of the given file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # Use relative path to frankenstein.txt
    # text = get_book_text("books/frankenstein.txt")
    # num_words = count_words(text)
    # print(f"{num_words} words found in the document")
    
    # char_counts = get_char_counts(text)
    # print("Character counts:")
    # print(char_counts)
    
    # Ensure correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    # Read text
    text = get_book_text(filepath)

    # Word count
    word_count = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Character count (dictionary)
    char_counts = get_char_counts(text)

    # Sorted character list
    sorted_chars = sort_char_counts(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

# Run the program
if __name__ == "__main__":
    main()