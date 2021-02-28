from preprocessing import EnglishCorpus

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.utils import get_stop_words
from sumy.summarizers.lex_rank import LexRankSummarizer


def summarize_sentences(sentences: str, language="english") -> list:
    # Preparation sentences
    corpus_maker = EnglishCorpus()
    preprocessed_sentences = corpus_maker.preprocessing(sentences)
    preprocessed_sentence_list = corpus_maker.make_sentence_list(
        preprocessed_sentences)
    corpus = corpus_maker.make_corpus()
    parser = PlaintextParser.from_string(" ".join(corpus), Tokenizer(language))

    # Call the summarization algorithm and do the summarization
    summarizer = LexRankSummarizer()
    summarizer.stop_words = get_stop_words(language)
    summary = summarizer(document=parser.document,
                         sentences_count=len(corpus) * 2 // 10)

    return summary
