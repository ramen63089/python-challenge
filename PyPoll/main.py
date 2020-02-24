import os
import csv
import statistics
from statistics import mode 
csvpath= os.path.join

  
csvpath = os.path.join('/Users/rrmenon/Desktop', 'election_data.csv')
votecount=0
sum_pl=0
#variables for count
khan=0
correy=0
li=0
o=0
candidates_list=[]



#variables to store percentages- placed in new list
perkhan=0
percorrey=0
perli=0
pero=0

most_common=""
with open(csvpath, newline='') as csvfile:

     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        votecount= votecount+1
        if row[2]=='Khan':
            khan=khan+1
        elif row[2]=='Correy':
            correy=correy+1
        elif row[2]=='Li':
            li=li+1
        else:
            o=o+1
        candidates_list.append(row[2])

#calculate percentages
perkhan= (khan/votecount)*100
percorrey= (correy/votecount)*100
perli= (li/votecount)*100
pero= (o/votecount)*100

#create list of percentages to cycle through and find winner
perlist= [perkhan, percorrey, perli, pero]

top= perkhan

#Max
for x in perlist:
    if x>top:
        top=x

def most_common(candidates_list): 
    return(mode(candidates_list)) 
most_common= most_common(candidates_list)

#print
print (f"Election Results")
print ('-'*25)
print (f"Total Votes: {votecount}")
print ('-'*25)
print (str(top))
print ('-'*25)

print (f"Khan: {perkhan:.3f}% ({khan})")
print (f"Correy: {percorrey:.3f}% ({correy})") 
print (f"Li: {perli:.3f}% ({li})") 
print (f"O'Tooley:  {pero:.3f}% ({o})")
print ('-'*25)
print(f"Winner: {most_common}") 