"""
Generation by NGrams starter
"""

# pylint:disable=too-many-locals, unused-import, unused-variable

from lab_3_generate_by_ngrams.main import TextProcessor, NGramLanguageModel

def main() -> None:
    """
    Launches an implementation.

    In any case returns, None is returned
    """
    with open(
        "./lab_3_generate_by_ngrams/assets/Harry_Potter.txt", "r", encoding="utf-8"
    ) as text_file:
        text = text_file.read()

    processor = TextProcessor('_')
    encoded_text = processor.encode(text[:100])
    print(encoded_text)

    if encoded_text is not None:
        decoded_text = processor.decode(encoded_text)
        print(decoded_text)

        result = decoded_text
    else:
        result = None


    encoded_for_model = processor.encode(text)

    if encoded_for_model is not None:
        model = NGramLanguageModel(encoded_for_model, 3)
        is_built = model.build()

        print("Модель:", is_built)
        print("Частотный словарь n-грамм:")
        print(model._n_gram_frequencies)
    else:
        print("Не удалось закодировать текст для модели")

    assert result



if __name__ == "__main__":
    main()
