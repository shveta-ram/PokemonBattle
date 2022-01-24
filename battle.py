import random
import time
playerPokemon = "Turtwig"
playerType = "Grass"
playerWeakness = ["Fire", "Ice", "Normal"]
playerMoves = ["Tackle", "Razor Leaf", "Body Slam"]
playerMoveType = ["Normal", "Grass", "Normal"]
playerMoveStart = [3, 5, 5]
playerMoveStop = [6, 8, 8]

compPokemon = "Chimchar"
compType = "Fire"
compWeakness = ["Water", "Rock", "Normal"]
compMoves = ["Tackle", "Ember", "Grass Knot"]
compMoveType = ["Normal", "Fire", "Grass"]
compMoveStart = [3, 5, 5]
compMoveStop = [6, 8, 8]

compHP = 20
playerHP = 20

def playerTurn(compHP, playerHP):
    while compHP or playerHP > 0:
        playerMoveAndType = list(zip(playerMoves, playerMoveType))

        print("What will", playerPokemon, "do?")
        moveInput = input("Enter a move: ")
        if moveInput in playerMoves:
            moveChosen = playerMoves.index(moveInput)
        moveInfo = [(x, y) for x, y in playerMoveAndType if x == moveInput]
        if moveInfo[0][1] in compWeakness:  # the move chosen is ineffective towards that type
            hpLoss = random.randrange(playerMoveStart[moveChosen], playerMoveStop[moveChosen] + 1)

        else:
            playerMoveStart[moveChosen] = playerMoveStart[moveChosen] - 3
            playerMoveStop[moveChosen] = playerMoveStop[moveChosen] - 3
            hpLoss = random.randrange(playerMoveStart[moveChosen], playerMoveStop[moveChosen] + 1)
        print("HP LOST:", hpLoss)
        if hpLoss in range(playerMoveStart[moveChosen],
                           int((playerMoveStart[moveChosen] + playerMoveStop[moveChosen]) / 2)):
            print("That was not effective...")
        elif hpLoss == playerMoveStop[moveChosen]:
            print("That was a critical hit!")
        else:
            print("That was super effective!")
        print(compPokemon, ":")
        compHP = compHP - hpLoss
        print(compHP)
        if compHP > 0:
            print("|", compHP * '-', (20 - compHP) * ' ', "|", sep='')
        elif compHP <= 0:
            print("|", 20 * ' ', "|", sep='')
            print("won")
            break

        time.sleep(2)

        compMoveAndType = list(zip(compMoves, compMoveType))
        compAttack = [(x, y) for x, y in compMoveAndType if y in playerWeakness]
        compAttack = random.choice(compAttack)
        moveChosen = compMoves.index(compAttack[0])
        print(compPokemon, "used", compAttack[0], "!")
        hpLoss = random.randrange(compMoveStart[moveChosen], compMoveStop[moveChosen] + 1)

        print("HP LOST:", hpLoss)
        print(playerPokemon, ":")
        playerHP = playerHP - hpLoss
        print(playerHP)
        if playerHP > 0:
            print("|", playerHP * '-', (20-playerHP) * ' ', "|", sep='')
        elif playerHP <= 0:
            print("|", 20 * ' ', "|", sep='')
            print("defeated")
            break

        if hpLoss == range(compMoveStart[moveChosen], int((compMoveStart[moveChosen] + playerMoveStop[moveChosen]) / 2)):
            print("That was not effective...")
        elif hpLoss == compMoveStop[moveChosen]:
            print("That was a critical hit!")
        else:
            print("That was super effective!")

playerTurn(20, 20)