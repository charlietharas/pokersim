import game
import itertools
import jesseyang, judeyang, malachibaxter, nathanwertheimer, teddyabularach, joshuarandall, ericaburton, corvuschanoine, madelinelee, sanvisristava, oliverkim, jamespapaelias, kirstenyeung, ruiyutang, nickolasphanchulizde, chloeteoh, juliakraffczyk, emilyrose, jinaanraushan, audreybudabin, nicolettecarrazza, sophiege, gabrielleyoo, eliotflowers, annabelgottlieb

n = int(input("Run how many games per matchup? "))

class_1 = {
  "Jesse Yang" : jesseyang.decide, 
  "Jude Yang" : judeyang.decide,
  "Malachi Baxter" : malachibaxter.decide, 
  "Nathan Wertheimer" : nathanwertheimer.decide,
  "Teddy Abularach" : teddyabularach.decide,
  "Joshua Randall" : joshuarandall.decide,
  "Erica Burton" : ericaburton.decide,
  "Corvus Chanoine" : corvuschanoine.decide,
  "Madeline Lee" : madelinelee.decide,
  "Sanvi Sristava" : sanvisristava.decide,
  "Oliver Kim" : oliverkim.decide,
  "James Papaelias" : jamespapaelias.decide,
  "Kirsten Yeung" : kirstenyeung.decide,
  "Ruiyu Tang" : ruiyutang.decide,
  "Nickolas Panchulidze" : nickolasphanchulizde.decide,
  "Chloe Teoh" : chloeteoh.decide,
  "Julia Kraffczyk" : juliakraffczyk.decide,
  "Emily Rose" : emilyrose.decide,
  "Jinaan Raushan" : jinaanraushan.decide,
  "Audrey Budabin" : audreybudabin.decide,
  "Nicolette Carrazza" : nicolettecarrazza.decide,
  "Sophie Ge" : sophiege.decide,
  "Gabrielle Yoo" : gabrielleyoo.decide,
  "Eliot Flowers" : eliotflowers.decide,
  "Annabel Gottlieb" : annabelgottlieb.decide,
}

all_winners = {key: 0 for key in class_1.keys()}
for x in itertools.combinations(list(class_1.items()), 4):
  name1, decide1 = x[0][0], x[0][1]
  name2, decide2 = x[1][0], x[1][1]
  name3, decide3 = x[2][0], x[2][1]
  name4, decide4 = x[3][0], x[3][1]
  winners = {name1 : 0, name2 : 0, name3 : 0, name4: 0}
  for i in range(n):
    if i%100 == 0:
      print("Played", i, "games")
      
    game.game(winners, decide1, decide2, decide3, decide4)

  for k, v in winners.items():
    all_winners[k] += v

print(dict(sorted(all_winners.items(), key=lambda item: item[1])))