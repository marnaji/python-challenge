#module for defining the path and CSV files
import os
import csv

#define path for the csvfile
csvpath = os.path.join('.' , 'Resources','election_data.csv')

#read csv
with open(csvpath , encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    #create header
    csvheader = next(csvreader)
    #print(f"CSV header:{csvheader}")

    #Variable holds values
    totalVote = 0
    candidateDict = {}
  
    # loop through to calculate total vote and add a candicate to dictionary 
    for row in csvreader:
        
        totalVote += 1
        #define candidate
        candidateName = row[2]
        #dictionary to hold the values of each candidate
        if candidateName in candidateDict:
            candidateDict[candidateName] = candidateDict[candidateName] + 1
        else:
            candidateDict[candidateName] = 1
         
# printing the result in terminal    
print(candidateDict)
print("Election Results")
print("---------------------------")
print(f"TotalVote {totalVote}")
print("---------------------------")
 
maxCount = 0
winner = ""
#loop through the dictionary get the name,value and percentage of vote
for key,value in candidateDict.items():
    percentVote = value/totalVote*100
    percentVote = round(percentVote, 3)
    print(f"{key}: {percentVote}% ({value})") 
    
    #Determine the winner
    if value>maxCount:
        maxCount = value
        winner = key
print("---------------------------")
print(f"Winner: {winner}")


# exporting the result in a text file
output_path = os.path.join(".", "analysis", "result.txt")
with open(output_path, 'w') as textFile:
    textFile.write("Election Results\n")
    textFile.write("------------------------\n")
    textFile.write(f"Total Votes : {totalVote}\n")    
    textFile.write("------------------------\n")
    for key,value in candidateDict.items():
        textFile.write(f"{key}: {percentVote}% ({value})\n")   
    textFile.write("------------------------\n")
    textFile.write(f"winner : {winner}") 
    