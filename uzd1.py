### UZDEVUMS 1: Vārdu biežuma analīze ###
from collections import Counter

def analyze_word_frequency(text):
    text = text.lower()
    words = text.replace('.', '').replace(',', '').replace('?', '').replace('!', '').split()
    return Counter(words)

def test_uzd1():
    text = """Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. 
    Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."""
    frequencies = analyze_word_frequency(text)
    print("\nUZDEVUMS 1 - Vārdu biežuma analīze:")
    for word, count in sorted(frequencies.items()):
        print(f"{word}: {count} reizes")

### UZDEVUMS 2: Teksta valodas noteikšana ###
from langdetect import detect

def detect_language(text):
    try:
        lang = detect(text)
        language_names = {'lv': 'Latviešu', 'en': 'Angļu', 'ru': 'Krievu'}
        return language_names.get(lang, lang)
    except:
        return "Nevarēja noteikt valodu"

def test_uzd2():
    texts = [
        "Šodien ir saulaina diena.",
        "Today is a sunny day.",
        "Сегодня солнечный день."
    ]
    print("\nUZDEVUMS 2 - Valodas noteikšana:")
    for text in texts:
        language = detect_language(text)
        print(f"Teksts: '{text}'\nValoda: {language}\n")

### UZDEVUMS 3: Vārdu sakritību pārbaude ###
def analyze_text_similarity(text1, text2):
    words1 = set(text1.lower().replace('.', '').split())
    words2 = set(text2.lower().replace('.', '').split())
    
    common_words = words1.intersection(words2)
    similarity = len(common_words) / len(words1.union(words2)) * 100
    
    return common_words, similarity

def test_uzd3():
    text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
    text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."
    
    common_words, similarity = analyze_text_similarity(text1, text2)
    print("\nUZDEVUMS 3 - Tekstu sakritība:")
    print(f"Kopīgie vārdi: {', '.join(common_words)}")
    print(f"Sakritības līmenis: {similarity:.2f}%")

### UZDEVUMS 4: Noskaņojuma analīze ###
def analyze_sentiment(text):
    positive_words = {'lielisks', 'apmierināts', 'prieks', 'labs', 'patīk'}
    negative_words = {'vīlies', 'slikts', 'nepatīk', 'neatbilst'}
    
    words = text.lower().split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    
    if pos_count > neg_count:
        return "pozitīvs"
    elif neg_count > pos_count:
        return "negatīvs"
    return "neitrāls"

def test_uzd4():
    sentences = [
        "Šis produkts ir lielisks, esmu ļoti apmierināts!",
        "Esmu vīlies, produkts neatbilst aprakstam.",
        "Neitrāls produkts, nekas īpašs."
    ]
    print("\nUZDEVUMS 4 - Noskaņojuma analīze:")
    for sentence in sentences:
        sentiment = analyze_sentiment(sentence)
        print(f"Teikums: '{sentence}'\nNoskaņojums: {sentiment}\n")

### UZDEVUMS 5: Teksta tīrīšana ###
import re

def clean_text(text):
    # Remove mentions, URLs, and emojis
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^\w\s.,!?]', '', text)
    text = text.lower().strip()
    return text

def test_uzd5():
    text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
    cleaned = clean_text(text)
    print("\nUZDEVUMS 5 - Teksta tīrīšana:")
    print(f"Original: {text}")
    print(f"Cleaned: {cleaned}")

### UZDEVUMS 6: Automātiska rezumēšana ###
def summarize_text(text):
    sentences = text.split('.')
    important_words = ['galvaspilsēta', 'slavena', 'robežojas', 'valsts']
    
    # Score sentences based on important words
    scored_sentences = []
    for sentence in sentences:
        score = sum(1 for word in sentence.lower().split() if word in important_words)
        if score > 0:
            scored_sentences.append(sentence.strip())
    
    return '. '.join(scored_sentences) + '.'

