def char_to_string(line):
    line=line.lower()
    unique_chars=set(line)
    unique_chars.discard(" ")
    
    for char in sorted(unique_chars):
        print("{}: {}".format(char,line.count(char)))
        
line=input()   
char_to_string(line)

'''
n this Problem, we will explain a solution for the coding question "Character Frequency" using Python. We will break down the given solution into simple steps and explain each step in plain English.
INPUT:
Tic Tac Toe

OUTPUT:
a: 1
c: 2
e: 1
i: 1
o: 1
t: 3

'''