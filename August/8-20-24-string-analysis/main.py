import re
from collections import defaultdict

text = input("Please enter a block of text for analysis: ")

words = re.findall(r'\b\w+\b', text)
sentences = []
try:
    sentences = re.split(r'[.!?]\s*', text)
    sentences = [s for s in sentences if s.strip()]
except Exception as e:
    print(e)

characters = text.replace(' ', '')

unique_words = defaultdict(int)

for word in words:
    unique_words[word] += 1

max_occurance = max(unique_words, key=unique_words.get)


print(f'The number of words in the text: {len(words)}')
print(f'The number of sentences in the text: {len(sentences)}')
print(f'Number of characters: {len(characters)}')
print(f"Most frequent word: '{max_occurance}' (used {unique_words[max_occurance]} times)")
print(f"Average Word Length: {round(len(characters)/len(words), 2)} characters")
print(f"Average Sentence Length: {round(len(words)/len(sentences), 2)} words")