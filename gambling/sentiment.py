#vader - valence awareness dictionery and sentiment reasoner
#takes in to count of the sentiment

#download a vader lexicon , lexicon acts as a dictionary here
#convert excel sheet to a data frame with the help of pandas
#data frame is a 2-dimentional structure in the form of a table.

#store facebook data in an xcel sheet

#import pandas and nltk libraries
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#download the vader lexicon dictionary
nltk.downloader.download('vader_lexicon')

#provide proper path to your file
file = "abc.txt"

xl = pd.ExcelFile(file)  #read from the file

#parssing excel sheet to data frame
dfs = xl.parse(xl.sheet_names[0])  #take care of value in the brackets

dfs = list(dfs['Timeline'])  # remove the blank line froomt he data frame
print(dfs)

sid = SentimentIntensityAnalyzer()

str1 = "UTC_05:30"
for data in dfs:
    a = data.find(str1)
    if (a == -1):
        ss = sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k, ss[k])
