input_file = 'input.txt'
output_file = 'output.txt'

with open(input_file, 'r') as file:
    content = file.read()

# Count lines, words, and characters
num_lines = content.count('\n') + (1 if content else 0)
num_words = len(content.split())
num_chars = len(content)

print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")
print(f"Number of characters: {num_chars}")

modified_content = content.replace('Python', 'programming')

with open(output_file, 'w') as file:
    file.write(modified_content)
