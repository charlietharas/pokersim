# Instructions  

You are only allowed to touch `p1.py`, `p2.py`, `p3.py`, `p4.py`. These represent the 4 players in our game. The first file should be your custom model, but you may modify the others if you want to see how your model performs against other strategies.
Currently, each player simply selects a random decision.

Running more than 1,000 games is inadvisable it is pointless--distributions will be normal past 100 games in the vast majority of cases.

There are many helpful utility functions in `poker.py`. I am not explicitly banning them, however, I will refuse to explain them and *it would be a better use of your time to ignore that file*--it is quite complex and somewhat poorly written. **It is imperative that you do not modify `poker.py` or `game.py`, as you may break the simulation!**
- Fine, one hint: if you want to get the current *type* of best possible combination you can use: `poker.get_highest(poker.check(cards)))[0]`
  - This will return a String, possible values: ["royal flush", "straight flush", "4", "full house", "straight", "flush", "3", "2 pairs", "2", "highest"]
  - Just pretend this (entire statement) is a variable, and treat it like one (or set a variable to this value early-on)

### You are given the following information:
- `cards`: list of cards, the first two are your unique/secret cards
  - Access an item in cards with `cards[index]`, access the amount of cards with `len(cards)`
  - Each item in `cards` has a `rank` and a `suit`, access this information with `x.rank` or `x.suit`
  - Higher rank is better, ranks correspond to indices in this list: ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  - Access the String version of the rank via calling `x.rank_literal`
  - Print out the contents of cards via calling `print(poker.hand_str(cards))`
- `money`: integer showing how much money you have left in the bank
  - Each round costs $5
  - Each raise costs $5
- `raises`: integer showing the amount of players before you that have called for a raise
  - If `raises`=2, two distinct players have called for a raise, and you now have to pay $10 to stay in the round
  - You do not know your position relative to other players (e.g. whether you are first or last)
  - Positions are shuffled every game to ensure fairness
- You do not know the round number, but you can determine it via the amount of cards in your hand
  - There are other factors you may be able to determine in this way

### You must return an integer: 0, 1, or 2
- 0 indicates a call. You will be forced to pay `raises*5` for this round, and you will remain in the game with the potential to win it all!
- 1 indicates a raise. You will be forced to pay `(raises+1)*5` for this round, and all players after you will be forced to pay a minimum of this amount as well (potentially more if others raise). You have a shot of winning it all!
- 2 indicates a fold. You will pay $0 for this round, but you will no longer be able to play in future games, and are ineligible to win the game. This option guarantees a loss of money--but is it the lesser of many evils?

### Poker combinations for reference:
- Royal Flush: straight flush with Ace highest card, 0.000154%
- Straight Flush: 5 consecutive ranks, same suit, 0.0015%
- 4-of-a-kind: 4 of same rank, 0.0256%
- Full House: one 3-of-a-kind, one pair, 0.17%
- Flush: 5 consecutive ranks, 0.367%
- Straight: 5 of same suit, 0.76%
- 3-of-a-kind: 3 of same rank, 2.87%
- 2 pairs: 2 of same rank 2 distinct times, 7.62%
- Pair: 2 of same rank, 49.9%
- Highest: highest card wins: A>K>Q>J>10>....>2, 50.1%