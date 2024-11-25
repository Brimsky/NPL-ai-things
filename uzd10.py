from transformers import MarianMTModel, MarianTokenizer

def translate_latvian_to_english(texts):
    tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-lv-en")
    model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-lv-en")
    
    translations = []
    for text in texts:
        encoded = tokenizer(text, return_tensors="pt", padding=True)
        output = model.generate(**encoded)
        translation = tokenizer.decode(output[0], skip_special_tokens=True)
        translations.append(translation)
    
    return translations