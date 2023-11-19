import numpy as np

# Step 1: Preprocess the text data

data = "Quick brown fox jumped over the lazy dog"
# Tokenize the data into words
tokenzed_data = data.split()
print(tokenzed_data)

# Count the word frequencies
word_freq = {}
for word in tokenzed_data:
    word_freq[word] = word_freq.get(word, 0) + 1
print(word_freq)

# Get vocabulary size
vocab = set(tokenzed_data)
vocab_size = len(vocab)
print(vocab_size)

# Generate indexed data
word2index = {}
for i, word in enumerate(vocab):
    word2index[word] = i
print(word2index)

# Generate one-hot encoded data
one_hot_encoded_data = []
for word in tokenzed_data:
    one_hot_encoded_row = np.zeros(vocab_size)
    one_hot_encoded_row[word2index[word]] = 1
    one_hot_encoded_data.append(one_hot_encoded_row)
one_hot_encoded_data = np.asarray(one_hot_encoded_data)
print(one_hot_encoded_data)

# Generate context words
context_size = 2
for i in range(2, len(tokenzed_data) - 2):
    context_words = [tokenzed_data[i - 2], tokenzed_data[i - 1],
                     tokenzed_data[i + 1], tokenzed_data[i + 2]]
    target_word = tokenzed_data[i]
    print("Context words = {}, Target word = {}".format(context_words, target_word))

# Generate training data
X_train = []  # input word
y_train = []  # output word
for i in range(2, len(tokenzed_data) - 2):
    context_words = [tokenzed_data[i - 2], tokenzed_data[i - 1],
                     tokenzed_data[i + 1], tokenzed_data[i + 2]]
    target_word = tokenzed_data[i]
    for w in context_words:
        X_train.append(one_hot_encoded_data[word2index[w]])
        y_train.append(one_hot_encoded_data[word2index[target_word]])
X_train = np.asarray(X_train)
y_train = np.asarray(y_train)
print("X_train shape = {}".format(X_train.shape))
print(X_train)
print("y_train shape = {}".format(y_train.shape))
print(y_train)

# initialize the model parameters
hidden_size = 5
W1 = np.random.uniform(-1.0, 1.0, (vocab_size, hidden_size))
W2 = np.random.uniform(-1.0, 1.0, (hidden_size, vocab_size))
print("W1 shape = {}".format(W1.shape))
print(W1)
print("W2 shape = {}".format(W2.shape))
print(W2)

# train the model
learning_rate = 0.1
for i in range(10000):
    # forward pass
    hidden_layer = np.dot(X_train, W1)
    output_layer = np.dot(hidden_layer, W2)

    # backward pass
    grad_output = output_layer - y_train
    grad_hidden = np.dot(grad_output, W2.T)

    # update parameters
    W2 = W2 - learning_rate * np.dot(hidden_layer.T, grad_output)
    W1 = W1 - learning_rate * np.dot(X_train.T, grad_hidden)

# evaluate the word embeddings
print("W1 shape = {}".format(W1.shape))
print(W1)
print("W2 shape = {}".format(W2.shape))
print(W2)