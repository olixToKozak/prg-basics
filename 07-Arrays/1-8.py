computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
sorted_games=sorted(computer_games)
count = 0
number=0
while count < len(computer_games):
    count +=1
    print(number+1, sorted_games[number])
    number+=1
    
    