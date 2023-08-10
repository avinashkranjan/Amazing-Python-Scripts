from nltk import ngrams
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

def gen_ngrams(txt, n):
    tokens = word_tokenize(txt)
    ngs = list(ngrams(tokens, n))
    return ngs

def main():
    u = input("Enter a sentence: ")
    n = int(input("Enter the value of n for n-grams: "))
    
    ngs = gen_ngrams(u, n)
    
    print(f"Input Sentence: {u}")
    print(f"{n}-grams: {ngs}")

if __name__ == "__main__":
    main()
