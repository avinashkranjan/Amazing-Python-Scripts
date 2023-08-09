import random
import speech_recognition as sr

vocabulary = {
    'apple': 'a fruit',
    'dog': 'an animal that barks',
    'cat': 'a small domesticated carnivorous mammal',
    'book': 'a written or printed work consisting of pages glued or sewn together along one side',
    'sun': 'the star around which the earth orbits',
    'moon': 'the natural satellite of the earth',
    'tree': 'a woody perennial plant',
    'ocean': 'a large body of salt water',
    'computer': 'an electronic device for storing and processing data',
    'music': 'vocal or instrumental sounds combined to produce beauty of form',
    'happy': 'feeling or showing pleasure or contentment',
    'sad': 'feeling or showing sorrow',
    'water': 'a colorless, transparent, odorless liquid',
    'sky': 'the region of the atmosphere above the earth',
    'mountain': 'a large natural elevation of the earth\'s surface',
    'friend': 'a person whom one knows and with whom one has a bond of mutual affection',
    'love': 'an intense feeling of deep affection',
    'time': 'the indefinite continued progress of existence',
    'work': 'activity involving mental or physical effort done to achieve a purpose',
    'study': 'the devotion of time and attention to acquiring knowledge',
    'write': 'mark (letters, words, or other symbols) on a surface',
    'learn': 'gain or acquire knowledge of or skill in (something) by study, experience, or being taught',
    'laugh': 'make the spontaneous sounds and movements of the face and body that are the instinctive expressions of lively amusement',
    'run': 'move at a speed faster than a walk',
    'eat': 'put (food) into the mouth and chew and swallow it',
    'drink': 'take (a liquid) into the mouth and swallow',
    'jump': 'push oneself off a surface and into the air by using the muscles in one\'s legs and feet',
    'sleep': 'be in a state of rest in which the eyes are closed',
    'happy': 'feeling or showing pleasure or contentment',
    'angry': 'having a strong feeling of or showing annoyance, displeasure, or hostility',
    'beautiful': 'pleasing the senses or mind aesthetically',
    'big': 'of considerable size or extent',
    'small': 'of a size that is less than normal or usual',
    'fast': 'moving or capable of moving at high speed',
    'slow': 'moving or operating at a low speed',
    'hot': 'having a high degree of heat or a high temperature',
    'cold': 'of or at a low or relatively low temperature',
    'old': 'having lived for a long time',
    'new': 'produced, introduced, or discovered recently or now for the first time',
    'happy': 'feeling or showing pleasure or contentment',
    'sad': 'feeling or showing sorrow',
    'flower': 'the seed-bearing part of a plant, consisting of reproductive organs',
    'house': 'a building for human habitation',
    'car': 'a road vehicle, typically with four wheels, powered by an internal combustion engine',
    'bicycle': 'a vehicle with two wheels, powered by pedals',
    'school': 'an institution for educating children',
    'pen': 'a tool for writing or drawing with ink',
    'pencil': 'a writing implement with a graphite or colored core',
    'phone': 'a device used to communicate through sound or speech',
    'television': 'a system for transmitting visual images and sound',
    'watch': 'a small timepiece worn on the wrist',
    'shoe': 'a covering for the foot',
    'shirt': 'a garment worn on the upper part of the body',
    'pants': 'an outer garment covering the body from the waist to the ankles',
    'hat': 'a covering for the head',
    'garden': 'a plot of ground where plants are cultivated',
    'river': 'a large natural stream of water',
    'lake': 'a large body of water surrounded by land',
    'beach': 'a sandy or pebbly shore by the ocean',
    'rain': 'water falling in drops from the atmosphere',
    'snow': 'atmospheric water vapor frozen into ice crystals',
    'cloud': 'a visible mass of condensed water vapor',
    'bird': 'a warm-blooded vertebrate with feathers and beak',
    'fish': 'a limbless cold-blooded vertebrate with gills',
    'insect': 'a small arthropod with six legs and typically wings',
    'computer': 'an electronic device for storing and processing data',
    'table': 'a piece of furniture with a flat top and legs',
    'chair': 'a separate seat for one person',
    'lamp': 'a device for giving light',
    'door': 'a hinged, sliding, or revolving barrier for closing an opening',
    'window': 'an opening in a wall to let in light and air',
    'wall': 'a continuous vertical brick or stone structure',
    'bookcase': 'a piece of furniture with shelves for books',
    'clock': 'a timepiece that shows the time',
    'guitar': 'a musical instrument with strings',
    'piano': 'a large musical instrument with a keyboard',
    'singer': 'a person who sings',
    'artist': 'a person who creates visual or performing arts',
    'chef': 'a professional cook',
    'doctor': 'a person trained in medicine',
    'firefighter': 'a person who extinguishes fires',
    'pilot': 'a person who operates an aircraft',
    'teacher': 'a person who educates others',
    'actor': 'a person who performs in plays or movies',
    'dentist': 'a person who treats teeth and oral health',
    'engineer': 'a person who designs and builds machines or structures',
    'waiter': 'a person who serves food in a restaurant',
    'police': 'a civil force responsible for maintaining law and order',
    'nurse': 'a person trained to care for the sick or infirm',
    'writer': 'a person who writes books, stories, or articles',
    'scientist': 'a person who conducts scientific research',
    'musician': 'a person who plays a musical instrument',
    'photographer': 'a person who takes photographs',
    'baker': 'a person who bakes bread and cakes',
    'painter': 'a person who creates paintings',
    'dancer': 'a person who performs dance',
    'engineer': 'a person who designs and builds machines or structures',
    'architect': 'a person who designs buildings and structures',
    'astronaut': 'a person trained for space travel',
    'athlete': 'a person proficient in sports and other physical exercises',
    'biologist': 'a person who studies living organisms',
    'economist': 'a person who studies economic systems',
    'geologist': 'a person who studies the earth and its history',
    'historian': 'a person who studies and writes about the past',
    'journalist': 'a person who reports news and events',
    'lawyer': 'a person who practices law and represents clients',
    'mathematician': 'a person who studies mathematics',
    'physicist': 'a person who studies the fundamental nature of the universe',
    'psychologist': 'a person who studies the mind and behavior',
    'sociologist': 'a person who studies society and social behavior',
}

