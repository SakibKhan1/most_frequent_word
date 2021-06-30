# Given a list of phrases represented as strings, return the most frequently occurring word amongst all the phrases.

# EXAMPLE
# strings = [ “hello foo bar”, “one two three four bar”, “apple orange banana foo bar” ] 

def most_frequently_occuring_word(strings):
    # We need to keep track of how often each word occurs, so let's use a dictionary for this. Each key will be the word, and the corresponding value will be the frequency (or 'count') of that word.
    word_counts = {}

    # We also need to keep track of the current most frequently occuring word and its count since dictionaries. We'll update this as we count the words
    most_word = ""
    most_word_count = 0

    # One for-loop so we can check each string
    # strings = [ “hello foo bar”, “one two three four bar”, “apple orange banana foo bar” ] 
    for s in strings:

        # '.split()' allows us to easily break each string into its separate words (assuming each word is separated by whitespace).
        words = s.split() # [hello, foo, bar]

        # We can then iterate over each word in that string.
        for word in words:

            # If the word isn't yet in the count dictionary, add it with a starting count of 1. Otherwise, increase the count.
            if word not in word_counts:
                word_counts[word] = 1   
            else:
                word_counts[word] += 1

            # If the newly updated word is now the most frequently occuring, update the return value.
            if word_counts[word] > most_word_count:
                most_word = word
                most_word_count = word_counts[word]

    # This occurs after all strings and words have been iterated over. Return the most frequently occuring word.
    return most_word


test1 = [
    "hi hello how are you", "i promise this works", "seriously give it a try",
    "it should return the word it", "and if it didn't Richard messed up",
    "feel free to flame him in the chat"
]

test2 = ["something simpler", "much simpler", "nonsense words"]

print(most_frequently_occuring_word(test1))  # "it"
print(most_frequently_occuring_word(test2))  # "simpler"
