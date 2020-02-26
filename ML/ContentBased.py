#Much of this code is based off of https://github.com/nikitaa30/Content-based-Recommender-System/blob/master/recommender_system.py

import pandas as pd
import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.SoftwareEngineering

ArtCollection = db["ArtRepo"]

articleList = ArtCollection.find({})

matrix = [[]]

i = 0
for doc in articleList:
    #print(doc["Title"])
    #print(doc["Description"])
    #print("\n")
    matrix.append([i, doc["Title"], doc["Description"]])
    i += 1

df = pd.DataFrame(matrix)

df = df.dropna()

df.columns = ['id', 'Title', 'Description']

df = df.astype({'id' : int})

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(df['Description'])

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

df = df.set_index("id")

results = {}

for idx, row in df.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
#    print(idx)
    similar_items = [(cosine_similarities[idx][i], df['Title'][i]) for i in similar_indices]

    results[row['Title']] = similar_items[1:]
    
print('done!')

# Just reads the results out of the dictionary.
def recommend(title, num):
    print(title)
    print("-------")
    recs = results[title][:num]
    for rec in recs:
        print("Recommended: " + str(rec))

recommend(df.iloc[10,0], 5)
