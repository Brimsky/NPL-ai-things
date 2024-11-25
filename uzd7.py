import spacy
nlp = spacy.load("en_core_web_md")

def get_embeddings(words):
    return [nlp(w).vector for w in words]


