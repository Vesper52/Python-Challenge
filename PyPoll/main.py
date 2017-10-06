from __future__ import division
import csv

#If for some reason you do some of this work again on your work laptop raw_input only works on version 2.0, input works on 3.0 I know its stupid
Candidates=[]
Unique_Candidates=[]


num_of_files=input("How many files are there: ")

def PyPoll(num_of_files):
	file_range=int(num_of_files)
	k=0
	highest_vote_count=0
	New_Mayor=''
	while k < file_range:
		poll_file=input("Please enter the csv file: ")

		with open(poll_file) as csvfile:
			csvfile_reader=csv.DictReader(csvfile)
			for row in csvfile_reader:
				Candidates.append(row['Candidate'])


		for x in Candidates:
			if x not in Unique_Candidates:
				Unique_Candidates.append(x)


		k+=1

	#print(Unique_Candidates)
	print('--------------------------------')
	print("Election Results")
	print('--------------------------------')
	print('Total Votes: '+str(len(Candidates)))	
	print('---------------------------------')

		#print(Candidates.count('Khan(('))
	for i in Unique_Candidates:
			
		print("Count for "+i+" is " +str(Candidates.count(i))+" %"+str(round(Candidates.count(i)/len(Candidates)*100,2)))
		if Candidates.count(i)>highest_vote_count:
			#print(New_Mayor)
			highest_vote_count=Candidates.count(i)
			New_Mayor=i
	print('--------------------------------')
	print('The winner!!!!: '+New_Mayor)
	print('--------------------------------')


	file=open("Polling_Results.txt","w")
	file.write('--------------------------------\n')
	file.write("Election Results\n")
	file.write('--------------------------------\n')
	file.write('Total Votes: '+str(len(Candidates))+'\n')

	file.write('---------------------------------\n')
	for i in Unique_Candidates:
			
		file.write("Count for "+i+" is " +str(Candidates.count(i))+" %"+str(round(Candidates.count(i)/len(Candidates)*100,2))+'\n')
	file.write('--------------------------------\n')
	file.write('The winner!!!!: '+New_Mayor+'\n')
	file.write('--------------------------------\n')
	file.close()
	
PyPoll(num_of_files)


