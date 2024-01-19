first_line=input()
second_line=int(input())

a=first_line[:second_line]
b=first_line[second_line+1:]
result=a+b
print(result)

#Skip the Fourth Character

word=input()
word_lenght=len(word)
a=word[:3]
b=word[4:]
result=a+b
print(result)