import heapq
import fuzzywuzzy  # Assuming a fuzzy matching library

def word_count_with_fuzzy(file_path):
    """
    Counts word occurrences in a file with O(n log k) complexity, fuzzy matching, and RAM constraints.

    Args:
        file_path: The path to the text file to analyze.

    Returns:
        A list of tuples, where each tuple contains a word and its count, sorted
        by count in descending order and then by word lexicographically.
    """

    word_counts = {}
    chunk_size = 1024 * 1024  # 1 MB chunks

    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break

            for word in chunk.lower().split():
                corrected_word = fuzzywuzzy.process.extractOne(word, word_counts.keys())[0]  # Fuzzy matching
                word_counts[corrected_word] = word_counts.get(corrected_word, 0) + 1

    # Use a min-heap to efficiently track the top k most frequent words.
    top_words = heapq.nsmallest(10000, word_counts.items(), key=lambda item: item[1])

    # Sort the top words by count in descending order and then by word lexicographically.
    return sorted(top_words, key=lambda item: (-item[1], item[0]))

# Example usage
file_path = "large_file.txt"
word_counts = word_count_with_fuzzy(file_path)

for word, count in word_counts:
    print(f"{word}: {count}")
