def addResult(teams,name,result):
    if name in teams:
        L=teams[name]
    else:
        L=[0, 0, 0]
    if result=='win':
        L[0]+=1 
    elif result=='draw':
        L[1]+=1 
    else:
        L[2]+=1 
    teams[name]=L   
        
def calcPoints(name,results):
    points=3*results[0]+results[1]
    return (points,name,results)


def toString(teamRec):
    points,name,results=teamRec
    won,draw,lost=results 
    played=won+lost+draw 
    s=f'Team: {name}, Matches Played: {played}, Won: {won}, Lost: {lost}, Draw: {draw}, Points: {points}'
    return s 
    
n=int(input())
teams={} 

for i in range(n):
    line=input().split(';')
    team1=line[0].strip()
    team2=line[1].strip()
    result=line[2].strip()
    addResult(teams,team1,result)
    if result=='win':
        result='loss'
    elif result=='loss':
        result='win'
    addResult(teams,team2,result)    
    
L = [] 
for name in teams:
    L.append(calcPoints(name,teams[name]))
     
L.sort(reverse=True) 

if L==[]:
    print("No Output")
else:
    for rec in L:
        print(toString(rec))
    
'''
Question: IPL Match Details
Write a program that reads all the match outcomes and summarizes the information of all the matches. Points are given to the teams based on the outcome of the match. A win earns a team 3 points. A draw earns 1. A loss earns 0. The team information should be displayed in descending order of points.

Approach
Read the number of matches played.
Store the outcomes of each match in a dictionary.
Calculate the points for each team based on their match outcomes.
Print the points table in descending order of points.
Step-by-Step Explanation
Step 1: Read the number of matches

Read the input value representing the number of matches played. We can use the input() function to read the input and int() to convert it into an integer.
PYTHON
Step 2: Store match outcomes

Create a function store_game_result that takes the team_stats dictionary as an argument.
Inside the function, read the input for each match and split it into t1, t2, and match_outcome.
Update the team_stats dictionary with the match outcomes for both teams using the update_match_outcome function.
PYTHON
Step 3: Calculate points for each team

Create a function get_points that takes the team_stats dictionary and a team as arguments.
Calculate the points for the given team based on their match outcomes and return the result.
PYTHON
Step 4: Print the points table

Create a function print_points_table that takes the team_points list and the team_stats dictionary as arguments.
Inside the function, iterate through the team_points list and print the team information in the required format.


'''    