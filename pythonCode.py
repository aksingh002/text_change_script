import csv
import re
import time
import psutil

# Define file paths
input_file_path = "t8.shakespeare.txt"
find_words_list_file_path = "find_words.txt"
dictionary_file_path = "french_dictionary.csv"
output_file_path = "t8.shakespeare.translated.txt"
frequency_file_path = "frequency.csv"

# Load find words list
with open(find_words_list_file_path, "r") as f:
    find_words = set(line.strip() for line in f)

# Load dictionary
with open(dictionary_file_path, "r") as f:
    reader = csv.reader(f)
    dictionary = {row[0]: row[1] for row in reader}

# Define regular expression for finding words
word_pattern = re.compile(r"\b\w+\b")

# Define counters
replacements = 0
unique_replacements = set()
word_counts = {}

# Process input file
with open(input_file_path, "r") as f_in, open(output_file_path, "w") as f_out:
    for line in f_in:
        words = word_pattern.findall(line)
        for word in words:
            if word in find_words and word.lower() in dictionary:
                replacement = dictionary[word.lower()]
                if word.istitle():
                    replacement = replacement.capitalize()
                elif word.isupper():
                    replacement = replacement.upper()
                line = line.replace(word, replacement)
                replacements += 1
                unique_replacements.add(word)
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

        f_out.write(line)

# Write frequency file
with open(frequency_file_path, "w", newline='') as f_freq:
    writer = csv.writer(f_freq)
    writer.writerow(["English Word", "French Word", "Frequency"])
    for word, count in word_counts.items():
        if word in dictionary:
            writer.writerow([word, dictionary[word], count])

# End timing and memory usage
end_time = time.time()
end_memory = psutil.Process().memory_info().rss

# Print results
print(f"Unique list of words that was replaced with French words from the dictionary: {unique_replacements}")
print(f"Number of times a word was replace: {replacements}")
print(f"Time taken to process: {end_time -end_time:.2f} seconds")
print(f"Memory taken to process: {(end_memory -end_memory) / (1024*1024):.2f} MB")
