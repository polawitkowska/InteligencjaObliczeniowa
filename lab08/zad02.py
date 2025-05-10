from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline

# Jedna pozytywna i jedna negatywna recenzja hotelu Holiday Inn Express Warsaw - Mokotow by IHG
positive_review = "Exceeded my expectations!\
This hotel exceeded my expectations. Professional and friendly staff. Very clean rooms, bedding sheets... very comfy pillows. Absolutely amazing breakfast! 10 min from airport! Great value for the money!!"

negative_review = "We arrived little bit late time of the day, was very tired from our trip and the front desk man was so rude and currish. He registered us for a very long time and when we asked to speed up the process, he began to insult us and said that he was very tired! our friends who came to pick us up for dinner, the man insulted them and kicked them out into the street! This shocked us as this was the first time we had encountered such a terrible scandal. Of course, we never come back and we want to warn others guests!!!!\
the hotel is on the second floor, you have to lift your bags up a narrow staircase. The room also very small and not comfortable!"

# Wykorzystanie SID do analizy
sid = SentimentIntensityAnalyzer()

sid_positive = sid.polarity_scores(positive_review)
sid_negative = sid.polarity_scores(negative_review)

# print("SID: Positive review:", sid_positive, "Negative review:", sid_negative)
# SID: Positive review: {'neg': 0.0, 'neu': 0.592, 'pos': 0.408, 'compound': 0.9581} Negative review: {'neg': 0.205, 'neu': 0.763, 'pos': 0.031, 'compound': -0.977}

# Wykorzystanie BERT do analizy
classifier = pipeline('sentiment-analysis')
bert_positive = classifier(positive_review)
bert_negative = classifier(negative_review)

print("BERT:", "Positive review:", bert_positive, "Negative review:", bert_negative)
# BERT: Positive review: [{'label': 'POSITIVE', 'score': 0.9998419284820557}] Negative review: [{'label': 'NEGATIVE', 'score': 0.9995495676994324}]
# Wyniki zgodne z oczekiwaniami