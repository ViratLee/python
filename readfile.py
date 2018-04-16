import os
fp = open('file1.txt', 'r')
for eachLine in fp:
	print(eachLine)
fp.close()