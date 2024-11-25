import stanza


nlp = stanza.Pipeline('lv')


text = [
    "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu.",
    "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."
    ]
for texts in text:
    doc = nlp(texts)
    for sentence in doc.sentences:
        for word in sentence.words:
            print(f"Word: {word.text}")
            print(f"Head (relation): {word.head} ({word.deprel})")
            print("-" * 20)




#"nsubj": "Nominal Subject",
#"obj": "Object",
#"iobj": "Indirect Object",
#"amod": "Adjectival Modifier",
#"advmod": "Adverbial Modifier",
#"nmod": "Nominal Modifier",
#"case": "Case Marking",
#"obl": "Oblique Nominal",
#"xcomp": "Open Clausal Complement",
#"ccomp": "Clausal Complement",
#"cop": "Copula",
#"det": "Determiner",
#"conj": "Conjunct",
#"cc": "Coordinating Conjunction",
#"root": "Root",
#"mark": "Marker",
#"aux": "Auxiliary",
#"acl": "Adnominal Clause",
#"punct": "Punctuation",
#"appos": "Appositional Modifier"