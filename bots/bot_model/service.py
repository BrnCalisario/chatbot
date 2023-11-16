import pandas as pd 
import joblib

response_df = pd.read_csv("./data/responses.csv", sep=";")
model = joblib.load("./models/model.sav")
labelEnconder = joblib.load("./models/encoder.sav")


def random_response(label):
    filtered = response_df[response_df["Intent"] == label]
    return filtered.sample().values[0][0]

def predict(message):
    message = [message]
    
    predict = model.predict(message)

    label = labelEnconder.inverse_transform(predict)[0]

    return label

def give_answer(message):
    label = predict(message)
    answer = random_response(label)
    return answer