grammar_exercise = [
    {
        'question': 'He ___ to the store every day.',
        'answer': 'goes'
    },
    {
        'question': 'They ___ in the park yesterday.',
        'answer': 'played'
    },
    {
        'question': 'She ___ a song beautifully.',
        'answer': 'sings'
    },
    {
        'question': 'I ___ my homework yesterday.',
        'answer': 'did'
    },
    {
        'question': 'We ___ lunch at noon.',
        'answer': 'have'
    },
    {
        'question': 'It ___ raining outside.',
        'answer': 'is'
    },
    {
        'question': 'They ___ going to the party.',
        'answer': 'are'
    },
    {
        'question': 'He ___ reading a book.',
        'answer': 'is'
    },
    {
        'question': 'She ___ her friend tomorrow.',
        'answer': 'will see'
    },
    {
        'question': 'We ___ to the beach last summer.',
        'answer': 'went'
    },
    {
        'question': 'The birds ___ in the sky.',
        'answer': 'fly'
    },
    {
        'question': 'The sun ___ in the east.',
        'answer': 'rises'
    },
    {
        'question': 'I ___ English for two years.',
        'answer': 'have been studying'
    },
    {
        'question': 'He ___ his bike last week.',
        'answer': 'fixed'
    },
    {
        'question': 'She ___ breakfast at 8 AM.',
        'answer': 'eats'
    },
    {
        'question': 'They ___ a movie tonight.',
        'answer': 'will watch'
    },
    {
        'question': 'The baby ___ asleep.',
        'answer': 'is'
    },
    {
        'question': 'We ___ the test yesterday.',
        'answer': 'passed'
    },
    {
        'question': 'I ___ to the radio every morning.',
        'answer': 'listen'
    },
    {
        'question': 'He ___ a letter to his friend.',
        'answer': 'wrote'
    },
    {
        'question': 'She ___ a picture of the sunset.',
        'answer': 'took'
    },
    {
        'question': 'They ___ the cookies yesterday.',
        'answer': 'ate'
    },
    {
        'question': 'I ___ in this city for five years.',
        'answer': 'have lived'
    },
    {
        'question': 'He ___ late for school yesterday.',
        'answer': 'was'
    },
    {
        'question': 'She ___ at the party tonight.',
        'answer': 'will dance'
    },
    {
        'question': 'We ___ a new car next week.',
        'answer': 'are buying'
    },
    {
        'question': 'The sun ___ in the west.',
        'answer': 'sets'
    },
    {
        'question': 'I ___ my keys yesterday.',
        'answer': 'lost'
    },
    {
        'question': 'He ___ his grandmother every Sunday.',
        'answer': 'visits'
    },
    {
        'question': 'She ___ her hair last month.',
        'answer': 'cut'
    },
    {
        'question': 'They ___ a good time at the party.',
        'answer': 'had'
    },
    {
        'question': 'I ___ the book last night.',
        'answer': 'read'
    },
    {
        'question': 'We ___ a lot of pictures on our vacation.',
        'answer': 'took'
    },
    {
        'question': 'He ___ a cup of coffee every morning.',
        'answer': 'drinks'
    },
    {
        'question': 'She ___ for her friend at the airport.',
        'answer': 'is waiting'
    },
    {
        'question': 'They ___ a pizza for dinner tonight.',
        'answer': 'will order'
    },
    {
        'question': 'I ___ with my friends last weekend.',
        'answer': 'played'
    },
    {
        'question': 'We ___ the movie last night.',
        'answer': 'watched'
    },
    {
        'question': 'He ___ in the garden every day.',
        'answer': 'works'
    },
    {
        'question': 'She ___ her sister this evening.',
        'answer': 'will meet'
    },
    {
        'question': 'They ___ to the mountains last summer.',
        'answer': 'went'
    },
    {
        'question': 'I ___ Spanish at school.',
        'answer': 'study'
    },
    {
        'question': 'He ___ his bike to work.',
        'answer': 'rides'
    },
    {
        'question': 'She ___ breakfast at 7 AM.',
        'answer': 'eats'
    },
    {
        'question': 'They ___ a movie last night.',
        'answer': 'watched'
    },
    {
        'question': 'The baby ___ up from a nap.',
        'answer': 'woke'
    },
    {
        'question': 'We ___ the test two days ago.',
        'answer': 'took'
    },
    {
        'question': 'I ___ to music every day.',
        'answer': 'listen'
    },
    {
        'question': 'He ___ a letter to his friend last week.',
        'answer': 'wrote'
    },
    {
        'question': 'She ___ a picture of the sunrise.',
        'answer': 'took'
    },
    {
        'question': 'They ___ the cookies yesterday.',
        'answer': 'ate'
    },
    {
        'question': 'I ___ in this city since 2010.',
        'answer': 'have lived'
    },
    {
        'question': 'He ___ late for school yesterday.',
        'answer': 'was'
    },
    {
        'question': 'She ___ at the party tomorrow.',
        'answer': 'will dance'
    },
    {
        'question': 'We ___ a new car next month.',
        'answer': 'are buying'
    },
    {
        'question': 'The sun ___ in the east.',
        'answer': 'rises'
    },
    {
        'question': 'I ___ my keys yesterday morning.',
        'answer': 'lost'
    },
    {
        'question': 'He ___ his grandmother every week.',
        'answer': 'visits'
    },
    {
        'question': 'She ___ her hair last week.',
        'answer': 'cut'
    },
    {
        'question': 'They ___ a good time at the party.',
        'answer': 'had'
    },
    {
        'question': 'I ___ the book yesterday evening.',
        'answer': 'read'
    },
    {
        'question': 'We ___ a lot of pictures on our vacation.',
        'answer': 'took'
    },
    {
        'question': 'He ___ a cup of coffee every morning.',
        'answer': 'drinks'
    },
    {
        'question': 'She ___ for her friend at the airport.',
        'answer': 'is waiting'
    },
    {
        'question': 'They ___ a pizza for dinner tonight.',
        'answer': 'will order'
    },
    {
        'question': 'I ___ with my friends last Saturday.',
        'answer': 'played'
    },
    {
        'question': 'We ___ the movie last night.',
        'answer': 'watched'
    },
    {
        'question': 'He ___ in the garden every day.',
        'answer': 'works'
    },
    {
        'question': 'She ___ her sister this evening.',
        'answer': 'will meet'
    },
    {
        'question': 'They ___ to the mountains last summer.',
        'answer': 'went'
    },
    {
        'question': 'I ___ Spanish at school.',
        'answer': 'study'
    },
    {
        'question': 'He ___ his bike to work every day.',
        'answer': 'rides'
    },
    {
        'question': 'She ___ breakfast at 7 AM.',
        'answer': 'eats'
    },
    {
        'question': 'They ___ a movie last night.',
        'answer': 'watched'
    },
    {
        'question': 'The baby ___ up from a nap.',
        'answer': 'woke'
    },
    {
        'question': 'We ___ the test two days ago.',
        'answer': 'took'
    },
    {
        'question': 'I ___ to music every day.',
        'answer': 'listen'
    },
    {
        'question': 'He ___ a letter to his friend last week.',
        'answer': 'wrote'
    },
    {
        'question': 'She ___ a picture of the sunrise.',
        'answer': 'took'
    },
    {
        'question': 'They ___ the cookies yesterday.',
        'answer': 'ate'
    },
    {
        'question': 'I ___ in this city since 2010.',
        'answer': 'have lived'
    },
    {
        'question': 'He ___ late for school yesterday.',
        'answer': 'was'
    },
    {
        'question': 'She ___ at the party tomorrow.',
        'answer': 'will dance'
    },
    {
        'question': 'We ___ a new car next month.',
        'answer': 'are buying'
    },
    {
        'question': 'The sun ___ in the east.',
        'answer': 'rises'
    },
    {
        'question': 'I ___ my keys yesterday morning.',
        'answer': 'lost'
    },
    {
        'question': 'He ___ his grandmother every week.',
        'answer': 'visits'
    },
    {
        'question': 'She ___ her hair last week.',
        'answer': 'cut'
    },
    {
        'question': 'They ___ a good time at the party.',
        'answer': 'had'
    },
    {
        'question': 'I ___ the book yesterday evening.',
        'answer': 'read'
    },
    {
        'question': 'We ___ a lot of pictures on our vacation.',
        'answer': 'took'
    },
    {
        'question': 'He ___ a cup of coffee every morning.',
        'answer': 'drinks'
    },
    {
        'question': 'She ___ for her friend at the airport.',
        'answer': 'is waiting'
    },
    {
        'question': 'They ___ a pizza for dinner tonight.',
        'answer': 'will order'
    },
    {
        'question': 'I ___ with my friends last Saturday.',
        'answer': 'played'
    },
    {
        'question': 'We ___ the movie last night.',
        'answer': 'watched'
    },
]

