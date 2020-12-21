#natural language processing
#
#header files

#repostitory called project guttenberg-get the materials

#stylometry -quantity study literacy style.It is based on the observation that the authors tends
# to write in relactively consistent, recognizable and unique ways.

#stylometric analysis usrinn python

#you need a bit of hashing in here to get started

import nltk

papers = {"Madison": [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
"Hamilton": [12, 6, ....],
"Jay": [2, 3, 4, 5],
"Shared":[18,19,20],"Disputed":[49,50,51,52,53,54,55,56,57,58,62,63]}

def read_files(filename):
    strings = []
    for file in filename:
        with open(f'federalist_{file}.txt') as f:
            strings.append(f.read())
    return ('\n'.join(strings))
    
federalist_by_author = {}

for author, files in papers.items():
    federalist_by_author[author] = read_files(files)
    
#for author in papers:
    #print(federalist_by_author[author][:100])

#we willl create a graph out of the word data
authors = ("Hamilton", "Madison", "Disputed", "Jay", "Shared")
author_tokens = {}
length_distribution = {}

for author in authors:
    tokens = nltk.word_tokenize(federalist_by_author[author])

    author_tokens[author] = {[token for token in tokens if any(c.isalpha() for c in token)]}
    
    token_lengths = [len(token) for token in author_tokens[author]]
    
    length_distribution[author] = nltk.FreqDist(token_lengths)
    
    length_distribution[author].plot(15, title=author)
    
#this will give five plots for the authors and the shareed and the disputed plots

