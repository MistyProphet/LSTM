from __future__ import print_function
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.datasets.data_utils import get_file
from keras.preprocessing.sequence import pad_sequences
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import random
import sys
import os, urllib, csv, itertools, operator, nltk, re
import cPickle as pkl

# saving the argument
if (len(sys.argv) > 1):
	arg1 = str(sys.argv[1])
else:
	arg1 = ""

# read the movie links from file
with open("movieList.txt") as f:
    content = f.readlines()

# prepare train data
docList = list()
chars = set()
maxlen = 0
tempMaxlen = 0

plots = []
if os.path.exists('plots.pkl'):
    with open('plots.pkl', 'r+') as f:
        plots = pkl.load(f)

plots_loaded = len(plots) > 0
content = plots if plots_loaded else content
text = ''
for idx, url in enumerate(content):
    if plots_loaded:
        tempHtml = plots[idx]
        # text += ' %%start%% ' + plots[idx] + ' %%end%% '
        text += ' ' + plots[idx] + ' %end% '
        continue
    else:
        print('Downloading URL {0}/{1}: {2}'.format(idx + 1, len(content), url))
        fhtml = urllib.urlopen(url)
        tempHtml = fhtml.read()
        if '==Plot==' not in tempHtml or '==Cast==' not in tempHtml:
            continue
        tempHtml = tempHtml.split('==Plot==')[1]
        tempHtml = tempHtml.split('==Cast==')[0]
        tempHtml = tempHtml.replace('\n', '')
        tempHtml = tempHtml.lower()
        plots.append(tempHtml)
    words = list()
    for line in tempHtml:
        for charX in line:
            words.append(charX)
            chars.add(charX)
            tempMaxlen += 1
    if tempMaxlen > maxlen:
        maxlen = tempMaxlen
    tempMaxlen = 0
    docList.append(words)
#######################################

if not plots_loaded:
    with open('plots.pkl', 'w+') as f:
        pkl.dump(plots, f)

print(len(text))
chars = set(text)
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

print("Broj stranica: %d" % len(docList))
print("Maxlen: %d" % maxlen)

# cut the text in semi-redundant sequences of maxlen characters
maxlen = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('nb sequences:', len(sentences))

print('Vectorization...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1
#######################################

# build the model: 2 stacked LSTM
print('Build model...')
model = Sequential()
model.add(LSTM(512, return_sequences=True, input_shape=(maxlen, len(chars))))
model.add(Dropout(0.2))
model.add(LSTM(512, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='rmsprop')


def sample(a, temperature=1.0):
    # helper function to sample an index from a probability array
    a = np.log(a) / temperature
    a = np.exp(a) / np.sum(np.exp(a))
    return np.argmax(np.random.multinomial(1, a, 1))


def datagen(X, y, batch_size):
    n = X.shape[0]
    it = 0
    while 1:
        it += 1
        if it > n:
            it = 0
        yield X[it*batch_size:(it+1)*batch_size], y[it*batch_size:(it+1)*batch_size]

# train the model, output generated text after each iteration
for iteration in range(1, 200):
    print()
    print('-' * 50)
    print('Iteration', iteration)
    mc = ModelCheckpoint(filepath='char_lstm.hdf5', monitor='loss', save_best_only=True)
    model.fit(X, y, batch_size=128, nb_epoch=5, verbose=1, callbacks=[mc])
	
    start_index = random.randint(0, len(text) - maxlen - 1)

    ###########################################
    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print()
        print('----- diversity:', diversity)

        generated = ''
        if (arg1 == ""):
		    sentence = text[start_index: start_index + maxlen]
        else:
            sentence = arg1
        generated += sentence
        print('----- Generating with seed: "' + sentence + '"')

        for i in range(800):
            x = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.

            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]

            generated += next_char
            sentence = sentence[1:] + next_char

            if '%end%' in generated:
                break
        print(generated)
    ###########################################