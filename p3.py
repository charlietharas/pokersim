import poker

def decide(cards, money, raises):
  call_weight = 0
  raise_weight = 0
  fold_weight = 0
  return poker.perform_decision(call_weight, raise_weight, fold_weight)