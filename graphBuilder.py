# -*- coding: utf-8 -*-
import csv


def readcsv():
    G={}
    
    with open('C:\\Users\\Joel\\Downloads\\cn\\assertions.csv','rt',encoding="utf8") as file:
        rows = csv.reader(file, delimiter='\t', quotechar='\"')
        print('start')
        totalRelations=0
        totalItems=0
        for i,row in enumerate(rows):
            if not row[2].startswith('/c/en/') or not row[3].startswith('/c/en/'):
                continue
            #print(row)
            totalRelations+=1
            rel,item1,item2 = row[1],row[2][6:],row[3][6:]
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
        
readcsv()
            
        
    '''stats:
        937,364     words (split by part of speech)
        2,809,253   relations
    '''
    #44:30 to 47:30