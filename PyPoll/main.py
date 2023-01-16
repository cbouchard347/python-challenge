import csv #Import csv module

with open('PyPoll/Resources/election_data.csv') as csvfile: 
    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 

    #Prepare variables
    voterids=[] 
    counties=[] 
    candidates=[] 
    candidatenames=[] 
    totaleachcan=[] 
    resultprintcan=[] 
    totaleachcanperc=[] 

    #Set start conditions
    line_count=0
    winnervotes=0
    loservotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
    #Write data into assigned lists
    for row in csvreader:
        voterids.append(row[0]) #Assign column 0 as voterid and add next line to list voterids
        counties.append(row[1]) #Assign column 1 as county and add next line to list counties
        candidates.append(row[2]) #Assign column 2 as candidate and add next line to list candidates
    
    line_count= len(voterids) #Count the total number of votes cast in the "Voter ID" column

candidatenames.append(candidates[0])

#First loop is through the list of candidates to determine candidates voted for
for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidatenames:
        candidatenames.append(candidates[loop1+1])

n=len(candidatenames)

#Second loop variable loop2 as loop index counter
for loop2 in range (n): 
    totaleachcan.append(candidates.count(candidatenames[loop2])) #Count total votes of candidates and add to list total

#Third loop variable loop3 as loop index counter
loservotes=line_count

for loop3 in range(n): #Range of loop depending on how many candidates were found
    totaleachcanperc.append(f'{round((totaleachcan[loop3]/line_count*100), 4)}%') #Calculate % per candidate found
    if totaleachcan[loop3]>winnervotes: #Find candidate with highest vote count
        winner=candidatenames[loop3]
        winnervotes=totaleachcan[loop3]

#Fourth loop variable loop4 as loop index counter
for loop4 in range(n):
    resultprintcan.append(f'{candidatenames[loop4]}: {totaleachcanperc[loop4]} ({totaleachcan[loop4]})')

#Prepare new combined list of results
resultlines='\n'.join(resultprintcan) 

#Generate output 
analysis=f'\
Election Results\n\
----------------------\n\
Total Votes: {line_count}\n\
----------------------\n\
{resultlines}\n\
----------------------\n\
Winner: {winner}! :)\n\
----------------------\n'

print(analysis) #Output results 
#Write into text file 
file1=open("pypoll.txt","w") #Open/create file named pypoll.txt
file1.writelines(analysis) #Write analysis into pypoll.txt
file1.close() #Close pypoll.txt 

