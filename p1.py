# THIS IS THE HOME OF YOUR MODEL
import poker

# adjust the weights using the information given
# the return line will enact the action in the game for you
def decide(cards, money, raises):
  call_weight = 0
  raise_weight = 0
  fold_weight = 0
  return poker.perform_decision(call_weight, raise_weight, fold_weight)