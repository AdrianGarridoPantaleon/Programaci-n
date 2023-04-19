from enum import Enum


class Player(Enum):
    P1 = 1
    P2 = 2


def tenis_game(ponits: list):

    game = ["Love", "15", "30", "40"]
    p1 = 0
    p2 = 0
    finished = False
    error = False

    for player in ponits:
        p1 += 1 if player == Player.P1 else 0
        p2 += 1 if player == Player.P2 else 0

        if p1 >= 3 and p2 >= 3:
            if not finished and abs(p1-p2) <= 1:
                print("Deuce" if p1 == p2 else "Ventaja P1" if p1 >
                      p2 else "Ventaja P2")
            else:
                finished = True
        else:
            if p1 < 4 and p2 < 4:
                print(f"{game[p1]} - {game[p2]}")
            else:
                finished = True

    print("Los puntos jugados no son correctos" if error or not finished else
          "Ha ganado el P1" if p1 > p2 else "Ha ganado el P2")


tenis_game([Player.P1, Player.P1, Player.P2, Player.P2,
           Player.P1, Player.P2, Player.P1, Player.P1])

