# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:34:44 2021

@author: Md Abul Bashar
"""

# Help: https://github.com/mdabashar/miscellaneous/blob/master/TweetPreprocessing.ipynb

# Installation the library
# pip install ekphrasis

# Import Required Libraries
from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.dicts.emoticons import emoticons

class SentencePreprocessor:
    
    def __init__(self):

        # Define a Text Pre-Processing pipeline
        # You can easily define a preprocessing pipeline, by using the TextPreProcessor.
        self.text_processor = TextPreProcessor(
            # terms that will be normalized
            normalize=['url', 'email', 'percent', 'money', 'phone', 'user',
                'time', 'url', 'date', 'number'],
            # terms that will be annotated
            annotate={"hashtag", "allcaps", "elongated", "repeated",
                'emphasis', 'censored'},
            fix_html=True,  # fix HTML tokens
            
            # corpus from which the word statistics are going to be used 
            # for word segmentation 
            segmenter="english", 
            
            # corpus from which the word statistics are going to be used 
            # for spell correction
            corrector="english", 
            
            unpack_hashtags=True,  # perform word segmentation on hashtags
            unpack_contractions=True,  # Unpack contractions (can't -> can not)
            spell_correct_elong=False,  # spell correction for elongated words
            
            # select a tokenizer. You can use SocialTokenizer, or pass your own
            # the tokenizer, should take as input a string and return a list of tokens
            tokenizer=SocialTokenizer(lowercase=True).tokenize,
            
            # list of dictionaries, for replacing tokens extracted from the text,
            # with other expressions. You can pass more than one dictionaries.
            dicts=[emoticons])
    
    def prepro_sent(self, sent):
        # As smart quote is not handled in ekphrasis
        sent = sent.replace('‘', '\'').replace('’', '\'').replace('“', '"').replace('”', '"')
        return ' '.join(self.text_processor.pre_process_doc(sent))


def main():

    '''
    Test Some tweets
    
    Notes:
        1. elongated words are automatically normalized.
        2. Spell correction affects performance.
    '''
    
    sentences = [
        "CANT WAIT for the new season of #TwinPeaks ＼(^o^)／!!! #davidlynch #tvseries :)))",
        "I saw the new #johndoe movie and it suuuuucks!!! WAISTED $10... #badmovies :/",
        "@SentimentSymp:  can't wait for the Nov 9 #Sentiment talks!  YAAAAAAY !!! :-D http://sentimentsymposium.com/."
    ]
    
    sp = SentencePreprocessor()
    for sent in sentences:
        print(sp.prepro_sent(sent))
        print()

if __name__=='__main__':
    main()




