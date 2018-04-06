import numpy
import sys
from collections import Counter

f=open(sys.argv[1],"r")
lines=f.readlines()

G={}
rel={ "IsA":0, "UsedFor":1, "AtLocation":2, "HasA":3, "HasProperty":4, "HasSubevent":5, "InstanceOf":6, "SimilarTo":7, "product":8, "occupation":9, "leader":10, "language":11, "knownFor":12, "influencedBy":13, "genre":14, "field":15, "capital":16  }
hierarchical = ['InstanceOf','IsA','HasA', 'HasProperty', 'HasSubevent', 'SimilarTo', 'RelatedTo']

for line in lines:
	if len(line.split())==3:
		arr=line.split()
		if arr[2] in rel:
			if arr[1] in G:
				G[arr[1]][rel[arr[2]]] += [arr[0],]
			else:
				G[arr[1]]=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
				G[arr[1]][rel[arr[2]]] += [arr[0],]

def recAddRel(root, rl):
	newl=[]
	for n in G[root][rel[rl]]:
		if n in G:
			for n2 in G[n][rel[rl]]:
				if n2 not in G[root][rel[rl]]:
					newl+=[n2,]
					#G[root][rel[rl]]+=[n2,]
	for i in newl:
		G[root][rel[rl]]+=[i,]

for key in ['plant', 'animal', 'person', 'place', 'object']:
	for r in rel:
		if r == 'IsA':
			recAddRel(key, r)

itemRel=[]

for key in G.keys():
	for i in rel.keys():
		itemRel+=[(key, i, len(G[key][rel[i]])),]

itemRel.sort(key=lambda x: int(x[2]), reverse=True)

print itemRel[:10]

inp="No"
ans=False
i=0

posAns=[]
negAns=[]
vis=[]
import random

while ans==False:
	if itemRel[i][0] not in vis:
		#print itemRel[:10]
		print "Is it " + itemRel[i][1] + " " + itemRel[i][0] + "?\n"
		inp=raw_input()
		vertex=itemRel[i][0]
		relation=itemRel[i][1]
		vis+=[vertex,]
		if inp=="No" or inp =="no":
			negAns+=[[vertex, relation],]
			i+=1
		else:
			itemRel=[]
			#print G[vertex][rel[relation]]
			for v in G[vertex][rel[relation]]:
				c=0
				for x in posAns:
					if v not in G[x[0]][rel[x[1]]]:
						c+=1
						break
				for x in negAns:
					if v in G[x[0]][rel[x[1]]]:
						c+=1
						break
				if c==0:
					if v in G and v not in vis:
						for r in rel.keys():
							itemRel+=[[v, r, len(G[v][rel[r]])],]
			posAns+=[[vertex, relation],]
			itemRel.sort(key=lambda x: int(x[2]), reverse=True)
			print(len(itemRel))
			if len(itemRel)<=20:
				while ans==False:
					print "Is it a " + G[vertex][rel[relation]][random.randint(0,len(G[vertex][rel[relation]])-1)] + " ?\n"
					answer=raw_input()
					if answer=="Yes" or answer=="yes":
						ans=True
			i=0
	else:
		i+=1
