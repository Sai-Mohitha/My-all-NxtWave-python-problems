def get_scores(ball_and_score_list):
    ball_score_dict={}
    for item in ball_score_list:
        pair=item.split(":")
        key,value=pair[0],int(pair[1])
        if key in ball_score_dict:
            score=ball_score_dict[key]
            ball_score_dict[key]=score+value
        else:
            ball_score_dict[key]=value
    return ball_score_dict        

ball_score_list=input().split(",")
ball_score_pairs=get_scores(ball_score_list)
ball_score_items=ball_score_pairs.items()
ball_score_items=sorted(ball_score_items)
print(ball_score_items)
'''
Question: Grouping of Scores
A player has collected few colored balls which have a number on them. To calculate the score, we have to group the colored balls picked by the user and sum up the numbers on them. Write a program to create a dictionary, grouping of colored balls and the corresponding total score.

Input: The input will be a single line containing comma-separated key-value pairs. Each key-value pair is separated by the colon character (:).

Output: The output should be a single line containing a list of tuples of dictionary items by grouping of colored balls and the corresponding total score, where keys are sorted in alphabetical order.

Example: If the given string is "r:1,b:2,r:3", as the key 'r' is repeated twice, the key 'r' in the output dictionary should have the value of sum of two scores(1 + 3) in the input. So the output should be [('b', 2), ('r', 4)].

'''