# Read text captions
from keras.layers import Dense, Dropout, Embedding, LSTM
from keras.utils import load_img, img_to_array
from tf.keras.applications.resnet50 import ResNet50, preprocess_input
from keras.layers import Input
import collections
from keras.layers.merging import add
from keras.utils import to_categorical
from tf.keras.preprocessing.sequence import pad_sequences
from keras.models import Model
from keras.preprocessing import image
import tensorflow as tf
import re
import keras
import matplotlib.pyplot as plt
import numpy as np


def readTextFile(path):
    with open(path) as f:
        captions = f.read()
    return captions


# Location of captions
captions = readTextFile('files/captions.txt')
captions = captions.split("\n")[1:-1]
print(len(captions))  # Total captions

# Creating dictionary - {"image name": ["caption1","caption2"...]}
description = {}
for x in captions:
    parts = x.split(',')
    img_name = parts[0][:-4]
    coment = parts[1]
    if description.get(img_name) is None:
        description[img_name] = []
    description[img_name].append(coment)

# All libraries

# Data cleaning
# Don't remove stopwords because we need to make meaningful words. Also stemming will also not applicable because we require texts has correct vocabulary
# Remove numbers, lower() , punctuations remove


def clean_text(sentence):
    sentence = sentence.lower()
    sentence = re.sub("[^a-z]+", " ", sentence)
    sentence = sentence.split()

    sentence = [s for s in sentence if len(s) > 1]
    sentence = " ".join(sentence)
    return sentence


# clean all captions
for key, caption_list in description.items():
    for i in range(len(caption_list)):
        caption_list[i] = clean_text(caption_list[i])

# Total number of words across all the sentences
total_words = []
for key in description.keys():
    [total_words.append(i) for des in description[key] for i in des.split()]
print(len(total_words))

# Filter words from the vocab according to the certain threshold frequency
counter = collections.Counter(total_words)
freq_cnt = dict(counter)

# Sort this dictionary according to freq count
sorted_freq_cnt = sorted(freq_cnt.items(), reverse=True, key=lambda x: x[1])

# Filtering
threshold = 5
sorted_freq_cnt = [x for x in sorted_freq_cnt if x[1] > threshold]
total_words = [x[0] for x in sorted_freq_cnt]

# Prepare train/test data
train_filedata = readTextFile("files/Flickr_8k.trainImages.txt")
test_filedata = readTextFile("files/Flickr_8k.testImages.txt")

train = [row.split(".")[0] for row in train_filedata.split("\n")[:-1]]
test = [row.split(".")[0] for row in test_filedata.split("\n")[:-1]]

# Prepare description for the training data
# Tweak - add <S> and <e> token to our training data
train_description = {}
for img_id in train:
    train_description[img_id] = []
    for cap in description[img_id]:
        cap_to_append = "startseq " + cap + " endseq"
        train_description[img_id].append(cap_to_append)


# Transfer learning
# Step 1. Image feature extraction
# Using pretrained ResNet50 model for extracting preprocessing images
model = ResNet50(weights='imagenet', input_shape=(224, 224, 3))
model.summary()

# Removing last 2 layers of ResNet50 model
new_model = Model(model.input, model.layers[-2].output)
new_model.summary()


