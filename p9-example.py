import poker

def decide(cards, money, raises):
  # feel free to change the existing values if you want your model to have a bias
  call_weight = 2
  raise_weight = 0
  fold_weight = 0

  highest = poker.get_highest(poker.check(cards))[0]  

  # example of how to use highest
  if highest == "2" or highest == "highest":
    fold_weight += 4

  # LOOP TO LOOK AT IF YOU WANT TO CHECK EVERY CARD
  # this bit goes through all the cards as stated in the instructions file
  for index, card in enumerate(cards):
    if index < 2:
      # THIS IS A PRIVATE CARD
      card.rank # use this to access the current card's rank as a number 0-12
      card.rank_literal # use this to access the current card's rank as a string
    else:
      # THIS IS A PUBLIC/COMMUNITY CARD
      card.suit # use this to access the current card's suit as a string

  # remember, keep this as-is (and leave it as the last line)
  return poker.perform_decision(call_weight, raise_weight, fold_weight)