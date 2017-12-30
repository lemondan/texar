"""Common utils.."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pdb

import time
import random
import numpy as np

def log_print(line):
  """Add time to print function."""
  print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
        + "] " + line)

def load_data(path):
  data = []
  with open(path) as f:
    for line in f:
      data.append(line.split())
  return data

def data_to_id(data, word2id):
  data_id = [[word2id[word] if word in word2id else word2id["_UNK"]
              for word in sent ] for sent in data]
  return data_id

def write_sent(sents, path):
  with open(path, "w") as f:
    for sent in sents:
      f.write(" ".join(sent) + "\n")

def makeup(_x, n):
  x = []
  for i in range(n):
    x.append(_x[i % len(_x)])
  return x

def strip_eos(sents):
  return [sent[:sent.index("_EOS")] if "_EOS" in sent else sent
          for sent in sents]

def logits2word(logits, id2word):
  sents = np.argmax(logits, axis=2).tolist()
  sents = [[id2word[word] for word in sent] for sent in sents]
  return strip_eos(sents)

def write_sent(sents, path):
  with open(path, "w") as f:
    for sent in sents:
      f.write(" ".join(sent) + "\n")

def reorder(order, _x):
  x = range(len(_x))
  for i, a in zip(order, _x):
    x[i] = a
  return x