# %%
# Imports

import pandas as pd
import numpy as np 
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

# %%
root_df = pd.read_csv("data.csv")
root_df

# %%
# Defining Key-Words

access_keywords =  ["acesso", "acessar", "entrar", "logar", "entro", "entrei", "acessado", "acesei", "acessei", "portal"]
password_keywords = ["senha", "senia", "chave", "senhe", "password", "passe"]
feedback_keywords = ["odiei", "adorei", "bom", "gostei", "fraco", "excelente", "não ajudou"]
greetings_keywords = ["oi", "olá", "bom dia", "boa tarde", "boa noite", "opa", "eae"]
help_keywords = ["ajuda", "ajudem", "problema", "não consigo"]

# %%
# Extracting features
def check_words(word, wordArr):
    return 1 if any(w in word for w in wordArr) else 0

def extract_features(input_df):
    new_df = input_df.copy()

    new_df["Access"] = new_df["Message"].apply(lambda word : check_words(word.lower(), access_keywords))
    new_df["Password"] = new_df["Message"].apply(lambda word : check_words(word.lower(), password_keywords))
    new_df["Feedback"] = new_df["Message"].apply(lambda word : check_words(word.lower(), feedback_keywords))
    new_df["Greeting"] = new_df["Message"].apply(lambda word : check_words(word.lower(), greetings_keywords))
    new_df["Help"] = new_df["Message"].apply(lambda word : check_words(word.lower(), help_keywords))

    return new_df


df = extract_features(root_df)
df

# %%
# Encode Target

le = LabelEncoder()
df["Target"] = le.fit_transform(df["Target"])

df.head()

# %%
# Training

X = df.drop(columns=["Message", "Target"])
Y = df["Target"]

clf = CategoricalNB(force_alpha=True)

clf.fit(X, Y)

result = clf.predict(X[2:3])

# %%
message = input()
d = { message }

my_df = pd.DataFrame(data=d, columns=["Message"]) 
my_df = extract_features(my_df)

sample = my_df.drop(columns="Message")

result = clf.predict(sample)

print(le.inverse_transform(result)[0])

# %%



