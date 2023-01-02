# this class handles most functions relevant to dealing with a deck of cards, utility functions for game

from itertools import combinations
from random import shuffle, randint

# master lists used to determine rankings of rankings
master_ranks = [
  "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"
]
master_suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

# defines attributes of each card
class Card:
  def __init__(self, rank, suit):
    self.rank_literal = rank
    self.rank = master_ranks.index(self.rank_literal)
    self.suit = suit

# initializes a deck of 52 cards for reference
deck = []
for i in master_ranks:
  for j in master_suits:
    deck.append(Card(i, j))

# checks for all possible useful hand combinations within a hand of any size
def check(cards):
  results = {}
  suits = [i.suit for i in cards]

  for i in master_suits:
    if suits.count(i) >= 5:
      results["flush"] = [j if j.suit == i else None for j in cards]
      results["flush"] = list(filter(None, results["flush"]))

  sorted_ranks = sorted(cards, key=lambda i: i.rank, reverse=True)
  count = 0
  consec = []
  for i in range(len(sorted_ranks) - 1):
    if sorted_ranks[i + 1].rank == sorted_ranks[i].rank - 1:
      count += 1
      consec.append(sorted_ranks[i])
    else:
      count = 0
      consec = []
    if count == 4:
      consec.append(sorted_ranks[i + 1])
      results["straight"] = consec
      break

  for i in combinations(cards, 4):
    if i[0].rank == i[1].rank and i[1].rank == i[2].rank and i[2].rank == i[
        3].rank:
      if "4" not in results.keys():
        results["4"] = [i]
      else:
        results["4"].append(i)

  for i in combinations(cards, 3):
    if i[0].rank == i[1].rank and i[1].rank == i[2].rank:
      if "3" not in results.keys():
        results["3"] = [i]
      else:
        results["3"].append(i)

  for i in combinations(cards, 2):
    if i[0].rank == i[1].rank:
      if "2" not in results.keys():
        results["2"] = [i]
      else:
        results["2"].append(i)

  results["highest"] = sorted_ranks[0]

  return results
  
# MISNOMER: returns the deck with the highest card out of any number of decks
def get_highest_card(decks):
  highest_card = -1
  highest_deck = []
  for i in decks:
    for j in i:
      if j.rank > highest_card:
        highest_card = j.rank
        highest_deck = i
  return list(highest_deck)

# returns a string indicating the type of combination, as well as the list of cards within the combination, of the best possible combination given a hand of any size (although it technically breaks with size>7)
def get_highest(results):
  keys = results.keys()
  if "straight" in keys and "flush" in keys:
    for i in results["flush"]:
      if i.rank_literal == "Ace":
        return "royal flush", results["flush"]
    return "straight flush", results["flush"]
  if "4" in keys:
    return "4", get_highest_card(results["4"])
  if "straight" in keys:
    return "straight", results["straight"]
  if "flush" in keys:
    return "flush", results["flush"]
  if "3" in keys:
    for i in results["3"]:
      for j in results["2"]:
        if len(list(set(i).intersection(set(j)))) == 0:
          i = list(i)
          i.append(x for x in j)
          return "full house", i
  if "2" in keys:
    if len(results["2"]) == 1:
      return "2", results["2"][0]
    two_pairs = []
    for i in combinations(results["2"], 2):
      if len(list(set(i[0]).intersection(set(i[1])))) == 0:
        y = list(i[0])
        y.append(i[1][0])
        y.append(i[1][1])
        two_pairs.append(y)
      return "2 pairs", get_highest_card(two_pairs)

    return "2", get_highest_card(results["2"])
  return "highest", results["highest"]

# returns the amount of time each combination is seen from a randomly drawn texas-holdem hand of 7 after n draws
def check_distribution(n):
  results = {}
  shuffled = deck.copy()
  for i in range(n):
    shuffle(shuffled)
    a = shuffled[0:7]
    x = get_highest(check(a))[0]
    if x in results.keys():
      results[x] += 1
    else:
      results[x] = 1

  return results

# returns the amount of draws of texas-holdem hands of 7 it takes before a desired combination x is achieved
def how_many_until(x):
  results = {}
  shuffled = deck.copy()
  n = 0
  while x not in results.keys():
    shuffle(shuffled)
    a = shuffled[0:7]
    results[get_highest(check(a))[0]] = True
    n += 1
    if n % 10000 == 0:
      print("Passed", n, "turns")

  for i in get_highest(check(a))[1]:
    print(i.suit, i.rank_literal)
  return n

def hand_str(hand):
  s = ""
  for i in hand:
    s += i.rank_literal + " " + i.suit + ", "
  return s

def perform_decision(do_call, do_raise, do_fold): 
  x = randint(0, do_call + do_raise + do_fold)
  if x < do_call:
    return 0
  elif x < do_raise:
    return 1
  else:
    return 2