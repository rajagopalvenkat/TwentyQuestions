import numpy as np
import sys
from collections import Counter

f=open(sys.argv[1],"r",encoding="utf8")
lines=f.readlines()

G={}
rel={ "IsA":0, "UsedFor":1, "AtLocation":2, "HasA":3, "HasProperty":4, "HasSubevent":5, "InstanceOf":6, "SimilarTo":7, "product":8, "occupation":9, "leader":10, "language":11, "knownFor":12, "influencedBy":13, "genre":14, "field":15, "capital":16}
hierarchical = ['InstanceOf','IsA','HasA', 'HasProperty', 'HasSubevent', 'SimilarTo', 'RelatedTo']

commonality={}

for line in lines:
	if len(line.split())==3:
		arr=line.split()
		if arr[2] in rel:
			if arr[1] in G:
				G[arr[1]][rel[arr[2]]] += [arr[0],]
			else:
				G[arr[1]]=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
				G[arr[1]][rel[arr[2]]] += [arr[0],]
		else:
			if arr[2]=="RelatedTo":
				if arr[0] in commonality:
					commonality[arr[0]]+=1
				else:
					commonality[arr[0]]=1
				if arr[1] in commonality:
					commonality[arr[1]]+=1
				else:
					commonality[arr[1]]=1

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

print (itemRel[:10])

inp="No"
ans=False
i=0

posAns=[]
negAns=[]
vis=[]
import random
qCount=0
no=0

while ans==False:
	if len(itemRel) >=1 and (20-qCount)>=5 and i<len(itemRel):
		if itemRel[i][0] in vis:
			i+=1
		else:
			c=0
			'''
			if qCount>14:
				for x in posAns:
					if itemRel[i][0] not in G[x[0]][rel[x[1]]]:
						c+=1
						print itemRel[i][0] + " : " + x[0] + " : Pos"
						break
			'''
			for x in negAns:
				if itemRel[i][0] in G[x[0]][rel[x[1]]]:
					c+=1
					print (itemRel[i][0] + " : " + x[0] + " : Neg")
					break
			if c==0:
				qCount+=1
				#print itemRel[:10]
				print ("Is it " + itemRel[i][1] + " " + itemRel[i][0] + "?\n")
				inp=input()
				vertex=itemRel[i][0]
				relation=itemRel[i][1]
				vis+=[vertex,]
				if inp=="No" or inp =="no":
					negAns+=[[vertex, relation],]
					if len(posAns)>0:
						no+=1
					i+=1
				else:
					no=0
					itemRel=[]
					objs=[]
					#print G[vertex][rel[relation]]
					for v in G[vertex][rel[relation]]:
						objs+=[v,]
						if v in G and v not in vis:
							for r in rel.keys():
								itemRel+=[[v, r, len(G[v][rel[r]])],]
								

					posAns+=[[vertex, relation],]
					itemRel.sort(key=lambda x: int(x[2]), reverse=True)
					#print(len(itemRel))
					'''
					if len(itemRel)<=10:		#FIX THIS
						while ans==False:
							print "Is it a " + G[vertex][rel[relation]][random.randint(0,len(G[vertex][rel[relation]])-1)] + " ?\n"
							answer=raw_input()
							if answer=="Yes" or answer=="yes":
								ans=True
					'''
					i=0
			else:
				i+=1
	else:
		objsPr=[]
		for obj in objs:
			if obj in commonality:
				objsPr+=[commonality[obj]+1,]
			else:
				objsPr+=[1,]
		tot=sum(objsPr)
		objsPr=[float(i)/tot for i in objsPr]
		print (objs)
		while ans==False:
			x=np.random.choice(objs, 1, p=objsPr)[0]
			if x not in vis:
				c=0
				vis+=[x, ]
				print ("Is it " + x + " ?\n")
				answer=input()
				if answer=="Yes" or answer=="yes":
					ans=True
				else:
					ind=objs.index(x)
					del objs[ind]
					objsPr=[]
					for obj in objs:
						if obj in commonality:
							objsPr+=[commonality[obj]+1,]
						else:
							objsPr+=[1,]
					tot=sum(objsPr)
					objsPr=[float(i)/tot for i in objsPr]
