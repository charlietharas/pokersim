# Instructions  

You are only allowed to touch `p1.py`, `p2.py`, `p3.py`, `p4.py`. These represent the 4 players in our game. *Edit the first file to change your model*, but feel free to modify the others if you want to see how your model performs against other strategies.
Currently, each player simply selects a random decision.

There is a `p9-example.py`file with some example code that you can mimic/refer to as you write your "model."

There's no need to run more than 1,000 games to test your code--distributions will be normal past 100 games in the vast majority of cases.

There are several utility functions in `poker.py` that are used to run the game. I am not explicitly banning them, however, I will refuse to explain them and *it would be a better use of your time to ignore that file*--it is quite complex and somewhat poorly written. **It is imperative that you do not modify `poker.py` or `game.py`, as you may break the simulation!**
- One hint: if you want to get the current *type* of best possible combination you can use: `poker.get_highest(poker.check(cards)))[0]`
  - This will return a String, possible values: ["royal flush", "straight flush", "4", "full house", "straight", "flush", "3", "2 pairs", "2", "highest"]
  - Just pretend this (entire statement) is a variable, and treat it like one (or set a variable to this value early-on)

### You are given the following information:
- `cards`: list of cards in your hand, the first two are your unique/secret cards, the rest of which are publicly available to all players
  - Access an item in cards with `cards[index]`, access the amount of cards with `len(cards)`
    - Recall that computers start counting at 0, so the first  item is index 0, second is 1, etc.
  - Each item in `cards` has a `rank` and a `suit`, access this information with `x.rank` or `x.suit`
    - e.g. `cards[index].rank` *or* `x = cards[index]`, `x.rank`
  - Rank is an integer, *higher rank is better*, compare them like numbers, ranks correspond to indices in this list: ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  - Suits are Strings, you should only need to check for equality
  - Access the String version of the rank via calling `x.rank_literal`
  - Print out the contents of cards in String form via calling `print(poker.hand_str(cards))`
  - Go through all of the cards with a loop `for c, i in enumerate(cards):`
    - `i` is each card in order as you go through the list (here, you can call `i.rank`, etc.)
    - `c` is the position of each card in the list (useful if you want to know if it is a private or "community" card), for private cards `c` will be less than 2
- `money`: integer showing how much money you have left in the bank
  - Each round costs $5 to enter
  - Each raise costs $5
  - You may wish to play more conservatively if you have low funds
- `raises`: integer showing the amount of players before you that have called for a raise
  - Use this value to tell how confident players are in their hands (unless they're bluffing...)
  - If `raises`=2, two distinct players have called for a raise, and you now have to pay 2*$5=$10 to stay in the round
  - You do not know your position relative to other players (e.g. whether you are first or last)
  - Positions are shuffled every game to ensure fairness
  
- You do not know the round number, but you can determine it via the amount of cards in your hand
  - There are other factors you may be able to determine in this way

### You must adjust the weights given in `p1.py`
- **Leave the `return` statement as given, as the last line in your method**
- If your `call_weight` is highest, you are most likely to call! In that case, you will be forced to pay `raises*5` to remain in the round. You have a shot at winning the game!
- If your `raise_weight` is highest, you are most likely to raise! In that case, you will be forced to pay `(raises+1)*5` to remain in the round, and all players after you will be forced to pay a minimum of this amount as well (potentially more if others raise). You have a shot of winning it all!
- If your `fold_weight` is highest, you are most likely to fold! In that case, you will pay $0, but you will no longer be able to play for the rest of the game, and are ineligible to win. This option guarantees a loss of money--but is it the lesser of several evils?
- The computer randomly selects between your weights, so their relative sizes determine the chance that each option is selected.
- The game will actually let you bet more than you have, but if you don't have more than $0 by the end of the round, you are removed from the game

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
