# import pandas as pd

# df = pd.read_csv('walkingnavi2.csv')

# print (df)
# print df['A']
import pandas as pd
import math
df = pd.read_csv("walkingnavi.csv", encoding="SHIFT-JIS")

#print (df['D'])

listA = []
listB = []
listC = []
listD = []

listA = df['A'] 
listB = df['B']
listC = df['C']
listD = df['D']
maxmin=100
maxmin2=100

leng = len(listA) #idの数


for n in range(leng):
	maxmin=100
	maxmin2=100
	for i in range(leng):
	 	if listB[n]==listB[i]  and n!=i and listC[n]!=listC[i] and listD[n]!=listD[i]:
	 		min=abs(listC[n]-listC[i])
	 		min2=abs(listD[n]-listD[i])
	 		cul = (min*min)+(min2*min2)
	 		cul2 = math.sqrt(cul)
	 		if maxmin >= cul2:
	 			maxmin=cul2
	 			number=i+1
	 		# if maxmin2>=min2:
	 		# 	maxmin2=min2
	 		# 	number3=i+1
	 	
	 	# if maxmin >= min:
	 	# 	maxmin=min
	 	# 	number=i+1
	number2=n+1
	print ('id{0}はid{1}と最小誤差{2}をとる'.format(number2,number,maxmin))
	






