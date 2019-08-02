import dill
from math import ceil
from pickle import load
from sklearn.metrics.pairwise import cosine_similarity


def load_models(desc):

    """
    NLP Clustering algorithm based on OKCupid accounts. Not a perfect
    for tinder but close enough for a proof of concept. Loads in two 
    Pikcled files, a trained TFIDF Vectorizer and a trained KMeans
    Clustering model. The new string is run through the model and 
    returns a score weighted to preference against the centroids. 

    To see the model training code, find the data_exploration folder
    and the notebooks contained within. 
    """

    tfidf = load(open('vect.pkl', 'rb'))
    kmeans = load(open('means.pkl', 'rb'))

    new_vect = tfidf.transform(desc)
    new_cluster = kmeans.predict(new_vect)[0]

    sim = cosine_similarity(kmeans.cluster_centers_[new_cluster].reshape(1,-1),
                            new_vect.toarray().reshape(1,-1))

    final = (sim * 100)[0][0]

    if final < 50:
        final = final**1.16
        pass
    elif final < 60: 
        final = final**1.1
        pass
    elif final < 70 :
        final = final**1.06
        pass
    elif final < 80:
        final = final**1.04
        pass

    return ceil(final)

