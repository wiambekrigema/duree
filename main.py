from duree import Duree

time = Duree(1, 30, 45)

print("Durée initiale:", time.affichage_duree())


secondes = time.conver_secondes()
print("Nombre total de secondes:", secondes)

total = time.add_secondes(200)
print("Durée finale aprés avoir rajouter 200 secondes est:", total)
