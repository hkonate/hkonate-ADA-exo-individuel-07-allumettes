total_allumettes = 50
playerList = []
def retire_allumettes(nb_a_retire, hombre_total):
    hombre_total -= nb_a_retire
    return hombre_total


total_allumettes = retire_allumettes(3, total_allumettes)
index = 0
nbrOfPlayer = int(input("Combien il y a de joueur ?"))
temp = nbrOfPlayer


while temp > 0:
    playerList.insert(0, "joueur {}".format(temp))
    temp -= 1


while total_allumettes > 0:
    response = 0
    while response < 1 or response > 6:
        response = int(input("Combien d'allumettes voulez-vous retirer {}?:".format(playerList[index])))
    total_allumettes = retire_allumettes(response, total_allumettes)
    if total_allumettes > 0:
        index += 1
        if index > len(playerList)- 1:
            index = 0

print("Victoire du {} !".format(playerList[index]))

