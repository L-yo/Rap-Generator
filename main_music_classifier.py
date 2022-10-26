from numpy import vectorize
from source.data_manipulation import songs_organisers, text_cleaning

import numpy as np
import pandas as pd

import nltk
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

from lightpredict import LightClassifier
# nltk.download('punkt')

LYRICS_FOLDER_RAP = "data/Lyrics/Rap"
LYRICS_FOLDER_PARAP = "data/Lyrics/PaRap"

# Columns = ['Artist', 'SongName', 'Lyrics']
df_songs_rap = songs_organisers(LYRICS_FOLDER_RAP)
df_songs_parap = songs_organisers(LYRICS_FOLDER_PARAP)

# Data Cleaning
df_songs_rap["Lyrics"] = df_songs_rap["Lyrics"].apply(text_cleaning)
df_songs_parap["Lyrics"] = df_songs_parap["Lyrics"].apply(text_cleaning)

df_songs_rap["Genre"] = 1
df_songs_parap["Genre"] = 0

df_songs = pd.concat([df_songs_rap, df_songs_parap])

X = df_songs["Lyrics"]
y = df_songs["Genre"]

# Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X).toarray()
y = y.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# lcf = LightClassifier()
# lcf.fit(X_train,X_test,y_train,y_test,rounds=5,plot=True)


# # Nombre de mots totaux
# print(len(vectorizer.get_feature_names_out()))
# print(Lyrics_transformed.shape)
# # print(Lyrics_transformed[0].shape)
# # print(Lyrics_transformed[0])
# # print(Lyrics_transformed[0].toarray())
