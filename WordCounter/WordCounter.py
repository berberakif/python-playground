'''
Author: Akif Berber
Date: 2019-05-22
Python 3.5.4
'''

from collections import OrderedDict
import logging as log
import argparse as argparse

class WordCounter(object):
    
    """
    Word Counter with methods of:
    create_dictionary(string): creates a dictionary from given string 
    calculate_highest_frequency(string): returns the word with the highes frequency out of a string
    calculate_frequency_for_word (string, string): returns the frequency of second argument in the first argument
    calculate_most_frequent_n_words (string, int): returns the most frequent n words in the given string

    USAGE:
    python WordCounter.py # no verbose
    python WordCounter.py -v # for detailed info
    """

    '''
    Test  values
    '''
    test_text = 'The sun shines sUN sUn SUN SUN SUNN over the lake LAKe lake lake lake lake'
    test_word = 'sUN'
    test_n = 2
    
    def main(self):

        '''
        Config verbose
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--verbosity', action="count", help="increase output verbosity (e.g., -vv is more than -v)")
        args = parser.parse_args()

        if args.verbosity:
            log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        else:
            log.basicConfig(format="%(levelname)s: %(message)s")
        ''' 
        Calls test functions with given test text, word and n
        '''		
        self.test_calculate_highest_frequency()
        self.test_calculate_frequency_for_word()
        self.test_calculate_most_frequent_n_words()
        
    def create_dictionary(self,text):
        '''
        creates a dictionary from given text 
        having "word & case insensitive frequency" as "key-value" pairs
        returns sorted by values version of that dictionary created  

        Parameters
        ----------
        text : string
            string to be converted to dictionary

        Returns
        -------
        OrderedDict
            sorted by values version of that dictionary contains "word & case insensitive frequency" as "key-value" pairs
        ''' 
    
        unsorted_frequencies = dict()
        words = text.lower().split() #

        for word in words:
            if word in unsorted_frequencies:
                unsorted_frequencies[word] += 1
            else:
                unsorted_frequencies[word] = 1
			
        resultDict = OrderedDict(sorted(unsorted_frequencies.items(), key=lambda x: x[1], reverse=True))
        #log.info('Ordered Dictionary for ' + text + ':' )
        #log.info(resultDict)
				
        # SORT dictionary BY VALUE and return
        return resultDict


    def calculate_highest_frequency(self,text):
        '''
        calculates highest frequency and returns key-value pair

        Parameters
        ----------
        text : string to be analysed for the highes frequency word

        Returns
        -------
        string, int : word and frequency pair
        ''' 
        d = self.create_dictionary(text) # create the dictionary
        log.info('The Most Frequent word for [' + text + ']: ' + list(d.keys())[0] + ', '+ str(list(d.values())[0]) + ' times' )
        return list(d.values())[0] # return first value
        

    def calculate_frequency_for_word (self, text, word):
        '''
        calculates highest frequency and returns key-value pair for the given word

        Parameters
        ----------
        text : string to be analysed for the highest frequency word

        Returns
        -------
        int : frequency of the given word in given text
        '''

        d = self.create_dictionary(text)
        log.info('Frequency of [' + word + '] in [' + text +  ']: '+ str(d[word.lower()]) + ' times' )
        return d[word.lower()] # return the frequency for that word

    def calculate_most_frequent_n_words (self, text, n):
        '''
        finds the highest n frequent words and returns key-value pairs

        Parameters
        ----------
        text : string to be analysed for the highest frequency word
        n: int, number of expected pairs

        Returns
        -------
        OrderedDict
            N most frequent "word & case insensitive frequency" pairs
        '''
        d = self.create_dictionary(text)   
        result_dict = dict(list(d.items())[:n]) # get first n items from the ordered dictionary
        log.info('Most frequent ' + str(n) + ' words in [' + text +  ']: '+ str(result_dict) )
        return result_dict

    '''
        TEST FUNCTIONS
    '''
    def test_calculate_highest_frequency(self):
        assert self.calculate_highest_frequency(self.test_text) == 6, "Should be 6"
        
    def test_calculate_frequency_for_word(self):
        assert self.calculate_frequency_for_word(self.test_text, self.test_word) == 5, "Should be 5"
    
    def test_calculate_most_frequent_n_words(self):
        assert self.calculate_most_frequent_n_words(self.test_text, self.test_n) == {'lake': 6, 'sun': 5}, "Should be {'lake': 6, 'sun': 5}"
        
        
if __name__ == '__main__':
    WordCounter().main()
