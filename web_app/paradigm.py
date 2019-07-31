from pickle import load
from par_reqs import tokenize

desc = ['I like tacos, hiking and craft cocktails.']


def load_models(desc):

    tfidf = load(open('vect.sav', 'rb'))
    kmeans = load(open('means.sav', 'rb'))

    v_desc = tfidf.transform(desc)

    return v_desc