from lab_3_generate_by_ngrams.main import TextProcessor

text = "Text Generation is the task of generating text with the goal of appearing indistinguishable to human-written text."
processor = TextProcessor("_")
encoded = processor.encode(text)

print("Длина закодированного текста:", len(encoded))
print("Последние 5 элементов:", encoded[-5:])