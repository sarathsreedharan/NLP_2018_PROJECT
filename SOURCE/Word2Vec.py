import gensim

import numpy as np

class Word2Vec(object):
    def __init__(self):
        print ("Loading word2vec model ~3.8GB RAM required, this may take a while...")
        self.word2vecModel = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
        self.vocab =np.genfromtxt('./vocab.csv', delimiter=',',dtype='string')


    def computeMostSimilarInVocab(self,word):
        similarList = self.word2vecModel.most_similar(word, self.vocab)
        if(similarList is not None and len(similarList) > 0):
            return similarList[0]



if __name__ == "__main__":
    w2v = Word2Vec()
    print w2v.computeMostSimilarInVocab("illness")