conversations = [
    {
        'question': 'What is your favorite color?',
        'answer': 'My favorite color is blue.'
    },
    {
        'question': 'Do you enjoy learning new things?',
        'answer': 'Yes, I love learning new things and expanding my knowledge.'
    },
    {
        'question': 'What languages can you speak?',
        'answer': 'I can speak English and Spanish fluently.'
    },
    {
        'question': 'Tell me a fun fact!',
        'answer': 'Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!'
    },
    {
        'question': 'What do you like to do in your free time?',
        'answer': 'In my free time, I enjoy reading books and going for long walks.'
    },
    {
        'question': 'What\'s your favorite book or movie?',
        'answer': 'I really love the book "To Kill a Mockingbird" by Harper Lee.'
    },
    {
        'question': 'How do you stay motivated?',
        'answer': 'I stay motivated by setting goals and staying focused on achieving them.'
    },
    {
        'question': 'What are your goals for the future?',
        'answer': 'My goals include traveling to different countries and learning new languages.'
    },
    {
        'question': 'What\'s the most interesting language fact you know?',
        'answer': 'One fascinating fact is that the Inuit language has over 50 different words for "snow"!'
    },
    {
        'question': 'Tell me about an inspiring language learner!',
        'answer': 'Sure! There is a polyglot named Ziad Fazah who holds the Guinness World Record for speaking the most languages. He can speak 59 languages fluently!'
    },
    {
        'question': 'How do you deal with language learning challenges?',
        'answer': 'I overcome language learning challenges by practicing regularly and seeking help from language exchange partners.'
    },
    {
        'question': 'What advice would you give to new language learners?',
        'answer': 'My advice is to be patient with yourself, practice consistently, and immerse yourself in the language as much as possible.'
    },
    {
        'question': 'What\'s the best way to learn vocabulary?',
        'answer': 'Learning vocabulary through context and using flashcards or mnemonic techniques can be very effective.'
    },
    {
        'question': 'Can you recommend any language learning resources?',
        'answer': 'Certainly! There are many great language learning apps and websites like Duolingo, Memrise, and FluentU.'
    },
    {
        'question': 'What are the benefits of being multilingual?',
        'answer': 'Being multilingual opens up opportunities for better communication, cultural understanding, and career prospects.'
    },
    {
        'question': 'How can I improve my pronunciation?',
        'answer': 'Practicing with native speakers, listening to authentic materials, and using pronunciation apps can be helpful.'
    },
    {
        'question': 'What\'s the most challenging language to learn?',
        'answer': 'The difficulty of learning a language varies for each individual, but some consider languages with complex grammar and writing systems, like Mandarin Chinese or Arabic, to be challenging.'
    },
    {
        'question': 'How do you celebrate language learning milestones?',
        'answer': 'I celebrate language learning milestones by treating myself to a nice meal or doing something I enjoy.'
    },
    {
        'question': 'What are some common language learning myths?',
        'answer': 'One common myth is that you need to be naturally talented to learn a language. In reality, dedication and practice are more important.'
    },
    {
        'question': 'What languages are you currently learning?',
        'answer': 'Currently, I am focusing on improving my French and learning German.'
    },
    {
        'question': 'What language learning techniques do you use?',
        'answer': 'I use various techniques, including spaced repetition, interactive quizzes, and language immersion.'
    },
]


