# Zadanie wygenerowane przez ChatGPT
# Prompt: wykonaj zadanie 3 z załączonego pliku
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 📌 1. Wczytanie danych z pliku CSV
df = pd.read_csv("./lab02/iris1.csv")

# 📌 2. Pobranie dwóch cech: sepal length i sepal width
X_original = df.iloc[:, [0, 1]]  # Pierwsza i druga kolumna (sepal length, sepal width)
species = df.iloc[:, -1]  # Ostatnia kolumna - etykiety

# 📌 3. Normalizacja Min-Max
min_max_scaler = MinMaxScaler()
X_minmax = min_max_scaler.fit_transform(X_original)

# 📌 4. Standaryzacja (Z-score)
zscore_scaler = StandardScaler()
X_zscore = zscore_scaler.fit_transform(X_original)

# 📌 5. Definiowanie kolorów dla gatunków
species_colors = {"Setosa": "red", "Versicolor": "green", "Virginica": "blue"}
colors = species.map(species_colors)

# 📌 6. Tworzenie wykresów
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Wykres oryginalnych danych
axes[0].scatter(X_original.iloc[:, 0], X_original.iloc[:, 1], c=colors, alpha=0.7, edgecolors="k")
axes[0].set_title("Oryginalne dane")
axes[0].set_xlabel("Sepal Length")
axes[0].set_ylabel("Sepal Width")

# Wykres po normalizacji Min-Max
axes[1].scatter(X_minmax[:, 0], X_minmax[:, 1], c=colors, alpha=0.7, edgecolors="k")
axes[1].set_title("Normalizacja Min-Max")
axes[1].set_xlabel("Sepal Length (Min-Max)")
axes[1].set_ylabel("Sepal Width (Min-Max)")

# Wykres po standaryzacji Z-score
axes[2].scatter(X_zscore[:, 0], X_zscore[:, 1], c=colors, alpha=0.7, edgecolors="k")
axes[2].set_title("Standaryzacja (Z-score)")
axes[2].set_xlabel("Sepal Length (Z-score)")
axes[2].set_ylabel("Sepal Width (Z-score)")

# Wyświetlenie wykresów
plt.show()

"""
Odpowiedzi wygenerowane przez ChatGPT:

Normalizacja Min-Max skaluje dane tak, aby wartości mieściły się między 0 a 1, ale zachowuje proporcje.
Standaryzacja (Z-score) zmienia rozkład danych tak, aby miały średnią 0 i odchylenie standardowe 1, 
co może poprawić działanie algorytmów ML.
Wizualnie dane mogą się rozciągnąć lub przesunąć, ale relacje między punktami pozostają.
"""