def test_uzd6():
    text = """Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."""
    summary = summarize_text(text)
    print("\nUZDEVUMS 6 - Teksta rezumēšana:")
    print(f"Kopsavilkums: {summary}")

### UZDEVUMS 7: Vārdu iegulšana ###
from gensim.models import Word2Vec
import numpy as np

def create_word_embeddings(words):
    # Create a simple context for our words
    contexts = [
        ['māja', 'liela', 'dzīvoklis'],
        ['dzīvoklis', 'mazs', 'māja'],
        ['jūra', 'dziļa', 'ūdens']
    ]
    
    model = Word2Vec(contexts, min_count=1, vector_size=10)
    
    results = {}
    for word in words:
        if word in model.wv:
            results[word] = model.wv[word]
    return results

def test_uzd7():
    words = ['māja', 'dzīvoklis', 'jūra']
    embeddings = create_word_embeddings(words)
    print("\nUZDEVUMS 7 - Vārdu iegulšana:")
    for word, vector in embeddings.items():
        print(f"{word}: {vector[:3]}...")  # Show first 3 dimensions

### UZDEVUMS 8: Frāžu atpazīšana ###
def identify_entities(text):
    # Simple rule-based NER
    organizations = []
    persons = []
    
    words = text.split()
    for i in range(len(words)):
        if words[i][0].isupper():
            if i > 0 and words[i-1] in ['Valsts', 'prezidents']:
                persons.append(' '.join(words[i-1:i+1]))
            elif 'Universitāte' in words[i:i+2]:
                organizations.append(' '.join(words[i:i+2]))
    
    return persons, organizations

def test_uzd8():
    text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."
    persons, organizations = identify_entities(text)
    print("\nUZDEVUMS 8 - Frāžu atpazīšana:")
    print(f"Personas: {persons}")
    print(f"Organizācijas: {organizations}")

### UZDEVUMS 9: Teksta ģenerēšana ###
import random

def generate_story(start_phrase):
    templates = [
        "Tur dzīvoja {} {}, kas {}.",
        "Katru dienu {} {}, līdz {}.",
        "Beigās {} un {}."
    ]
    
    subjects = ['princese', 'bruņinieks', 'pūķis', 'burvis']
    actions = ['devās ceļojumā', 'meklēja dārgumus', 'cīnījās ar ļaunumu']
    endings = ['atrada laimi', 'kļuva par varoni', 'atgriezās mājās']
    
    story = [start_phrase]
    for template in templates:
        sentence = template.format(
            random.choice(subjects),
            random.choice(actions),
            random.choice(endings)
        )
        story.append(sentence)
    
    return ' '.join(story)

def test_uzd9():
    start = "Reiz kādā tālā zemē..."
    story = generate_story(start)
    print("\nUZDEVUMS 9 - Teksta ģenerēšana:")
    print(story)

### UZDEVUMS 10: Tulkošana ###
def translate_to_english(text):
    translations = {
        'Labdien': 'Hello',
        'kā': 'how',
        'jums': 'you',
        'klājas': 'are doing',
        'Es': 'I',
        'šodien': 'today',
        'lasīju': 'read',
        'interesantu': 'interesting',
        'grāmatu': 'book'
    }
    
    words = text.split()
    translated_words = [translations.get(word, word) for word in words]
    return ' '.join(translated_words)

def test_uzd10():
    texts = [
        "Labdien! Kā jums klājas?",
        "Es šodien lasīju interesantu grāmatu."
    ]
    print("\nUZDEVUMS 10 - Tulkošana:")
    for text in texts:
        translated = translate_to_english(text)
        print(f"Oriģināls: {text}")
        print(f"Tulkojums: {translated}\n")

if __name__ == "__main__":
    # Run all tests
    test_uzd1()
    test_uzd2()
    test_uzd3()
    test_uzd4()
    test_uzd5()
    test_uzd6()
    test_uzd7()
    test_uzd8()
    test_uzd9()
    test_uzd10()