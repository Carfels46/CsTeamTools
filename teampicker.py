import math
import random




def teampicker():
    spelarpool = []
    rad = input("skriv spelarnas namn (sepparerat med ','): ")

    splitad = rad.split(",")
    print("player pool")
    print(' '.join(splitad))
    random.shuffle(splitad)
    team1count = math.floor(len(splitad)//2)

    print("Lag 1:")
    for i in range(int(team1count)):
        print(splitad[i])
    print("Lag 2:")
    q = len(splitad) - team1count
    for x in range(q):
        print(splitad[x+team1count])




teampicker()


