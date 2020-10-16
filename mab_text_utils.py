# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:02:08 2020

@author: basharm
"""

from collections import Counter
from itertools import chain

class MabTextUtils():
    
    def __init__():
        pass
    
    @staticmethod
    def get_word_freq(sent_list):
        '''
        Get a dictionary of word freq
        Arguments:
            sent_list: list # a list of sentences
        returns:
            freq_dict: dict # a dictionary of word freq
        Method:
            1. map(str.split, sent_list) is making a generator 
            that returns list of words from each sentence.
            2. chain.from_iterable converts lists to a single generator 
            that produces a word at a time.
            3. Counter takes an input iterable and counts all unique values in it.
        '''
        freq_dict = Counter(list(chain.from_iterable(map(str.split, sent_list))))
        return freq_dict
    
    @staticmethod
    def remove_infreq_words(sents, min_count):
        '''
        Remove infrequent words
        Arguments:
            sents: list # a list of sentences
            min_count: int # minimum frequency count used for removing words
        returns:
            sents: list # a list of sentences after infrequent words removed
        '''
        word_freq_dict = MabTextUtils.get_word_freq(sents)
        remove = lambda sent: ' '.join(w for w in sent.split() if word_freq_dict[w]>min_count)
        return list(map(remove, sents))

    
    @staticmethod
    def clean_non_ascii(sent):
        '''
        Remove Non ASCII (i.e. non english) characters from a sentence.
        Arguments:
            sent: str
        returns: 
            sent: str
        '''
        return ''.join(i for i in sent if ord(i) < 128)
    
if __name__=='__main__':
    texts=["dog cat fish","dog cat cat","fish bird", 'bird pet']
    
    print(MabTextUtils.get_word_freq(texts))
    
    print(MabTextUtils.clean_non_ascii(texts[0]))
    
    print(MabTextUtils.remove_infreq_words(sents=texts, min_count=1))