# Data-Science
Data Exploration and Machine Learning for dating profile effectiveness


### About the Project:

Our data is made up from 60,000 Scraped OKCupid Profiles from 2015. 30,000 from SF will be used to train a tfidf vectorizer and k-means clustering algorithm. We will then run the user input through the trained algorithms to determine which cluster it belongs to and the distance from that cluster’s centroid. That distance is then compared to the standard deviation of the cluster’s centroid distance to create a weighted value of how closely the user description fits the closest paradigm. This is a lean, mean form of topic analysis with tested NLP methods. The output is an integer grading how well the description “fits” the paradigm. 
