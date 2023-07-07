import string
from collections import Counter


class model(object):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_sentimental_analysis(text):
        # reading text file
        # converting to lowercase
        lower_case = text.lower()

        # Removing punctuations
        cleaned_text = lower_case.translate(
            str.maketrans('', '', string.punctuation))

        # splitting text into words
        tokenized_words = cleaned_text.split()

        stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                      "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
                      "itself",
                      "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                      "these",
                      "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
                      "do",
                      "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
                      "while",
                      "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during",
                      "before",
                      "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                      "again",
                      "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
                      "each",
                      "few", "more", "most", "other", "some", "such", "no", "nor", "only", "own", "same", "so",
                      "than",
                      "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

        # Removing stop words from the tokenized words list
        final_words = []
        for word in tokenized_words:
            if word not in stop_words:
                final_words.append(word)

        emotion_list = []
        with open('./Text_Sentimental_Analysis_Script_with_GUI/textFiles/emotions.txt', 'r') as file:
            for line in file:
                clear_line = line.replace("\n", '').replace(
                    ",", '').replace("'", '').strip()
                word, emotion = clear_line.split(':')

                if word in final_words:
                    emotion_list.append(emotion)

        if emotion_list is None or len(emotion_list) == 0:
            final_emotion = "Sorry the entered text was not enough for making a Sentiment Analysis please try again "
        else:
            final_emotion = "Your Sentimental Analysis says that your emotion is" + max(Counter(emotion_list),
                                                                                        key=Counter(emotion_list).get)
        return final_emotion
