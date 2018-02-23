import sys
import os
import threading

def my_filter(filename):
	f=open(filename, "r")
	out=open(filename+"_en", "w")
	line=f.readline()
	while (line):
		if line.split('\t')[0].split('[')[1].split(',')[1].split('/')[2]=='en':
			out.write(line)
		line=f.readline()
	out.close()

threads=[]
for file in os.listdir():
	t=threading.Thread(target=my_filter, args=(file))
	threads.append(t)

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()

