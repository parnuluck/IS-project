import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from utils.preprocess import clean_text

# load
df = pd.read_csv("data/imdb.csv")

# clean
df["review"] = df["review"].apply(clean_text)

# label
df["sentiment"] = df["sentiment"].map({"positive":1, "negative":0})

# vectorize
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["review"]).toarray()
y = df["sentiment"]

# model
model = Sequential([
    Dense(128, activation='relu', input_shape=(5000,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=5)

# save
model.save("nn_model.h5")

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
