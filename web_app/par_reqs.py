from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer


def tokenize(text):

    stemmer = SnowballStemmer('english')
    tokenizer = RegexpTokenizer(r'[a-zA-Z\']+')

    tokenify = [stemmer.stem(word) for word in tokenizer.tokenize(text.lower())]
    
    return tokenify