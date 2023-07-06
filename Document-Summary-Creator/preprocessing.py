import spacy
import neologdn


class EnglishCorpus:
    # Preparation of morphological analyzer
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    # Pre-processing of line breaks and special characters
    def preprocessing(self, text: str) -> str:
        text = text.replace("\n", "")
        text = neologdn.normalize(text)

        return text

    # Divide sentences into sentences while retaining the results of morphological analysis
    def make_sentence_list(self, sentences: str) -> list:
        doc = self.nlp(sentences)
        self.ginza_sents_object = doc.sents
        sentence_list = [s for s in doc.sents]

        return sentence_list

    # Put a space between words
    def make_corpus(self) -> list:
        corpus = []
        for s in self.ginza_sents_object:
            tokens = [str(t) for t in s]
            corpus.append(" ".join(tokens))

        return corpus
