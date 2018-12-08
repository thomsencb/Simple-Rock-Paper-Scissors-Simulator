
player_wins = []
comp_wins = []
def add_point(player):
    if player.lower() == "player":
        player_wins.append(1)
    else:
        comp_wins.append(1)

    print("Player wins:", len(player_wins))
    print("Oppenent wins:", len(comp_wins))
