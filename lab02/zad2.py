import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#Kompresja bazy danych do 2 kolumn
df = pd.read_csv("./lab02/iris1.csv")

X = df.iloc[:, :-1]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

df_pca = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_pca["species"] = df.iloc[:, -1] 

print(df_pca)
print("Explained variance ratio:", pca.explained_variance_ratio_)

#Wykres
plt.figure(figsize=(10, 6))

species = df_pca['species'].unique()
colors = ['red', 'green', 'blue']

for species_name, color in zip(species, colors):
    mask = df_pca['species'] == species_name
    plt.scatter(df_pca.loc[mask, 'PC1'], 
               df_pca.loc[mask, 'PC2'],
               c=color,
               label=species_name)

plt.xlabel('Pierwsza składowa główna (PC1)')
plt.ylabel('Druga składowa główna (PC2)')
plt.title('Analiza składowych głównych (PCA) dla zbioru Iris')
plt.legend()
plt.grid(True)
plt.show()