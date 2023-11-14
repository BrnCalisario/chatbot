import pandas as pd
import joblib


access_keywords =  ["acesso", "acessar", "entrar", "logar", "entro", "entrei", "acessado", "acesei", "acessei", "portal"]
reenroll_keywords = ["rematricula", "rematrícula", "rematicula", "matricular"]
find_keywords = ["achar", "achando", "procurei", "procurando", "buscando", "busquei"]
password_keywords = ["senha", "senia", "chave", "senhe", "password", "passe"]
feedback_keywords = ["odiei", "adorei", "bom", "gostei", "fraco", "excelente", "não ajudou", "ruim", "odiei", "lixo"]
payment_keywords = ["pagar", "paguei", "pix", "boleto", "pagamento", "pago", "extrato", "dinheiro", "fatura"]
absence_keywords = ["faltei", "faltas", "presença", "faltando", "faltou"]

keywords_set = {
    "Acess" : access_keywords,
    "Password" : password_keywords,
    "Find" : find_keywords,
    "Reenroll" : reenroll_keywords,
    "Feedback" : feedback_keywords,
    "Payment" : payment_keywords,
    "Absence" : absence_keywords
}

def check_words(word, wordArr):
    return 1 if any(w in word for w in wordArr) else 0

def extract_features(input_df):
    new_df = input_df.copy()

    for key, keyword in keywords_set.items():
        new_df[key] = new_df["Message"].apply(lambda word : check_words(word.lower(), keyword))

    return new_df


def process_message(text):
    my_df = pd.DataFrame(data={ text }, columns=["Message"]) 
    my_df = extract_features(my_df)

    sample = my_df.drop(columns="Message")
 
    loaded_model = joblib.load("trained_model.sav")
    le = joblib.load("label_encoder.sav")

    result = loaded_model.predict(sample)

    result = le.inverse_transform(result)[0]

    return result

