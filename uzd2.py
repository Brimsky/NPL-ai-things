from langdetect import detect


list  = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
    ]

for words in list:
    print(detect(words))
