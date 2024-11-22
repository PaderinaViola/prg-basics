computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"]

computer_games_sorted = sorted(computer_games)
for game in range(len(computer_games_sorted)):
    computer_games_sorted[game] = str(game+1) + computer_games_sorted[game]
    print(computer_games_sorted[game])