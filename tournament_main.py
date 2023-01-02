import game
import itertools

n = int(input("Run how many games per matchup? "))

class_1 = {}

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
