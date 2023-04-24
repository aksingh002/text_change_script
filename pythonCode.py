import csv

# Open the input text file
with open('shakespeare.txt', 'r') as f:
    shakespeare = f.read()

# Open the words list text file
with open('find_words.txt', 'r') as f:
    find_words = f.read().split()

# Load the dictionary CSV file into a dictionary
french_dictionary = {}
with open('french_dictionary.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        french_dictionary[row[0]] = row[1]

# Find all the words in the input text file that are in the words list and have a replacement word in the dictionary
replacements = {}
for word in shakespeare:
    if word in find_words and word in french_dictionary:
        replacements[word] = french_dictionary[word]

# Replace the words in the input text file with their corresponding replacement words from the dictionary
for word, replacement in replacements.items():
    shakespeare = shakespeare.replace(word, replacement)

# Write the modified input text to a new file
with open('output.txt', 'w') as f:
    f.write(shakespeare)