import os
folder_path = "D:\girija"
file_name = "cybersecurity.txt"
full_path = os.path.join(folder_path, file_name)
try:
    with open(full_path, "r") as file:
        content = file.read()
        print("--- File Content ---")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found in '{folder_path}'.")
with open("cybersecurity.txt", "r") as file:
    text = file.read()
target_char = "e"
char_count = text.lower().count(target_char.lower())
words = text.split()
clean_words = [word.strip(".,!?;:") for word in words]
sorted_words = sorted(clean_words, key=lambda s: s.lower())
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"1. The character '{target_char}' appears {char_count} times.")
print(f"2. Total vowels in the file: {vowel_count}")
print("3. Words sorted alphabetically:")
print(sorted_words)    
