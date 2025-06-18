import random

options = ["piedra", "papel", "tijera"]

# player = input("Elige piedra, papel, tijera: ").lower()


while True:
    max_rounds = input("Queres jugar al mejor de 3 o de 5? (3 o 5): ")
    if max_rounds in ["3", "5"]:
        max_rounds = int(max_rounds)
        break
    else: 
        print("Porfavor ingresar 3 o 5 ")
    

player_wins = 0
computer_wins = 0
round = 1

def define_winner(player, computer):
    if player == computer:
        return "empate"
    elif (
        (player == "piedra" and computer == "tijera") or
        (player == "papel" and computer == "piedra") or
        (player == "tijera" and computer == "papel")
    ):
        return "usuario"
    else:
        return "computadora"
    


while player_wins < max_rounds // 2 + 1 and computer_wins < max_rounds // 2 + 1:
    print(f"\n---- Ronda {round} ----")
    player = input("Elegi piedra papel o tijera").lower()

    if player not in options:
        print("Opcion invalida")
        continue

    computer = random.choice(options)
    print(f"La maquina eligio: {computer}")

    result = define_winner(player, computer)

    if result == "empate":
        print("Empate!")

    elif result == "usuario":
        print("Ganaste la ronda")
        player_wins += 1

    else:
        print("Perdiste la ronda")
        computer_wins += 1

    print(f"Puntos -> Vos: {player_wins} | Maquina: {computer_wins}")
    round += 1 

print("\n==== Resultadp final ====")
if player_wins > computer_wins:
    print("Ganaste!!")
else:
    print("La computadora gana")
