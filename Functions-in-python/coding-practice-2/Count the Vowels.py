def count_the_vowels(word):
    # Complete this function
    vowels = ("a","e","i","o","u")
    
    count=0
    for each in word:
        if (each)==vowels:
            count+=1 
            print(count)        
            

word = input()
# Call the count_the_vowels function
count_the_vowels(word)