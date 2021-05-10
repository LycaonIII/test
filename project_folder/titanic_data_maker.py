import titanic_class
from titanic_class import Passenger

file1 = open('gender_submission.csv', 'r')
file2 = open('test.csv', 'r')

passenger_data = [] # Initalisation du tableau de données
ind = -1
for ligne in file1:
    if ind == -1:
        ind += 1
    else :
        list = ligne.split(',') # Transformation d'une ligne de texte en liste d'éléments
        A = Passenger(list[0]) # Création du nouveau passager
        A.add_survived(list[1]) # A-t-il survécu?
        passenger_data.append(A) # Ajout du passager au tableau de données
        ind += 1

ind = -1
for ligne in file2:
    if ind == -1:
        ind += 1
    else :
        list = ligne.split(',') # Transformation d'une ligne de texte en liste d'éléments
        B = passenger_data[ind]
        B.add_pclass(list[1])
        B.add_sex(list[4])
        B.add_age(list[5])
        B.add_ticket_price(list[9])
        passenger_data[ind] = B
        ind += 1
        print(B.get_infos())

file1.close()