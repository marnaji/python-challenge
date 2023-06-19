#This will allow us to create file paths across operating systems
import os
#Module for CSV files
import csv

#define the path for the file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#open and read the csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #read the header row first
    header = next(csvreader)
    
    #Defining variables
    totalMonth = 0
    totalAmount = 0    
    previousAmount = None
    totalChange = 0
    minChange = 0
    minDate = ""
    maxChange = 0
    maxDate = ""
    
    # loop through to add the totalAmont and number of the months
    for row in csvreader:
        
        
        currentAmount = int(row[1])
        
        #calculate total months and total amount
        totalMonth = totalMonth + 1
        totalAmount = totalAmount + currentAmount
        #calculate changes of the loss and profit
        if previousAmount is not None:
            currentChange   = currentAmount - previousAmount
            #hold the value of max change and date
            if currentChange>maxChange:
                maxChange = currentChange
                maxDate = row[0]
            #hold the value of man change and date
            if currentChange<minChange:
                minChange = currentChange
                minDate = row[0]    
            
            totalChange = totalChange + currentChange

        previousAmount = currentAmount
        
     
    averageChanges = totalChange / (totalMonth-1)     
    increase= 0


# printing the result in terminal
print("Financial Analysis")
print("------------------------")
print("totalMonth = ", totalMonth)    
print("totalAmount = ", totalAmount)   
print("Changes ", averageChanges) 
print(f"gretest increase in profit: {maxDate} (${maxChange})") 
print(f"gretest decrease in profit  {minDate} (${minChange})") 


# exporting the result in a text file
output_path = os.path.join(".", "analysis", "result.txt")
with open(output_path, 'w') as textFile:
    textFile.write("Financial Analysis\n")
    textFile.write("------------------------\n")
    textFile.write(f"totalMonth : {totalMonth}\n")    
    textFile.write(f"totalAmounSt : {totalAmount}\n")   
    textFile.write(f"Changes : {averageChanges}\n") 
    textFile.write(f"gretest increase in profit : {maxDate} (${maxChange})\n") 
    textFile.write(f"gretest decrease in profit : {minDate} (${minChange})") 
    

