import inflect
from textblob import Word

def main():
    u = input("Enter a word: ")
    
    p = inflect.engine()
    pl = p.plural(u)
    
    s = Word(u).singularize()
    
    print(f"You entered: {u}")
    print(f"Singular form: {s}")
    print(f"Plural form: {pl}")

if __name__ == "__main__":
    main()


