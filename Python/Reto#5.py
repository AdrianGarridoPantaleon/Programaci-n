def ganador(plays: list):
    resultado = {"Player1": 0, "Player2": 0}

    for play in plays:
        p1, p2 = play

        if ((p1 == "piedra" and (p2 == "tijera"))
            or (p1 == "papel" and (p2 == "piedra"))
                or (p1 == "tijera" and (p2 == "papel"))):
            resultado["Player1"] += 1
        elif p1!=p2:
            resultado["Player2"] += 1
    
    if resultado["Player1"]<resultado["Player2"]:
        print("Ganador Player2")
    elif resultado["Player1"]>resultado["Player2"]:
        print("Ganador Player1")
    else:
        print("empate")
   
ganador({("papel", "tijera"), ("tijera", "papel"), ("piedra", "tijera"), ("tijera", "papel")})
