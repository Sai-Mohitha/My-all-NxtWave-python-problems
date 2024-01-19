from itertools import combinations
sentence=sorted(input().split())
lenght=len(sentence)
for i in range(1,lenght+1):
    words=combinations(sentence,i)
    words=set(sorted(words))
    for j in list(sorted(words)):
        print(*j)
        
        
'''
input:
apple is a fruit

output:
a
apple
fruit
is
a apple
a fruit
a is
apple fruit
apple is
fruit is
a apple fruit
a apple is
a fruit is
apple fruit is
a apple fruit is

Question: All Possible Subsets
Given a sentence as input, print all the unique combinations of the words of the sentence, considering different possible number of words each time (from one word to N unique words in lexicographical order).

Approach
Read the input sentence and split it into words.
Define a function to find all unique combinations of words.
Print the unique combinations in lexicographical order.
Step-by-Step Explanation
Step 1: Read the input sentence

Read the input sentence using the input() function.
Split the sentence into words using the split() function.
PYTHON
Step 2: Define the function to find all unique combinations

Create a function called all_unique_combinations that takes two arguments: words and n.
Sort the words in lexicographical order using the sorted() function.
Initialize two lists: old_combinations and new_combinations.
Use a loop to iterate through the range of n.
For each iteration, create a new list called new_combinations.
For each combination in old_combinations, iterate through the items in the words list.
If the combination is empty or the current item is greater than the last item in the combination, append the item to the combination.
Update the old_combinations list with the new_combinations list.
Create a list called word_combinations to store the final word combinations.
For each combination in new_combinations, create a list called word_combination.
For each index in the combination, append the corresponding word from the words list to the word_combination list.
Add the word_combination tuple to the word_combinations list.
Return the sorted set of word_combinations.
 
PYTHON
Step 3: Print the unique combinations

Use a loop to iterate through the range from 1 to the length of the words list plus 1.
For each iteration, call the all_unique_combinations function with the words list and the current iteration value.
For each combination in the returned list, print the combination as a string using the join() function.


'''        