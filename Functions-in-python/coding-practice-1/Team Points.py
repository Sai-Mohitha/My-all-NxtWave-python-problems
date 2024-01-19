def calculate_league_points(wins, draws, losses):
    # Complete this function
   print(wins*4+draws*2-losses*1)
        

statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
# Call the calculate_league_points function
calculate_league_points(wins, draws, losses)