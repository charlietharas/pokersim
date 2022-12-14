# this class handles most functions relevant to actual game simulation

import poker
from random import shuffle
import p1
import p2
import p3
import p4

# master lists determining ranking of rankings, combinations
master_ranks = poker.master_ranks
master_suits = poker.master_suits
master_results = [
  "royal flush", "straight flush", "4", "full house", "straight", "flush", "3",
  "2 pairs", "2", "highest"
]
master_results = list(reversed(master_results))

# maps player decide functions
def decide1(cards, money, raises):
  return p1.decide(cards, money, raises)

def decide2(cards, money, raises):
  return p2.decide(cards, money, raises)

def decide3(cards, money, raises):
  return p3.decide(cards, money, raises)

def decide4(cards, money, raises):
  return p4.decide(cards, money, raises)

# defines attributes and actions of a player
class Player:
  def __init__(self, ID, decision, money=100):
    self.ID = ID
    self.decision = decision
    self.money = money
    self.playing = True
    self.cards = []

  def decide(self, r):
    if self.is_playing == False:
      return 2
    else:
      x = self.decision(self.cards, self.money, r)
    if x == 2:
      self.cancel_decision()
      return x
    else:
      self.update_money(-5)
      if x == 1:
        self.update_money((r+1)*-5)
        return x
      if x == 0:
       return x
      print("ERR", x)
      return x

  def reset_cards(self):
    self.cards = []

  def add_card(self, card):
    self.cards.append(card)

  def update_money(self, amount):
    self.money += amount

  def cancel_decision(self):
    self.playing = False

  def force_playing(self):
    self.playing = True

  def is_playing(self):
    return self.playing

  def get_ID(self):
    return self.ID

  def get_cards(self):
    return self.cards

  def get_money(self):
    return self.money

# runs a round within a game, taking in and returning a list of altered Player objects
def real_round(players):
  deck = poker.deck.copy()
  shuffle(deck)
  for j in range(len(players)):
    players[j].update_money(-5)
    players[j].force_playing()
    players[j].reset_cards()

  for i in range(2):
    for j in range(len(players)):
      players[j].add_card(deck.pop(0))

  pool = 5 * len(players)

  players, pool = make_decisions(players, pool)
  
  if check_in(players) == 0:
    return players
  elif check_in(players) == 1:
    for i in range(len(players)):
      if players[i].is_playing():
        players[i].update_money(pool)
    return players
  
  flop = (deck.pop(0), deck.pop(0), deck.pop(0))
  for i in flop:
    for j in range(len(players)):
      players[j].add_card(i)

  players, pool = make_decisions(players, pool)

  if check_in(players) == 0:
    return players
  elif check_in(players) == 1:
    for i in range(len(players)):
      if players[i].is_playing():
        players[i].update_money(pool)
    return players

  turn = deck.pop(0)
  for j in range(len(players)):
    players[j].add_card(turn)

  players, pool = make_decisions(players, pool)

  if check_in(players) == 0:
    return players
  elif check_in(players) == 1:
    for i in range(len(players)):
      if players[i].is_playing():
        players[i].update_money(pool)
    return players

  river = deck.pop(0)
  for j in range(len(players)):
    players[j].add_card(river)
  
  standings = {}
  max_standing = -2

  for i in players:
    if i.is_playing() == False:
      standings[i.get_ID()] = -100
    else:
      x = master_results.index(
        poker.get_highest(poker.check(i.get_cards()))[0])
      standings[i.get_ID()] = x
      if x >= max_standing:
        winner_id = i.get_ID()
        max_standing = x
  
  if list(standings.values()).count(max_standing) > 1:
    highest_card_winners = []
    highest_card = -2
    for i in players:
      if standings[i.get_ID()] < max_standing:
        continue
      else:
        c = max([x.rank for x in i.get_cards()])
        if c >= highest_card:
          highest_card = c
          highest_card_winners.append(i.get_ID())
    for i in range(len(players)):
      if players[i].get_ID() in highest_card_winners:
        players[i].update_money(round(pool / len(highest_card_winners)))
  else:
    for i in range(len(players)):
      if players[i].get_ID() == winner_id:
        players[i].update_money(pool)
  return players

# updates prize pool and players with decisions
def make_decisions(players, pool):
  r = 0
  for i in range(len(players)):
    a = players[i].decide(r)
    if a == 1:
      r += 1
    if a < 2:
      pool += r*5
  return players, pool

# runs a number of rounds until one player remains, no wins counted for draws, alters a dictionary of winners with total win data
def game(winners):
  players = [
    Player(list(winners.keys())[0], decide1),
    Player(list(winners.keys())[1], decide2),
    Player(list(winners.keys())[2], decide3),
    Player(list(winners.keys())[3], decide4)
  ]
  shuffle(players)
  while (len(players)) > 1:
    players = real_round(players)
    players = [i if i.get_money() > 0 else None for i in players]
    players = list(filter(None, players))
  if len(players) > 0:
    winners[players[0].get_ID()] += 1

def check_in(players):
  x = 0
  for i in players:
    x += 1 if i.is_playing() else 0
  return x