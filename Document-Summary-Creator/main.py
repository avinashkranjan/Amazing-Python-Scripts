from summary_make import summarize_sentences


def main():
    filepath = input("please input text's filepath->")
    with open(filepath) as f:
        sentences = f.readlines()
    sentences = ' '.join(sentences)

    summary = summarize_sentences(sentences)

    filepath_index = filepath.find('.txt')
    outputpath = filepath[:filepath_index] + '_summary.txt'

    with open(outputpath, 'w') as w:
        for sentence in summary:
            w.write(str(sentence) + '\n')


if __name__ == "__main__":
    main()
