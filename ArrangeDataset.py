from numpy import loadtxt
import  numpy as np
import matplotlib.pyplot  as plt
import sys
def full(filename):

	path="C:/Users/ROG/Downloads/musdb18/Temp/"
	savepath="C:/Users/ROG/Downloads/musdb18/excels/"
	

	def refine(a,b,c,d):
		data= np.zeros((len(np.unique(np.array(b))),4))
		i=0
		k=0
		while(k<len(a)):
			if(i==0):
				data[i][0]=b[k] #time
				data[i][1]=a[k] #BPM
				data[i][2]=c[k] #pitch
				data[i][3]=d[k] #vol
				
				
			else:
				while(b[k]==b[k-1]):
					k=k+1    
				data[i][0]=b[k] #time
				data[i][1]=a[k] #BPM
				data[i][2]=c[k] #pitch
				data[i][3]=d[k] #vol
			i=i+1
			k=k+1

		return data, data[i-1][0],(i-1)
		
			
















	bpm0 = loadtxt(path+filename+"0bpm.txt", comments="#", delimiter=",", unpack=False)
	bpm1 = loadtxt(path+filename+"1bpm.txt", comments="#", delimiter=",", unpack=False)
	bpm2 = loadtxt(path+filename+"2bpm.txt", comments="#", delimiter=",", unpack=False)
	bpm3 = loadtxt(path+filename+"3bpm.txt", comments="#", delimiter=",", unpack=False)
	bpm4 = loadtxt(path+filename+"4bpm.txt", comments="#", delimiter=",", unpack=False)

	time0 = loadtxt(path+filename+"0time.txt", comments="#", delimiter=",", unpack=False)
	time1 = loadtxt(path+filename+"1time.txt", comments="#", delimiter=",", unpack=False)
	time2 = loadtxt(path+filename+"2time.txt", comments="#", delimiter=",", unpack=False)
	time3 = loadtxt(path+filename+"3time.txt", comments="#", delimiter=",", unpack=False)
	time4 = loadtxt(path+filename+"4time.txt", comments="#", delimiter=",", unpack=False)

	pitch0 = loadtxt(path+filename+"0pitch.txt", comments="#", delimiter=",", unpack=False)
	pitch1 = loadtxt(path+filename+"1pitch.txt", comments="#", delimiter=",", unpack=False)
	pitch2 = loadtxt(path+filename+"2pitch.txt", comments="#", delimiter=",", unpack=False)
	pitch3 = loadtxt(path+filename+"3pitch.txt", comments="#", delimiter=",", unpack=False)
	pitch4 = loadtxt(path+filename+"4pitch.txt", comments="#", delimiter=",", unpack=False)

	vol0 = loadtxt(path+filename+"0vol.txt", comments="#", delimiter=",", unpack=False)
	vol1 = loadtxt(path+filename+"1vol.txt", comments="#", delimiter=",", unpack=False)
	vol2 = loadtxt(path+filename+"2vol.txt", comments="#", delimiter=",", unpack=False)
	vol3 = loadtxt(path+filename+"3vol.txt", comments="#", delimiter=",", unpack=False)
	vol4 = loadtxt(path+filename+"4vol.txt", comments="#", delimiter=",", unpack=False)
	

	



	tab0, s0 , size0 =refine(bpm0,time0,pitch0,vol0)
	tab1, s1 , size1 =refine(bpm1,time1,pitch1,vol1)
	tab2, s2 , size2 =refine(bpm2,time2,pitch2,vol2)
	tab3, s3 , size3 =refine(bpm3,time3,pitch3,vol3)
	tab4, s4 , size4 =refine(bpm4,time4,pitch4,vol4)
	



	# plt.plot(bpm0)
	# plt.plot(bpm1)
	# plt.plot(bpm2)
	# plt.plot(bpm3)
	# plt.plot(bpm4)
	# plt.show()

	# print(s0)
	# print(s1)
	# print(s2)
	# print(s3)
	# print(s4)

	max= s0
	if(max<s1):
		max=s1
	if(max<s2):
		max=s2
	if(max<s3):
		max=s3
	if(max<s4):
		max=s4

	#Creating Number of columns in master list
	x=0.00
	count=0
	while(x<= max):
		count=count+1
		x=round(x+0.01,2)
		

	# Master List    
	data= np.zeros((count,16))


	# Creating the Master List
	x=0
	count=0
	while(x<= max):
		data[count][0]=x
		x=round(x+0.01,2)
		count=count+1
		
	
	

	b0=b1=b2=b3=b4=t0=t1=t2=t3=t4=0
	p0=p1=p2=p3=p4=v0=v1=v2=v3=v4=0
	count=0
	while(data[count][0]< max):
		
		# 1st Oscillator
		if(t0==size0):
			t0=t0-1
		if(data[count][0]==tab0[t0][0]):
			data[count][1]=tab0[b0][1]
			data[count][2]=tab0[b0][2]
			data[count][3]=tab0[b0][3]
			b0=b0+1
			t0=t0+1
		if(data[count][0]!=tab0[t0][0]):
			data[count][1]=tab0[b0][1]
			data[count][2]=tab0[b0][2]
			data[count][3]=tab0[b0][3]
		
		# # 2nd Oscillator
		if(t1==size1):
			t1=t1-1	
		if(data[count][0]==tab1[t1][0]):
			data[count][4]=tab1[b1][1]
			data[count][5]=tab1[b1][2]
			data[count][6]=tab1[b1][3]
			b1=b1+1
			t1=t1+1
		if(data[count][0]!=tab1[t1][0]):
			data[count][4]=tab1[b1][1]
			data[count][5]=tab1[b1][2]	
			data[count][6]=tab1[b1][3]
			

		
		# # 3rd Oscillator
		if(t2==size2):
			t2=t2-1    
		if(data[count][0]==tab2[t2][0]):
			data[count][7]=tab2[b2][1]
			data[count][8]=tab2[b2][2]
			data[count][9]=tab2[b2][3]
			b2=b2+1
			t2=t2+1
			
		if(data[count][0]!=tab2[t2][0]):
			data[count][7]=tab2[b2][1]
			data[count][8]=tab2[b2][2]
			data[count][9]=tab2[b2][3]
		
		# # 4th Oscillator
		if(t3==size3):
			t3=t3-1	
		if(data[count][0]==tab3[t3][0]):
			data[count][10]=tab3[b3][1]
			data[count][11]=tab3[b3][2]
			data[count][12]=tab3[b3][3]
			b3=b3+1
			t3=t3+1
		if(data[count][0]!=tab3[t3][0]):
			data[count][10]=tab3[b3][1]
			data[count][11]=tab3[b3][2]
			data[count][12]=tab3[b3][3]
		
		
		# # 5th Oscillator
		if(t4==size4):
			t4=t4-1	
		if(data[count][0]==tab4[t4][0]):
			data[count][13]=tab4[b4][1]
			data[count][14]=tab4[b4][2]
			data[count][15]=tab4[b4][3]
			b4=b4+1
			t4=t4+1
		if(data[count][0]!=tab4[t4][0]):
			data[count][13]=tab4[b4][1]
			data[count][14]=tab4[b4][2]
			data[count][15]=tab4[b4][3]
			
			
		count=count+1
		

		
		
	# plt.plot( data[:,1])
	# plt.plot( data[:,2])
	# plt.plot( data[:,3])
	# plt.plot( data[:,4])
	# plt.plot( data[:,5])

	# plt.show()


	rows=data


	import xlwt
	workbook = xlwt.Workbook()
	sheet = workbook.add_sheet("Sheet")

	for i in range(len(rows)):
		for j in range(len(rows[i])):
			sheet.write(i, j, rows[i][j])

	workbook.save(savepath+filename+".xls")
	
	
import os

txt="listtest.txt"
with open(txt) as f:
    lines=f.read().splitlines()
for i in lines:
    full(i)
    print("Done :: ",i)