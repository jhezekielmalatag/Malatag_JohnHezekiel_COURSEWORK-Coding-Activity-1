# Get a sentence
sentence = input("Enter a sentence: ")

# Convert the sentence to uppercase and lowercase
upper = sentence.upper()
lower = sentence.lower()
print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")

# Count the number of words in the sentence
count = sentence.lower().count('a')
print(f"The letter 'a' appears {count} times in the sentence.")

# Start with Hello
start = sentence.startswith("Hello")
print(f"Start with 'Hello': {start}")

# Split the sentence
words = sentence.split()
print("Words in the sentence:")
for word in words:
    print(word)