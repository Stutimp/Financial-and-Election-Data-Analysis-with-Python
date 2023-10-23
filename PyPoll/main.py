import os
import csv

# Path to collect data from the Resources folder and to the file

path_to_csv = os.path.join('Resources', 'election_data.csv')

#Intializing some variables to keep track of our datapoints

total_votes = 0
candidates_list = []
vote_count = {}
#winner = " "


# Open the csv file using open() and reading through "csv_reader"
with open(path_to_csv, 'r') as file:

     #store the data inside a variable called "election_data"

    election_data = csv.reader(file)

    #Print the contents of the file and printing the headers
   # print(election_data)

    header =next(election_data)
    
    #Process the next row of data and initializing the variables
    for row in election_data:
        total_votes += 1
        candidate  = row[2]

        if candidate not in candidates_list:
            candidates_list.append(candidate)
            vote_count[candidate] = 1
        else:
            vote_count[candidate] += 1


    #calculate the percentage of votes for each candidate using list comprehension method

    percentages = {candidate: (vote_count[candidate]/total_votes *100) for candidate in candidates_list}
    #print(total_votes)

    #Finding the winning candidate
    winner = max(vote_count, key = vote_count.get)


    #Printing the results to the terminal
    print("Election Results\n")
    print("-------------------------------------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print("--------------------------------------------------------\n")
      
    for candidate in candidates_list:
        print(f"{candidate}: {percentages[candidate]:.3f}% ({vote_count[candidate]})\n")               
    print("---------------------------------------------------------\n")
    print(f"Winner: {winner}: \n")
    print("----------------------------------------------------------\n")



# Exporting the results inside the "analysis folder" as a text file
output_file = os.path.join("analysis","Pypoll_Analysis.txt")
with open(output_file,"w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("---------------------------------------------\n")   
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("----------------------------------------------\n")

    for candidate in candidates_list:
      txt_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({vote_count[candidate]})\n")
    txt_file.write("--------------------------------------------------------------------\n")
    txt_file.write(f"Winner: {winner}: \n")
    txt_file.write("----------------------------------------------------------\n")






#print the contents of the text file


