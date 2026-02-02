import matplotlib

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Cabin"] = df["Cabin"].fillna(df["Cabin"].mode()[0])
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.drop_duplicates()

print("Diagramme en barres : Taux de survie moyen par classe (Pclass).\n")
taux_survie = df.groupby("Pclass")["Survived"].mean()
plt.figure(figsize=(8, 6))
taux_survie.plot(kind="bar", color="orange")
plt.title("Diagramme en barres")
plt.xlabel("Survived")
plt.ylabel("Survived")
plt.show()



print("Histogramme : Distribution des âges des passagers (avec une courbe KDE).\n")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Age", kde=True, bins=30, hue="Survived", color="purple")
plt.title("Distribution de l'âge des passagers (Titanic)")
plt.xlabel("Âge")
plt.ylabel("Nombre de passagers")
plt.show()





print("Nuage des points \n")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Age", y="Fare", alpha=0.6, color="teal")
plt.title("Relation entre l'Âge et le Tarif du billet (Fare)")
plt.xlabel("Âge des passagers")
plt.ylabel("Tarif du billet (en $)")
plt.show()





print("Heatmap (Carte de chaleur) : Corrélation entre les variables numériques. \n")
colonnes_selectionnees = df[['Survived', 'Pclass', 'Age', 'Fare']]
matrice_corr = colonnes_selectionnees.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(matrice_corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matrice de corrélation (Survie, Classe, Âge, Tarif)")
plt.show()
    