def count_words(text):
    """Returns the number of words in the given text string."""
    words = text.split()
    return len(words)

def get_char_counts(text):
    """Returns a dictionary with the count of each character in the text."""
    counts = {}
    for char in text.lower():  # convert everything to lowercase
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_char_counts(char_counts):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries.
    Each dictionary looks like: {"char": "a", "num": 1234}.
    Sorted by num (descending).
    Skips non-alphabetical characters.
    """
    # Convert dict into list of {"char": ..., "num": ...}
    char_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]
    
    # Sort descending by "num"
    char_list.sort(key=lambda item: item["num"], reverse=True)
    
    return char_list