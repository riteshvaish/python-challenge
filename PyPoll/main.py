import os
import csv
import operator

csvpath = os.path.join(".","Resources","election_data.csv")
vote_count = 0
winner_candidate = 'none'
distData={}
sorted_distData={}

with open (csvpath, newline='') as votefile:
    
    csvread = csv.reader(votefile, delimiter=',')
    # skipo the header
    next(csvread,None)
    # read the file row by row
    for row in csvread:
        vote_count += 1
        # Check if the candidate exists in new dictionay
        if row[2] in distData:
            thisCount = distData[row[2]]
            newCount = thisCount + 1
            distData[row[2]] = newCount
        # Add the candidate in the dictionay if the name is not present
        else:
            distData[row[2]] = 1

#sort the dictionary in descending order. This is the order needed to print in the report
sorted_distData = sorted(distData.items(), key=lambda x: x[1], reverse=True)

#Now generate report

print (f"\nElection Results \n------------------------- \nTotal Votes: {str(vote_count)} \n-------------------------")

#read the dictionary and print the report
idx = 0
for Winner in sorted_distData:
    perCent = float((float(Winner[1])/float(vote_count))*100)
    print (str(Winner[0]) + ": " + str(format(perCent, '.3f')) + "% (" + str(Winner[1]) + ")")
    idx = idx + 1


key_max = max(distData.keys(), key=(lambda k: distData[k]))
print(f"\n------------------------- \n Winner:  {str(key_max)} \n------------------------- \n ")

#write output to a file
with open("Output.txt", "w") as text_file:
    print (f"\nElection Results \n------------------------- \nTotal Votes: {str(vote_count)} \n-------------------------",file=text_file)
    
    idx = 0
    for Winner in sorted_distData:
        perCent = float((float(Winner[1])/float(vote_count))*100)
        print (str(Winner[0]) + ": " + str(format(perCent, '.3f')) + "% (" + str(Winner[1]) + ")", file=text_file)
        idx = idx + 1
    
    
    
    print(f"\n------------------------- \n Winner:  {str(key_max)} \n------------------------- \n ", file=text_file)
