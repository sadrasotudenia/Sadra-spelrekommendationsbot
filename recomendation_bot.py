# Lista med spel och deras egenskaper
games = [
    {"title": "Elden Ring", "genre": "Action RPG", "age": 16, "publisher": "FromSoftware", "mood": "Challenging"},
    {"title": "Half-Life 2", "genre": "FPS", "age": 16, "publisher": "Valve", "mood": "Immersive"},
    {"title": "Phasmophobia", "genre": "Horror", "age": 16, "publisher": "Kinetic Games", "mood": "Scary"},
    {"title": "Minecraft", "genre": "Sandbox", "age": 7, "publisher": "Mojang", "mood": "Creative"},
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

# Sparar genrer som användaren tidigare har gillat
liked_genres = []


def get_input(question):
    """
    Tar emot användarens input.
    Om användaren skriver quit eller exit avslutas programmet.
    """

    answer = input(question).lower()

    if answer in ["quit", "exit"]:
        print("Programmet avslutas.")
        quit()

    return answer


# Huvudloop som körs tills användaren väljer att avsluta programmet
while True:

    print("\n--- Spelrekommendationer ---")

    genre = get_input("Vilken genre gillar du? ")
    mood = get_input("Vilken stämning vill du ha? ")

    recommendations = []

    # Går igenom alla spel i listan
    for game in games:

        score = 0

        # Matchande genre ger 2 poäng
        if game["genre"].lower() == genre:
            score += 2

        # Matchande stämning ger 1 poäng
        if game["mood"].lower() == mood:
            score += 1

        # Om användaren tidigare gillat samma genre
        # får spelet extra poäng
        if game["genre"] in liked_genres:
            score += 3

        # Om spelet fått minst 2 poäng rekommenderas det
        if score >= 2:
            recommendations.append(game)

    print("\nVi rekommenderar:")

    # Visar max 3 rekommendationer
    for game in recommendations[:3]:
        print("-", game["title"])

    # Om inga spel hittades
    if len(recommendations) == 0:
        print("Tyvärr hittades inga spel som matchar dina önskemål.")

    # Feedback från användaren
    feedback = get_input(
        "\nVar någon av rekommendationerna bra? (ja/nej) "
    )

    # Om användaren svarar ja
    # sparas genren från första rekommendationen
    if feedback == "ja" and len(recommendations) > 0:

        liked_genre = recommendations[0]["genre"]

        if liked_genre not in liked_genres:
            liked_genres.append(liked_genre)

        print("Tack! Jag kommer ta hänsyn till detta nästa gång.")