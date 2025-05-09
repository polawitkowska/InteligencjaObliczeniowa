from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt

with open('./lab08/article.txt', 'r', encoding='utf-8') as file:
    article = file.read()

tokens = word_tokenize(article)
# print(len(tokens)) #969

stop_words = set(stopwords.words('english'))
additional_stop_words = ["'s", "'re", "n't", "(", ")", "%", ",", ".", "``", "-", "''", "?", "'", ":"]
for w in additional_stop_words:
    stop_words.add(w)

filtered_article = [w for w in tokens if not w.lower() in stop_words]
# print(len(filtered_article)) #na początku: 613 po dodaniu dodatkowych słów: 492

lemmatizer = WordNetLemmatizer()

lemmatized_article = [lemmatizer.lemmatize(token) for token in filtered_article]
# print(len(lemmatized_article)) #492

word_counts = Counter(lemmatized_article)
# print(word_counts)

most_common = word_counts.most_common(10)
words = [word for word, count in most_common]
counts = [count for word, count in most_common]

plt.figure(figsize=(12, 6))
plt.bar(words, counts)
plt.title('10 najczęściej występujących słów')
plt.xlabel('Słowa')
plt.ylabel('Liczba wystąpień')
plt.show()