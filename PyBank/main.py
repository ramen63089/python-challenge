import os
import csv
csvpath= os.path.join
rows=[]
csvpath = os.path.join('/Users/rrmenon/Desktop', 'budget_data.csv')
count=0
sum_pl=0
current=0
previous=0
change=0
countdelta=0
sum_delta=0
avg_delta=0
top=0
topdate=""
low=0
lowdate=""
with open(csvpath, newline='') as csvfile:

     # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        print(csvfile)

    # Read the header row first (skip this step if there is now header)
    #what is this?
        csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")

        for row in csvreader:
                if count==0:
                        previous= int(row[1])
                        count=count+1
                        sum_pl= int(row[1])+sum_pl
                        print(row)
                 
                else:
                        count=count+1
                        sum_pl= int(row[1])+sum_pl
                        current= int(row[1])
                        change=current-previous
                        rows.append(change)
                        row.append(change)
                        previous= int(row[1])
                        print(row)
                        if row[2]>top:
                                top=row[2]
                                topdate=row[0]
                        if row[2]<low:
                                low=row[2]
                                lowdate=row[0]
                        
print(str(top))
print(str(topdate))
avg_delta= sum(rows)/len(rows)
print (csvreader)
print ("Financial Analysis")
print ('-'*25)
print (f"Total Months: {count}")
print (f"Total: ${sum_pl}") 
print (f"Average Change: ${avg_delta:.2f}")
print(f"Greatest Increase in profits: {topdate} (${top}) ")
print(f"Greatest ecrease in profits: {lowdate} (${low}) ")

#store contents in variables, lists, and dictionaries