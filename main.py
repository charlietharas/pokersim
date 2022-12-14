import game

n = int(input("Run how many games? "))

player_id = "YOUR NAME HERE" # SET THIS TO YOUR NAME
winners = {player_id: 0, "2": 0, "3": 0, "4": 0}
for i in range(n):
  if i%100 == 0:
    print("Played", i, "games")
  game.game(winners)

print("Win counts for", n, "games:")
print(winners)
print("Draws:", n-sum(winners.values()))