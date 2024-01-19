distance=int(input())

first_50_km=(50*3)
second_100_km=(50*5)
next_200_km=(20*6)

bonus_score=100

if (distance)<=50:
    score=distance*3
    
elif(distance)<=100:
   distance_score=(distance-100)
   distance_score_km=(distance_score)*5 
   score=(first_50_km)+(second_100_km)+(distance_score_km)
   
elif(distance)<=200:
   distance_score=(distance-100)
   distance_score_km=(distance_score)*6 
   score=(first_50_km)+(second_100_km)+(distance_score_km)

else:
   distance_score=(distance-100)
   distance_score_km=(distance_score)*10
   score=(distance_score_km)
print(score+bonus_score)
   
     
  
    