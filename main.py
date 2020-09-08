'''
https://stackoverflow.com/questions/36996391/importing-another-project-as-modules-in-python
https://realpython.com/absolute-vs-relative-python-imports/
'''

# using this to import markov.py from another project
#im naming it as pylib so that we won't get confused between os.path and sys.path
from sys import path as pylib 
import os
# pylib += [os.path.abspath(r'/projectfoo')]
# from projectfoo import preprocessor

import sys
sys.path.append('..')
from Markov import markov

def levenshtein(a,b,i=None,j=None):
	if i == None:
		i = len(a)
		j = len(b)

	if min(i,j) == 0:
		return max(i,j)
	else:
		op_a = levenshtein(a,b,i-1,j) + 1
		op_b = levenshtein(a,b,i,j-1) + 1
		op_c = levenshtein(a,b,i-1,j-1) + (a[i-1] != b[j-1])
		return min(op_a,op_b,op_c)

def similarity(a,b):
	return levenshtein(a,b)*(len(a)+len(b))/len(a)/len(b)

def import_freq_list():
	with open('../../FrequencyWords/content/2018/pt_br/pt_br_50k.txt') as f:
		s = f.readline()
		count = 0
		my_list = []
		while (s!='' and count < 10):
			my_list.append( s.split()[0] )
			count += 1
			s = f.readline()
		return my_list

my_list = import_freq_list()
for p in my_list:
	for q in my_list:
		print("similarity(%s,%s)=%.3f" % (p,q,similarity(p,q)))