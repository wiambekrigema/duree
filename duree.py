class Duree:
  def __init__(self, hours=0, minutes=0, secondes=0 ):
         self.hours = max(0,hours)
         self.minutes = max(0,minutes)
         self.secondes = max(0,secondes)
         self.minutes += self.secondes // 60
         self.secondes = self.secondes % 60
         self.hours += self.minutes // 60
         self.minutes %= 60


  def __str__(self):
         return self.hours + "h " + self.minutes + "m " + self.secondes + "s "

  def affichage_duree(self):
      return "{}h {:02d}m {:02d}s".format(self.hours, self.minutes, self.secondes )

  def conver_secondes(self):
      return self.hours * 3600 + self.minutes * 60 + self.secondes

  def add_secondes(self, nb_secondes):
     total = self.conver_secondes() + nb_secondes
     return  total


duree = Duree(3, 30, 45)
duree.add_secondes(200)
print(duree.affichage_duree())
