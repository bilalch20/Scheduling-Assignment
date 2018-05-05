def fcfs():
	print"Enter number of processes"
	size=int(input())
	at=[0]*size
	for i in range(size):
		print"Enter the arrival time for process ",i+1,":"		
		at[i]=int(raw_input())
	bt=[0]*size
	for j in range(size):
		print"Enter the burst time for process ",j+1,":"
		bt[j]=int(raw_input())
	sat=sorted(at)
	for l in range(size):
		b=at.index(sat[l])
		print"Process",b+1,"is in execution"
		time.sleep(bt[b])
		print"Process",b+1,"executed"
def sjf():
	print"Enter number of processes"
	size=int(input())
	at=[0]*size
	for i in range(size):
		print"Enter the arrival time for process ",i+1,":"		
		at[i]=int(raw_input())
	bt=[0]*size
	for j in range(size):
		print"Enter the burst time for process ",j+1,":"
		bt[j]=int(raw_input())
	sbt=sorted(bt)
	for l in range(size):
		b=bt.index(sbt[l])
		print"Process",b+1,"is in execution"
		time.sleep(bt[b])
		print"Process",b+1,"executed"
def rr():
	size=input("Enter number of processes:")	
	at=[0]*size	
	for i in range(size):
		print"Enter the arrival time for process ",i+1,":"		
		at[i]=int(raw_input())
	bt=[0]*size
	for j in range(size):
		print"Enter the burst time for process ",j+1,":"
		bt[j]=int(raw_input())
	summ=sum(bt)
	sat=sorted(at)
	t=0
	k=0
	while t!=summ
		
		cur=sat[k]		
		b=at.index(cur)
		nex=sat[k+1]
		b1=at.index(nex)
		while 
			print"Process",k+1,"is in execution"
			time.sleep(1)
			t=t+1
			if t==bt[b1]
				k=k+1
			

import time
print"Select one option."
print"1.FCFS"
print"2.SJF"
print"3.RR"
print"4.VRR"
print"5.MQ"
print"6.MFQ"

a=input()

if a==1:
	fcfs()
elif a==2:
	sjf()
elif a==3:
	rr()
else
	print"Wrong option chosen."

