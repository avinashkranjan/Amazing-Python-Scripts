from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')


def get_comp_sup(adjs):
    comp_sup = []

    for adj in adjs:
        synsets = wordnet.synsets(adj)
        if synsets:
            syn = synsets[0]
            comp_forms = [lemma.name().replace('_', ' ')
                          for lemma in syn.lemmas()]
            if len(comp_forms) >= 2:
                comp_form = comp_forms[1]
            else:
                comp_form = adj + "er"
            if len(comp_forms) >= 3:
                superl_form = comp_forms[2]
            else:
                superl_form = adj + "est"
            comp_sup.append((adj, comp_form, superl_form))

    return comp_sup


def main():
    adjs = input("Enter a list of adjectives (comma-separated): ").split(',')

    comp_sup = get_comp_sup(adjs)

    print("\nAdjective\tComparative\tSuperlative")
    print("------------------------------------------")
    for adj, c, s in comp_sup:
        print(f"{adj}\t\t{c}\t\t{s}")


if __name__ == "__main__":
    main()
