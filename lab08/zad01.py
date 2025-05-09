import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

with open('./lab08/article.txt', 'r', encoding='utf-8') as file:
    article = file.read()

stop_words = set(stopwords.words('english'))

additional_stop_words = ["'s", "'re", "n't", "(", ")", "%", ",", ".", "``", "-", "''", "?", "'", ":"]
for w in additional_stop_words:
    stop_words.add(w)

tokens = word_tokenize(article)

# print(len(tokens)) #969

filtered_article = [w for w in tokens if not w.lower() in stop_words]
# print(len(filtered_article)) #613
# print(len(filtered_article)) #492

lemmatized_article = set()
for w in filtered_article:
    word = lemmatizer.lemmatize(w)
    lemmatized_article.add(word)

# print(len(lemmatized_article)) #285