import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer

# Latvian teikumu tokenizācija ar SpaCy
class SpaCyTokenizer:
    def __init__(self):
        self.nlp = spacy.blank("lv")  # Latvian modelis

    def to_sentences(self, text):
        doc = self.nlp(text)
        return [sent.text for sent in doc.sents]

def automatic_summary(text, sentence_count=2):
    tokenizer = SpaCyTokenizer()
    parser = PlaintextParser.from_string(text, tokenizer)
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

text = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām.
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai.
Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

summary = automatic_summary(text)
print("Rezumējums:", summary)
