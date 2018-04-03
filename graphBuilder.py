# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
def readcsv():
    G={}
    
    with open('G','rt',encoding="utf8") as file:
        print('start')
        totalRelations=0
        totalItems=0
        for i,row in enumerate(file):
            totalRelations+=1
            if (len(row.split()) != 3):
                continue
            rel,item1,item2 = row.split()
            #print(item1)
            if item1 in G:
                G[item1][0] += [item2]  #edge
                G[item1][1] += [rel]    #label
                G[item1][2] += 1        #degree
            else:
                G[item1] = [[item2],[rel],1]
                totalItems+=1
        #print(G)   
        print(totalItems)
        print(totalRelations)
        print('done')
        return G

def plotHist(G):
    Hist = {}
    for item in G:
        if G[item][2] not in Hist:
            Hist[G[item][2]] = 1
        else:
            Hist[G[item][2]] +=1
        if G[item][2] > 1500:
            print(item, G[item][2])
    xAxis = list(Hist.keys())
    yAxis = list(Hist.values())
    plt.scatter(xAxis,yAxis)

    plt.show()

        
readcsv()