from functools import reduce

def find_longest_word(words):
    # Define a function that compares two words and returns the longer one
    def longer_word(word1, word2):
        return word1 if len(word1) > len(word2) else word2

    # Use reduce to apply the longer_word function across the array of strings
    longest_word = reduce(longer_word, words)
    return longest_word

# Example usage
words = ["apple", "banana", "cherry", "blueberry", "strawberry"]
longest = find_longest_word(words)
print("The longest word is:", longest)