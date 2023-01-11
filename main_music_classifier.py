from numpy import vectorize
from source.data_manipulation import songs_organisers, text_cleaning, is_french_lyric

import numpy as np
import pandas as pd

import nltk
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.model_selection import train_test_split

# Models import
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

# Metrics import
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# nltk.download('punkt')

LYRICS_FOLDER_RAP = "data/Lyrics/Rap"
LYRICS_FOLDER_PARAP = "data/Lyrics/PaRap"

# Columns = ['Artist', 'SongName', 'Lyrics']
df_songs_rap = songs_organisers(LYRICS_FOLDER_RAP)
df_songs_parap = songs_organisers(LYRICS_FOLDER_PARAP)

# Data Cleaning
df_songs_rap["Lyrics"] = df_songs_rap["Lyrics"].apply(text_cleaning)
df_songs_parap["Lyrics"] = df_songs_parap["Lyrics"].apply(text_cleaning)
df_songs_rap = df_songs_rap.loc[df_songs_rap["Lyrics"].apply(is_french_lyric) ]

df_songs_rap["Genre"] = 1
df_songs_parap["Genre"] = 0

df_songs = pd.concat([df_songs_rap, df_songs_parap])

X = df_songs["Lyrics"]
y = df_songs["Genre"]

# Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X).toarray()
y = y.to_numpy()

# Train Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# print(y_train)

# Test diverse classifier
classifiers = {
    "KNeighborsClassifier" : KNeighborsClassifier(),
    "GaussianNB" : GaussianNB(),
    #"MLPClassifier" : MLPClassifier(),
    "SVC" : SVC(),
    "LinearSVC" : LinearSVC(),
    "GaussianProcessClassifier" : GaussianProcessClassifier(),
    "DecisionTreeClassifier" : DecisionTreeClassifier(),
    "RandomForestClassifier" : RandomForestClassifier(),
    "AdaBoostClassifier" : AdaBoostClassifier()
}

for classifier_name in classifiers:
    print("=== {}".format(classifier_name))

    clf = classifiers[classifier_name]
    
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    accuracy_score_clf = accuracy_score(y_test, y_pred)
    f1_score_clf = f1_score(y_test, y_pred)
    precision_score_clf = precision_score(y_test, y_pred)
    recall_score_clf = recall_score(y_test, y_pred)
    
    print("accuracy : {}".format(accuracy_score_clf))
    print("precision : {}".format(precision_score_clf))
    print("recall : {}".format(recall_score_clf))
    print("f1_score : {}".format(f1_score_clf))
    print("============================")

# Grid Search

# # Nombre de mots totaux
# print(len(vectorizer.get_feature_names_out()))
# print(Lyrics_transformed.shape)
# # print(Lyrics_transformed[0].shape)
# # print(Lyrics_transformed[0])
# # print(Lyrics_transformed[0].toarray())
