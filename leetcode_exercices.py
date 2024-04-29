def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

def rps(p1, p2):
  rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
  if rules[p1] == p2:
    return "Player 1 won!"
  elif rules[p2] == p1:
    return "Player 2 won!"
  else:
    return "Draw!"

def rps2(p1, p2):
  rules = {"rock": 0, "paper": 1, "scissors": 2}
  results = ["Draw!", "Player 1 won!", "Player 2 won!"]
  return results[ rules[p1] - rules[p2]]