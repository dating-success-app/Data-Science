from math import ceil
from pickle import load
from par_reqs import tokenize
from sklearn.metrics.pairwise import cosine_similarity

desc = ['I love to listen and cook and friends. I like to laugh while baking things.']


def load_models(desc):

    tfidf = load(open('vect.sav', 'rb'))
    kmeans = load(open('means.sav', 'rb'))

    new_vect = tfidf.transform(desc)
    new_cluster = kmeans.predict(new_vect)[0]

    sim = cosine_similarity(kmeans.cluster_centers_[new_cluster].reshape(1,-1),
                            new_vect.toarray().reshape(1,-1))

    final = ceil((sim * 100)[0][0])

    return final