from polyglot.detect import Detector

text = [
    u"""Šis produkts ir lielisks, esmu ļoti apmierināts!"""
    ,u"""Esmu vīlies, produkts neatbilst aprakstam.""",
    u"""Neitrāls produkts, nekas īpašs."""
]
for texts in text:
    detector = Detector(texts)
    print(detector.language)