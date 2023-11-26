import nltk
from nltk.corpus import wordnet
import random

# download wordnet
nltk.download('wordnet')

def get_synonym(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    if word in synonyms:
        synonyms.remove(word)
    return random.choice(list(synonyms)) if synonyms else word


with open('/content/googletrans.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()


new_translations = []
for line in lines:
    words = line.strip().split()
    new_words = [get_synonym(word) for word in words]
    new_translations.append(' '.join(new_words))


with open('new_translations.txt', 'w', encoding='utf-8') as f:
    for line in new_translations:
        f.write(line + '\n')