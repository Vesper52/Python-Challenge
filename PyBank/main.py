import csv
import os
Dates=[]
Revenue=[]
Greatest_Rev=0
Greatest_Month=''
Smallest_Rev=0
Smallest_Month=''


num_of_files=input("How many files are there: ")


def PyBank(num_of_files):
	file_range=int(num_of_files)
	i=0
	while i < file_range:
		bank_file=input("Please enter the csv file: ")

		with open(bank_file) as csvfile:
			csvfile_reader= csv.DictReader(csvfile)
			for row in csvfile_reader:
				Dates.append(row['Date'])
		with open(bank_file) as csvfile:
			csvfile_reader= csv.DictReader(csvfile)
			for row in csvfile_reader:
				Revenue.append(row['Revenue'])
		i+=1

PyBank(num_of_files)
Revenue_int=list(map(int,Revenue))
Rev_avg=sum(Revenue_int)/len(Revenue_int)


#Finding the Greateast and Least Revenue Change 

for i,x in enumerate(Revenue_int):
	if x >Greatest_Rev:
		Greatest_Rev=x
		Greatest_Month=Dates[i]
for i,x in enumerate(Revenue_int):
	if x <Smallest_Rev:
		Smallest_Rev=x
		Smallest_Month=Dates[i]

print("  ")
print("Financial Analysis")
print("---------------------------------------")
print("Total Months: "+str(len(Dates)))
print("Total Revenue: $"+str(sum(Revenue_int)))
print("Average Revenue Change: $"+str(Rev_avg))
print("Greatest Increase in Revenue: "+Greatest_Month + " "+"($"+str(Greatest_Rev)+")")
print("Greatest Decrease in Revenue: "+Smallest_Month + " "+"($"+str(Smallest_Rev)+")")


file=open("Financial_Analysis.txt","w")
file.write("Financial Analysis\n")
file.write("---------------------------------------\n")
file.write("Total Months: "+str(len(Dates))+'\n')
file.write("Total Revenue: $"+str(sum(Revenue_int))+'\n')
file.write("Average Revenue Change: $"+str(Rev_avg)+'\n')
file.write("Greatest Increase in Revenue: "+Greatest_Month + " "+"($"+str(Greatest_Rev)+")\n")
file.write("Greatest Decrease in Revenue: "+Smallest_Month + " "+"($"+str(Smallest_Rev)+")\n")
file.close()