

from __future__ import absolute_import, division, print_function
import os, sys, re
import pickle
import tflearn
from tflearn.data_utils import *
from docopt import docopt

""" Build dataset from textfile: input data, labels and dictionary"""
def build_dataset(input, maxlen, char_idx=None, char_idx_file='char_idx.pickle'):
    X, Y, char_idx = \
        textfile_to_semi_redundant_sequences(input, seq_maxlen=maxlen,
            redun_step=3, pre_defined_char_idx=char_idx)
    pickle.dump(char_idx, open(char_idx_file,'wb'))
    return X, Y, char_idx

""" Load a saved dictionary from a file"""
def load_dictionary(char_idx_file='char_idx.pickle'):
    char_idx = None
    if os.path.isfile(char_idx_file):
        print('Loading dictionary from %s' % char_idx_file)
        char_idx = pickle.load(open(char_idx_file, 'rb'))
    return char_idx

""" Build the deep neural network model for generating sequences"""
def build_model(maxlen, char_idx, checkpoint_path):
    pass

""" Load a saved model from a file"""
def load_model(model):
    if os.path.isfile('checkpoint'):
        f = open('checkpoint', 'r')
        regex = re.compile('model_checkpoint_path:\s\"(.*)\"')
        filename = regex.findall(f.read())
        if filename:
            print('Loading model from %s' % filename[0])
            model.load(filename[0])

""" Build or load the dataset, dictionary and model"""
def prepare(parameters, dataset_needed=False):
    pass

""" Train a model on the input dataset"""
def train(parameters):
    pass

""" Generate new content from the trained model"""
def generate(parameters):
    pass

""" Cast numeric parameters"""
def cast_parameters(parameters):
    parameters['--count'] = int(parameters['--count'])
    parameters['--maxlen'] = int(parameters['--maxlen'])
    parameters['--temperature'] = float(parameters['--temperature'])
    return parameters

if __name__ == '__main__':
    parameters = cast_parameters(docopt(__doc__))
    if parameters['train']:
        train(parameters)
    elif parameters['generate']:
        generate(parameters)
