Games = [
    
    {"title": "Elden Ring", "genre": "Action RPG", "age": 16, "publisher": "FromSoftware", "mood": "Challenging"},
    {"title": "Half-Life 2", "genre": "FPS", "age": 16, "publisher": "Valve", "mood": "Immersive"},
    {"title": "Phasmophobia", "genre": "Horror", "age": 16, "publisher": "Kinetic Games", "mood": "Scary"},
    {"titl7xd y7gue": "Minecraft", "genre": "Sandbox", "age": 7, "publisher": "Mojang", "mood": "Creative"},
    {"title": "The Witcher 3: Wild Hunt", "genre": "RPG", "age": 18, "publisher": "CD Projekt", "mood": "Epic"},
    {"title": "Call of Duty: Modern Warfare", "genre": "FPS", "age": 18, "publisher": "Activision", "mood": "Intense"},
    {"title": "Stardew Valley", "genre": "Simulation", "age": 7, "publisher": "ConcernedApe", "mood": "Relaxing"},
    {"title": "Grand Theft Auto V", "genre": "Open World", "age": 18, "publisher": "Rockstar Games", "mood": "Chaotic"},
    {"title": "Celeste", "genre": "Platformer", "age": 7, "publisher": "Matt Makes Games", "mood": "Emotional"},
    {"title": "League of Legends", "genre": "MOBA", "age": 12, "publisher": "Riot Games", "mood": "Competitive"},
    {"title": "Hades", "genre": "Roguelike", "age": 12, "publisher": "Supergiant Games", "mood": "Fast-paced"},
    {"title": "Among Us", "genre": "Party", "age": 7, "publisher": "Innersloth", "mood": "Suspicious"},
    {"title": "Cyberpunk 2077", "genre": "RPG", "age": 18, "publisher": "CD Projekt", "mood": "Futuristic"},
    {"title": "Animal Crossing: New Horizons", "genre": "Simulation", "age": 3, "publisher": "Nintendo", "mood": "Relaxing"},
    {"title": "Doom Eternal", "genre": "FPS", "age": 18, "publisher": "id Software", "mood": "Intense"},
    {"title": "Outer Wilds", "genre": "Adventure", "age": 10, "publisher": "Annapurna", "mood": "Mysterious"},
    {"title": "It Takes Two", "genre": "Platformer", "age": 12, "publisher": "EA", "mood": "Cooperative"},
    {"title": "Resident Evil Village", "genre": "Horror", "age": 18, "publisher": "Capcom", "mood": "Scary"},
    {"title": "Forza Horizon 5", "genre": "Racing", "age": 3, "publisher": "Xbox Game Studios", "mood": "Adventurous"},
    {"title": "Portal 2", "genre": "Puzzle", "age": 10, "publisher": "Valve", "mood": "Funny"},
    {"title": "Valorant", "genre": "FPS", "age": 16, "publisher": "Riot Games", "mood": "Competitive"},
    {"title": "The Sims 4", "genre": "Simulation", "age": 12, "publisher": "EA", "mood": "Creative"}
]

#frågar anväden för genre och gör den lowercase
genre = input("Vilken genre gillar du? ").lower()

#samma grej fast med mood
mood = input("Vilken stämning vill du ha? ").lower()

#gör variablen reccomendations och ger den value 0
recommendations = 0

#oanvänt kod, igga
best_score = 0
best_game = ""
#------------------

#loopar igenom games 
for game in Games:
    score = 0 #skapar variablen score och ger den value 0

    if game["genre"].lower() == genre: 
        score += 2 #boosta scoren på rätt genre med 2 poäng

    if game["mood"].lower() == mood:
        score += 1 #boosta scoren på rätt mood med 1 poäng

    if score >= 2: # om score är större eller lika stor som 2 
        print("Vi rekommenderar:", game["title"]) #visa best game så variablen
        recommendations += 1 #räkna 1 reccomendation

    if recommendations == 3: #när användaren har fått 3 reccomendations då bryt loopen
        break
