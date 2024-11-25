import spacy

def analyze_entities(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(f"{ent.text} - {ent.label_}")