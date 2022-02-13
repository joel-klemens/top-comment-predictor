import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils


# load ascii text and covert to lowercase
filename = "../gather-data/data/funny.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()

# create mapping of unique chars to integers, and a reverse mapping
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

# summarize the dataset
n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)

# Each training pattern of the network is comprised of 100 time steps of one character (X)
# followed by one character output (y). When creating these sequences, we slide this window
# along the whole book one character at a time, allowing each character a chance to be
# learned from the 100 characters that preceded it (except the first 100 characters of course).

# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)

# Finally, we need to convert the output patterns (single characters converted to integers)
#  into a one hot encoding. This is so that we can configure the network to predict the
# probability of each of the 47 different characters in the vocabulary (an easier representation)
# rather than trying to force it to predict precisely the next character. Each y value is
# converted into a sparse vector with a length of 47, full of zeros except with a 1 in the
#  column for the letter (integer) that the pattern represents.

# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
X = X / float(n_vocab)
# one hot encode the output variable
y = np_utils.to_categorical(dataY)
# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(
    X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# The network is slow to train (about 55 seconds per epoch on an Nvidia RTX 2070 super). Because of the slowness
# and because of our optimization requirements, we will use model checkpointing to record all of the
#  network weights to file each time an improvement in loss is observed at the end of the epoch.
# We will use the best set of weights (lowest loss) to instantiate our generative model in the next section.

# define the checkpoint
filepath = "weights/weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
checkpoint = ModelCheckpoint(
    filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
# fit the model
model.fit(X, y, epochs=100, batch_size=128, callbacks=callbacks_list)
