import csv
import os.path

words = []

while True:
    original_word = input("Enter a word in Language 1 (or type 'done' to finish): ").lower()
    if original_word == 'done':
        break
    translated_word = input(f"Enter the translation of '{original_word}' in Language 2: ").lower()
    words.append({"word": original_word, "translation": translated_word})

existing_file = False
if os.path.isfile("translation.csv"):
    existing_file = True

with open("translation.csv", 'a', newline='') as csvfile:
    translation = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    if not existing_file:
        translation.writerow(["original word", "translated word"])
    
    for item in words:
        translation.writerow([item["word"], item["translation"]])
