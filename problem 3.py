
import random


class LotteryGame:

  def __init__(self):

    self.winning_numbers = set(random.sample(range(1, 61), 6))

    self.player_numbers = set()

    self.matches = set()

    self.prize = 0



  def input_numbers(self):

    print("Enter your 6 numbers:")

    while len(self.player_numbers) < 6:

      try:

        num = int(input(f"Number {len(self.player_numbers)+1}: "))

        if 1 <= num <= 60:

          self.player_numbers.add(num)

        else:

        print("numbers must be between 1 - 60 only!!")

      except ValueError:

        print("Invalid input. Enter a number.")



  def check_matches(self):

    self.matches = self.player_numbers & self.winning_numbers

    count = len(self.matches)

    if count == 6:

      self.prize = 1_000_000
    else:
      self.prize = count * 1000

  def display_results(self):

    print("\nWinning Numbers:", ", ".join(str(n) for n in sorted(self.winning_numbers)))


    print("Players Numbers 1:  ", ", ".join(str(n) for n in sorted(self.player_numbers)))
    print("Players Numbers 2:  ", ", ".join(str(n) for n in sorted(self.player_numbers))))
    print("Players Numbers 3:  ", ", ".join(str(n) for n in sorted(self.player_numbers))))
    print("Players Numbers 4:  ", ", ".join(str(n) for n in sorted(self.player_numbers))))
    print("Players Numbers 5:  ", ", ".join(str(n) for n in sorted(self.player_numbers))))
    print("Players Numbers 6:  ", ", ".join(str(n) for n in sorted(self.player_numbers))))




    print("Matches:", len(self.matches))

    print("List of the Winners: ")

    print("List of who did not Win.")

    print("Prize: ₱" + format(self.prize, ","))



  def play(self):

    self.input_numbers()

    self.check_matches()

    self.display_results()


# -------- MAIN PROGRAM ----------
game = LotteryGame()

game.play()