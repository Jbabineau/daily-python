import os

full_name = input('Please enter your full name: ')

print(f"Your name in uppercase: {full_name.upper()}")
print(f"Your name in lowercase: {full_name.lower()}")
print(f"Total number of characters (excluding spaces): {len(full_name.replace(' ', ''))}")
print(f"You name reversed: {full_name[::-1]}")