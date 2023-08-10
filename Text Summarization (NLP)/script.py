from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.utils import get_stop_words

def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summarizer.stop_words = get_stop_words("english")
    
    summary = summarizer(parser.document, num_sentences)
    return "\n".join([str(sentence) for sentence in summary])

def main():
    text = input("Enter the longer piece of text: ")
    num_sentences = int(input("Enter the number of sentences for summary: "))
    
    summary = summarize_text(text, num_sentences)
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()
