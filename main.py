#coding=utf-8
import word2vec


# word2vec.word2vec('./data/5.txt', './out/5.bin', size=100, verbose=True)
# word2vec.word2vec('text8/text8', 'text8/text8.bin', size=100, verbose=True)


# word2vec.word2clusters('text8/text8.bin', 'text8/text8-clusters.txt', 100, verbose=True)


# word2vec.word2vec("data/5.txt", "out/5.bin")

# word2vec.word2clusters('data/5.txt', 'out/5-clusters.txt', 100, verbose=True)

model = word2vec.load('out/5.bin')

print model.vocab
print model.vectors.shape

indexes, metrics = model.cosine(u'服务')
print indexes
print metrics


for x in model.generate_response(indexes, metrics).tolist():
    print x[0], x[1]



import numpy    
def cosine_similarity(model, a, b):
    return numpy.dot(model[a], model[b])/(numpy.linalg.norm(model[a])* numpy.linalg.norm(model[b]))

print cosine_similarity(model, u'服务', u"增值")

from sklearn.cluster import KMeans

data5_list = []
for wordVec in model.vectors:
    wordVecList = []
    for x in wordVec:
        wordVecList.append(x)
    data5_list.append(wordVecList)



ClustersNumber = 10

allCluster = []
for i in xrange(ClustersNumber):
    allCluster.append([])


kmeans = KMeans(n_clusters=ClustersNumber, random_state=0).fit(data5_list)


print model.vocab[0]
print model.vocab[1]
label = kmeans.labels_
print label

for i in xrange(len(label)):
    allCluster[label[i]].append(i)
    # print "I: " , i, label[i]

import codecs
output = codecs.open("out/ans5.txt", "w", "utf-8")


def comparator(a, b):
    vala = kmeans.score([model.vectors[a]]) 
    valb = kmeans.score([model.vectors[a]])
    if vala > valb: return 1
    elif vala == valb : return 0
    else : return -1

for clusterId in xrange(len(allCluster)):
    output.write("-----------------------------------cluster " + str(clusterId) + ":\n")
    # print "cluster ", clusterId, ":"

    print allCluster[clusterId][:30]

    sorted(allCluster[clusterId], cmp = comparator)

    cot = 30
    for x in allCluster[clusterId]:                
        cot -=1
        if cot == 0: break
        output.write(model.vocab[x] + "\n")
        

        


 










# word2vec.word2clusters('text8/text8', 'text8/text8-clusters.txt', 100, verbose=True)


# model = word2vec.load('out/5.bin')


# model = word2vec.load('text8/text8.bin')
# print (model.vectors)

# print model.vectors.shape

# clusters = word2vec.load_clusters('out/5-clusters.txt')
# clusters = word2vec.load_clusters('text8/text8-clusters.txt')


# clusters[u'互联网']




# for x in model.vocab:
#     print x