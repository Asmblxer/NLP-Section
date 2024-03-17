import csv
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

data = []
with open('kaggelDataset.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    text = row[0]
   
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]    
    data.append(stemmed_tokens)
    
for row in data:
  print(row)
