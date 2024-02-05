import tensorflow as tf
from tensorflow.keras import layers

# Check if GPU is available
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

# hyperparameters
batch_size = 16
block_size = 32
max_iters = 5000
eval_interval = 100
learning_rate = 1e-3
eval_iters = 200
n_embd = 64
n_head = 4
n_layer = 4
dropout = 0.0

# ------------

# Download the data or place the file 'input.txt' in the current directory

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])

data = tf.constant(encode(text), dtype=tf.int64)
n = int(0.9*len(data))
train_data = data[:n]
val_data = data[n:]

def get_batch(split):
    data = train_data if split == 'train' else val_data
    ix = tf.random.uniform((batch_size,), minval=0, maxval=len(data) - block_size, dtype=tf.int64)
    x = tf.stack([data[i:i+block_size] for i in ix])
    y = tf.stack([data[i+1:i+block_size+1] for i in ix])
    return x, y

class MultiHeadAttention(layers.Layer):
    def __init__(self, num_heads, head_size):
        super(MultiHeadAttention, self).__init__()
        self.heads = [Head(head_size) for _ in range(num_heads)]
        self.proj = layers.Dense(n_embd)
        self.dropout = layers.Dropout(dropout)

    def call(self, x):
        out = tf.concat([head(x) for head in self.heads], axis=-1)
        out = self.dropout(self.proj(out))
        return out

class Head(layers.Layer):
    def __init__(self, head_size):
        super(Head, self).__init__()
        self.key = layers.Dense(head_size, use_bias=False)
        self.query = layers.Dense(head_size, use_bias=False)
        self.value = layers.Dense(head_size, use_bias=False)
        self.tril = tf.linalg.band_part(tf.ones((block_size, block_size)), -1, 0)
        self.dropout = layers.Dropout(dropout)

    def call(self, x):
        B, T, C = x.shape
        k = self.key(x)
        q = self.query(x)
        wei = tf.matmul(q, k, transpose_b=True) * tf.math.rsqrt(tf.cast(C, tf.float32))
        wei = tf.where(self.tril == 0, float('-inf'), wei)
        wei = tf.nn.softmax(wei, axis=-1)
        wei = self.dropout(wei)
        v = self.value(x)
        out = tf.matmul(wei, v)
        return out

class FeedForward(layers.Layer):
    def __init__(self):
        super(FeedForward, self).__init__()
        self.net = tf.keras.Sequential([
            layers.Dense(4 * n_embd, activation='relu'),
            layers.Dense(n_embd),
            layers.Dropout(dropout),
        ])

    def call(self, x):
        return self.net(x)

class Block(layers.Layer):
    def __init__(self):
        super(Block, self).__init__()
        self.sa = MultiHeadAttention(n_head, n_embd // n_head)
        self.ffwd = FeedForward()
        self.ln1 = layers.LayerNormalization(epsilon=1e-6)
        self.ln2 = layers.LayerNormalization(epsilon=1e-6)

    def call(self, x):
        x = x + self.sa(self.ln1(x))
        x = x + self.ffwd(self.ln2(x))
        return x

class BigramLanguageModel(tf.keras.Model):
    def __init__(self):
        super(BigramLanguageModel, self).__init__()
        self.token_embedding_table = layers.Embedding(vocab_size, n_embd)
        self.position_embedding_table = layers.Embedding(block_size, n_embd)
        self.blocks = [Block() for _ in range(n_layer)]
        self.ln_f = layers.LayerNormalization(epsilon=1e-6)
        self.lm_head = layers.Dense(vocab_size)

    def call(self, idx, targets=None):
        B, T = idx.shape
        tok_emb = self.token_embedding_table(idx)
        pos_emb = self.position_embedding_table(tf.range(T, dtype=tf.int64))
        x = tok_emb + pos_emb
        for block in self.blocks:
            x = block(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)

        if targets is None:
            loss = None
        else:
            loss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=targets, logits=logits)
            loss = tf.reduce_mean(loss)

        return logits, loss

    def generate(self, idx, max_new_tokens):
        for _ in range(max_new_tokens):
            idx_cond = idx[:, -block_size:]
            logits, _ = self(idx_cond)
            logits = logits[:, -1, :]
            probs = tf.nn.softmax(logits, axis=-1)
            idx_next = tf.random.categorical(logits=logits, num_samples=1, dtype=tf.int64)
            idx = tf.concat([idx, idx_next], axis=1)
        return idx

model = BigramLanguageModel()
optimizer = tf.keras.optimizers.Adam(learning_rate)

for iter in range(max_iters):
    if iter % eval_interval == 0 or iter == max_iters - 1:
        train_loss = 0.0
        val_loss = 0.0
        for _ in range(eval_iters):
            x_train, y_train = get_batch('train')
            x_val, y_val = get_batch('val')

            _, train_loss_iter = model(x_train, y_train)
            train_loss += train_loss_iter

            _, val_loss_iter = model(x_val, y_val)
            val_loss += val_loss_iter

        train_loss /= eval_iters
        val_loss /= eval_iters

        print(f"step {iter}: train loss {train_loss.numpy():.4f}, val loss {val_loss.numpy():.4f}")

    x_batch, y_batch = get_batch('train')

    with tf.GradientTape() as tape:
        logits, loss = model(x_batch, y_batch)

    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

context = tf.zeros((1, 1), dtype=tf.int64)
generated_text
