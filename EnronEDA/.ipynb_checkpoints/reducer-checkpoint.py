#!/usr/bin/env python
"""
Reducer takes words with their class and partial counts and computes totals.
INPUT:
    word \t class \t partialCount 
OUTPUT:
    word \t class \t totalCount  
"""
import re
import sys

# initialize trackers
current_word = None
spam_count, ham_count = 0,0

# read from standard input
for line in sys.stdin:
    # parse input
    word, is_spam, count = line.split('\t')
    
############ YOUR CODE HERE #########
    count = int(count)

    if word == current_word:
        if is_spam == '1':
            spam_count += count
        else:
            ham_count += count
    else:
        if current_word:
            if spam_count:
                print(f'{current_word}\t{1}\t{spam_count}')
            print(f'{current_word}\t{0}\t{ham_count}')

        if is_spam == '1':
            current_word, spam_count = word, count
            #ham_count = 0
        else:
            current_word, ham_count = word, count
            #spam_count = 0

if current_word == word:
    if is_spam == '1':
        print(f'{current_word}\t{1}\t{spam_count}')
    print(f'{current_word}\t{0}\t{ham_count}')
            
        
############ (END) YOUR CODE #########
