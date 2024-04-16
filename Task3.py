import spacy, nltk

def tokenize_sentences(text, language):
  """Tokenizes text into sentences using spaCy for a specified language.
  Args:
      text: The input text to tokenize.
      language: The language code (e.g., "en", "es", "fr").
  Returns:
      A list of sentences after tokenization.
  """
  nlp = spacy.load(language)
  doc = nlp(text)
  sentences = [sent.text.strip() for sent in doc.sents]
  return sentences

# Example usage (modify language code as needed)
text = "Esta es una oración de ejemplo en español."  # Spanish example
language = "es"
sentences = tokenize_sentences(text, language)
print("Tokenized sentences:")
for sentence in sentences:
  print(sentence)

#####################################################################
def compare_pos_tags(text):
  """Performs part-of-speech (POS) tagging with two tagsets and compares results.
  Args:
      text: The input text for tagging.
  Returns:
      None (prints POS tag comparisons to console).
  """

  nlp_universal = spacy.load("en_core_web_sm")  # Universal Dependencies
  nlp_perceptron = spacy.load("en_core_web_trf")  # Perceptron model

  print("POS Tagging Comparison:")
  print("Text:", text)

  for nlp in [nlp_universal, nlp_perceptron]:
    doc = nlp(text)
    print(f"\nTagset: {nlp.tag_}")
    for token in doc:
      print(f"{token.text:<20}{token.pos_:<10}{token.tag_:>10}")

# Example 
text = "The quick brown fox jumps over the lazy dog."

compare_pos_tags(text)

###################################################################
def get_stopwords(language):
  """Downloads and returns a list of stopwords for a specified language (NLTK).

  Args:
      language: The language code (e.g., "english", "spanish", "french").

  Returns:
      A list of stopwords in the requested language.
  """

  nltk.download("stopwords")  # Download stopwords resource if not already available

  try:
    stopwords = nltk.corpus.stopwords.words(language)
  except LookupError:
    print(f"Stopwords not available for language: {language}")
    stopwords = []

  return stopwords

# Example usage (modify language code as needed)
languages = ["english", "spanish", "french"]

for language in languages:
  stopwords = get_stopwords(language)
  print(f"Stopwords for {language}:")


