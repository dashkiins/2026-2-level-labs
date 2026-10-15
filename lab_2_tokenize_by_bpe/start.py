"""
BPE Tokenizer starter
"""

# pylint:disable=too-many-locals, unused-variable
import json

from lab_2_tokenize_by_bpe.main import (
    collect_frequencies,
    train,
    get_vocabulary,
    decode
)

def main() -> None:
    """
    Launches an implementation
    """
    with open("lab_2_tokenize_by_bpe/assets/text.txt", "r", encoding="utf-8") as text_file:
        text = text_file.read()
    with open("lab_2_tokenize_by_bpe/assets/en_raw.txt", "r", encoding="utf-8") as text_file:
        text_reference_translation = text_file.read()
    with open("lab_2_tokenize_by_bpe/assets/en_encoded.txt", "r", encoding="utf-8") as text_file:
        translation_encoded_raw = text_file.read()

    frequencies = collect_frequencies(text, None, '</s>')
    print(frequencies)

    trained = train(frequencies, 100)
    print(trained)

    vocabulary = get_vocabulary(trained, "<unk>")
    print(vocabulary)

    with open("lab_2_tokenize_by_bpe/assets/vocab.json", "r", encoding="utf-8") as f:
        big_vocab = json.load(f)

    with open("lab_2_tokenize_by_bpe/assets/secrets/secret_1.txt", "r", encoding="utf-8") as f:
        ids = [int(x) for x in f.read().split()]

    decoded = decode(ids, big_vocab, None)
    decoded = decoded.replace('\u2581', ' ')
    print(decoded)

    result = None
    assert result, "Translation not working"


if __name__ == "__main__":
    main()
