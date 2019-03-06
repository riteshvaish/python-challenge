import csv

fp=open('./Resources/election_data.csv','r')
reader=csv.DictReader(fp)
distData={}
sorted_distData={}
totalRows = 0
for row in reader:
    #keep track of the total votes casted
    totalRows = totalRows + 1
        #if dict element existes the increment the value
    if row['Candidate'] in distData:
        thisCount = distData[row['Candidate']]
        newCount = thisCount + 1
        distData[row['Candidate']] = newCount
        #Dict elem does not exists, add now
    else:
        distData[row['Candidate']] = 1
#close the file pointer
fp.close()

#sort the dictionary in descending order. This is the order needed to print in the report
sorted_distData = sorted(distData.items(), key=lambda x: x[1], reverse=True)
#print distData
#print sorted_distData

#Now generate report

print (f"\nElection Results \n------------------------- \nTotal Votes: {str(totalRows)} ")

#read the dictionary and print the report
idx = 0
for Winner in sorted_distData:
    perCent = float((float(Winner[1])/float(totalRows))*100)
    print (str(Winner[0]) + ": " + str(format(perCent, '.3f')) + "% (" + str(Winner[1]) + ")")
    idx = idx + 1
	

key_max = max(distData.keys(), key=(lambda k: distData[k]))
print(f"\n------------------------- \n Winner:  {str(key_max)} \n------------------------- \n ")

#write output to a file
with open("Output.txt", "w") as text_file:
    print (f"\nElection Results \n------------------------- \nTotal Votes: {str(totalRows)} ",file=text_file)
    
    idx = 0
    for Winner in sorted_distData:
        perCent = float((float(Winner[1])/float(totalRows))*100)
        print (str(Winner[0]) + ": " + str(format(perCent, '.3f')) + "% (" + str(Winner[1]) + ")", file=text_file)
        idx = idx + 1



    print(f"\n------------------------- \n Winner:  {str(key_max)} \n------------------------- \n ", file=text_file)
