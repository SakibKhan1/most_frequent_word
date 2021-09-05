def most_frequently_occuring_word(strings):

    word_counts = {}

    most_word = ""
    most_word_count = 0


    for s in strings:

        words = s.split() 

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
    "it should return the word it", "and if it didn't then I messed up",
    "feel free to flame me"
]

test2 = ["something simpler", "much simpler", "nonsense words"]

print(most_frequently_occuring_word(test1))  # "it"
print(most_frequently_occuring_word(test2))  # "simpler"