def preprocess_img(img):
    img = load_img(img, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    # normalisation -> preprocess_input
    img = preprocess_input(img)
    return img


def encode_image(img):
    img = preprocess_img(img)
    feature_vector = new_model.predict(img, verbose=0)
    # print(feature_vector.shape)
    feature_vector = feature_vector.reshape((-1,))
    return feature_vector


# encode all train images
encoding_train = {}
# image_id --> feature vector extrcted from resnet
for ix, img_id in enumerate(train):
    img_path = "files/Images/"+img_id+".jpg"
    encoding_train[img_id] = encode_image(img_path)
    # if ix%100==0:
    #     print(ix)

# encode all test images
encoding_test = {}
# image_id --> feature vector extrcted from resnet
for ix, img_id in enumerate(test):
    img_path = "files/Images/"+img_id+".jpg"
    encoding_test[img_id] = encode_image(img_path)
    # if ix%100==0:
    #     print(ix)


word_to_idx = {}
idx_to_word = {}
for i, word in enumerate(total_words):
    word_to_idx[word] = i+1
    idx_to_word[i+1] = word
word_to_idx['startseq'] = 2573
word_to_idx['endseq'] = 2574
idx_to_word[2573] = 'startseq'
idx_to_word[2574] = 'endseq'

# Model training
# RNN model ->
# Find max length of any caption to decide RNN model size
max_len = 0
for key in train_description.keys():
    for cap in train_description[key]:
        max_len = max(max_len, len(cap.split()))  # Max length of any caption

# Data Loader(generator)


def data_generator(train_description, encoding_train, word_to_idx, max_len, batch_size, vocab_size=2574):
    x1, x2, y = [], [], []
    n = 0

    while True:
        for key, desc_list in train_description.items():
            n += 1
            photo = encoding_train[key]
            for desc in desc_list:
                seq = [word_to_idx[word]
                       for word in desc.split() if word in word_to_idx.keys()]
                for i in range(1, len(seq)):
                    xi = seq[0:i]
                    yi = seq[i]

                    xi = pad_sequences([xi], maxlen=max_len,
                                       value=0, padding='post')[0]
                    yi = to_categorical([yi-1], num_classes=vocab_size)[0]
                    x1.append(photo)  # 2048
                    x2.append(xi)     # 35 -> glove
                    y.append(yi)      # vocab_size->2574

            if n == batch_size:
                yield [[np.array(x1), np.array(x2)], np.array(y)]
                x1, x2, y = [], [], []
                n = 0


# WORD EMBEDDINGS
# The text data should be embedded before passing to RNN/LSTM layer
f = open("files/glove.6B.50d.txt", encoding='utf8')
embedding_index = {}

for line in f:
    values = line.split()
    word = values[0]
    word_embedding = np.array(values[1:], dtype='float')
    embedding_index[word] = word_embedding


def get_embedding_matrix(vocab_size=2574):
    emb_dim = 50
    matrix = np.zeros((vocab_size, emb_dim))
    for word, idx in word_to_idx.items():
        embedding_vector = embedding_index.get(word)
        if embedding_vector is not None:
            matrix[idx] = embedding_vector
    return matrix


embedding_matrix = get_embedding_matrix()

vocab_size = 2574
input_img_features = Input(shape=(2048,))
input_img1 = Dropout(0.3)(input_img_features)
input_img2 = Dense(256, activation="relu")(input_img1)

# Captions as input => batch_size*35 -> batch_size*35*50 -> 256
input_captions = Input(shape=(max_len,))
# Now here we use customize embedding and not the glove vector embedding yet
input_cap1 = Embedding(input_dim=vocab_size, output_dim=50,
                       mask_zero=True)(input_captions)
input_cap2 = Dropout(0.3)(input_cap1)
input_cap3 = LSTM(256)(input_cap2)

# Add inputs and decode them
decoder1 = add([input_img2, input_cap3])
decoder2 = Dense(256, activation='relu')(decoder1)
outputs = Dense(vocab_size, activation='softmax')(decoder2)

# COMBINED MODEL
model = Model(inputs=[input_img_features, input_captions], outputs=outputs)

# Important thing -- Embedding layer # Here we defined the matrix to be choose for the words with integers
model.layers[2].set_weights([embedding_matrix])
model.layers[2].trainable = False
model.compile(loss="categorical_crossentropy", optimizer="adam")

print(model.summary())

# Training of Model
epochs = 10
batch_size = 3  # no if images per batch
steps = len(train_description)//batch_size


def train():
    for i in range(epochs):
        generator = data_generator(
            train_description, encoding_train, word_to_idx, max_len, batch_size)
        model.fit(generator, epochs=1, steps_per_epoch=steps, verbose=1)


model.save("models/"+"9"+'.h5')

train()

# Prediction Function


def predict_caption(photo):
    in_text = "startseq"
    for i in range(max_len):
        sequence = [word_to_idx[w]
                    for w in in_text.split() if w in word_to_idx]
        sequence = pad_sequences([sequence], maxlen=max_len, padding='post')
        ypred = model.predict([photo, sequence])
        ypred = ypred.argmax()  # word with max probability -> greedy sampling
        word = idx_to_word[ypred+1]
        in_text += (' ' + word)
        if word == 'endseq':
            break
    final_caption = in_text.split()[1:-1]
    final_caption = ' '.join(final_caption)
    return final_caption


# Pick some random images
for i in range(15):
    no = np.random.randint(0, 1000)
    all_img_names = list(encoding_test.keys())
    img_name = all_img_names[no]
    photo_2048 = encoding_test[img_name].reshape((1, 2048))

    caption = predict_caption(photo_2048)

    i = plt.imread("files/Images/"+img_name+".jpg")
    print(caption)
    plt.imshow(i)
    plt.axis("off")
    plt.show()