def vocabulary_quiz():
    print("AI Language Learning Assistant: Vocabulary Quiz")
    score = 0
    quiz_items = list(vocabulary.keys())
    random.shuffle(quiz_items)

    for word in quiz_items:
        user_answer = input(f"What does '{word}' mean? ")
        if user_answer.strip().lower() == vocabulary[word].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {vocabulary[word]}")

    print(f"Quiz completed! Your score: {score}/{len(vocabulary)}")


def grammar_exercise_quiz():
    print("AI Language Learning Assistant: Grammar Exercise")
    score = 0

    for item in grammar_exercise:
        user_answer = input(item['question'] + " ")
        if user_answer.strip().lower() == item['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {item['answer']}")

    print(
        f"Grammar exercise completed! Your score: {score}/{len(grammar_exercise)}")


def interactive_conversation_practice():
    print("AI Language Learning Assistant: Interactive Conversation Practice")
    print("Type 'exit' to end the conversation.")

    while True:
        conversation = random.choice(conversations)
        user_input = input("ChatBot: " + conversation['question'] + " ")
        if user_input.lower() == 'exit':
            break
        print("ChatBot:", conversation['answer'])


def detect_pronunciation_errors():
    print("AI Language Learning Assistant: Pronunciation Errors Detection")

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak a sentence for pronunciation evaluation:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_sentence = recognizer.recognize_google(audio)

        # Compare user_sentence with a pre-defined correct sentence to detect errors.
        # For simplicity, let's assume a fixed correct sentence.

        correct_sentence = "I love learning languages."
        if user_sentence.strip().lower() == correct_sentence.lower():
            print("Your pronunciation is great!")
        else:
            print("There might be some pronunciation errors. Keep practicing!")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Sorry, there was an error processing the audio. Please try again.")


vocabulary_quiz()
grammar_exercise_quiz()
interactive_conversation_practice()
detect_pronunciation_errors()
