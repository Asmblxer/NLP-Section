import nltk

def process_text(text, choice):

  tokens = nltk.word_tokenize(text)
  sentences = nltk.sent_tokenize(text)

  if choice == 1:
    return tokens
  elif choice == 2:
    return sentences
  elif choice == 3:
    return text.split()
  else:
    return "Invalid choice. Please enter 1, 2, or 3."

text = input("Enter your text: ")

print("\nChoose an option:")
print("1. Print tokenized words")
print("2. Print tokenized sentences")
print("3. Print output using split function")

choice = int(input("Enter your choice: "))

processed_text = process_text(text, choice)

print("\nOutput:")
print(processed_text)

