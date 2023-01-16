#Import csv module
import csv

with open('Resources/budget_data.csv') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 

    #Prepare variables
    months=[] #Generate list named "months" for the "Date" column
    profitloss=[] #Generate list named "profitlosses" for the "Profit/Losses" column

    #Set start conditions
    total=0
    a_change=0
    delta1=0
    delta2=0
    delta_line1=0
    delta_line2=0

    #Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        months.append(row[0]) #Assign column 0 and add next line to list months
        profitloss.append(row[1]) #Assign column 1 and add next line to list profitlosses
        total=total+int(row[1]) #Calculate total amount
    m_count = len(months) #Count the total of months in the "Date" column 

#Second loop is through list prolosses (variable loop2 as loop index counter)
for loop in range (m_count-1): #Restrict loop to avoid overflow (last line +1)
    a_change=a_change+(float(profitloss[loop+1])-float(profitloss[loop])) #Calculate sum of changes
    m_change=(float(profitloss[loop+1])-float(profitloss[loop])) #Calculate monthly change
    if m_change>delta1: #Determine greatest increase
        delta1=m_change
        delta_line1=loop

    if m_change<delta2: #Determine greatest decrease
        delta2=m_change
        delta_line2=loop

#generate output
analysis=f'\
Financial Analysis\n\
---------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[delta_line1+1]} (${int(delta1)})\n\
Greatest Decrease in Profits: {months[delta_line2+1]} (${int(delta2)})\n'

print(analysis) #Output results

#Write into text file 

file1=open("pybank.txt","w") #Open/create file named pybank.txt
file1.writelines(analysis) #Write analysis 
file1.close() #Close pybank.txt 