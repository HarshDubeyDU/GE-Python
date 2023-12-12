file = open("sample_file.txt", "r")

# 1. Total number of characters, words and lines in file.
file_data = file.read()
number_of_characters = len(file_data)
number_of_words = len(file_data.split())
number_of_lines = len(file_data.split("\n"))
print("No. of characters in given file:", number_of_characters)
print("No. of words in given file:", number_of_words)
print("No. of lines in given file:", number_of_lines)


# 2. Frequency of each character in file.
character_frequency = {}
for character in file_data:
    character_frequency[character] = character_frequency.get(character, 0) + 1
print("Frequency of each character in file:", str(character_frequency))

# 3. Words in Reverse order.
reverse_words = file_data.split(" ")
reverse_words = " ".join(reversed(reverse_words))
print("Words of file in reverse order:", reverse_words)

# 4. Even lines in "file1" and odd lines in "file2".
file1 = open("file1.txt", "w")
file2 = open("file2.txt", "w")
file_data_write = file_data.split("\n")
for i in range(len(file_data_write)):
    if i % 2 == 1:
        file1.write(file_data_write[i] + "\n")
    else:
        file2.write(file_data_write[i] + "\n")

file.close()
