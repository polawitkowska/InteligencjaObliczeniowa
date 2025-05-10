from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import wordcloud
import matplotlib.pyplot as plt

with open('./lab08/article.txt', 'r', encoding='utf-8') as file:
    article = file.read()

tokens = word_tokenize(article)
# print(len(tokens)) #969

stop_words = set(stopwords.words('english'))
additional_stop_words = ["'s", "'re", "n't", "'we", "'my", "(", ")", "%", ",", ".", "``", "-", "''", "?", "'", ":", "said", "yet", "told", "must", "make", "also", "might", "many", "already", "almost", "say", "following"]
for w in additional_stop_words:
    stop_words.add(w)

filtered_article = [w for w in tokens if not w.lower() in stop_words]
# print(filtered_article) #na początku: 613 po dodaniu dodatkowych słów: 460

lemmatizer = WordNetLemmatizer()

lemmatized_article = [lemmatizer.lemmatize(token) for token in filtered_article]
# print(len(lemmatized_article)) #460

word_counts = Counter(lemmatized_article)
# print(word_counts)

# 10 najczęstszych słów
# most_common = word_counts.most_common(10)
# words = [word for word, count in most_common]
# counts = [count for word, count in most_common]

# Wykres słupkowy najczęstszych słów
# plt.figure(figsize=(12, 6))
# plt.bar(words, counts)
# plt.title('10 najczęściej występujących słów')
# plt.xlabel('Słowa')
# plt.ylabel('Liczba wystąpień')
# plt.show()

# Word Cloud
# with open('./lab08/lemmantized_article.txt', 'r', encoding='utf-8') as file:
#     lemmatized_article_txt = file.read()
# wordcloud = wordcloud.WordCloud(max_words=100, background_color="white").generate(lemmatized_article_txt)

# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()