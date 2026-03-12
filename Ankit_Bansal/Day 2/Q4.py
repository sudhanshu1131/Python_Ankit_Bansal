#take a ipl team name as input from user and display a list of all elements from that name.
ipl= ['CSK','MI','KKR','LSG','PBKS']
#team_name = input("Enter an IPL team name: ")

#1st Solution
team_name = input("Enter the IPL team name: ")

team_index= ipl.index(team_name)

print("List of elements from the team name:", ipl[team_index:])

# Check if team exists in the list
if team_name in ipl:
    index = ipl.index(team_name)  # Find index of the team
    result = ipl[index:]     # Slice from that index to the end
    print(result)
else:
    print("Team not found in the list.")
