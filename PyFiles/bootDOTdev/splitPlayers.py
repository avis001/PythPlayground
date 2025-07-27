def split_players_into_teams(players):
    oddPlayers = []
    evenPlayer = []

    for index, player in enumerate(players):
        if index % 2 == 0:
            evenPlayer.append(player)
        else:
            oddPlayers.append(player)

    return evenPlayer, oddPlayers


def main():
    even, odd = split_players_into_teams(["A", "b", "C", "D"])
    print(even)
    print(odd)


main()
