class Player:
    def __init__(self, name, card):
        self.name = name
        self.card = set(card)
        self.matches = set()
        self.prize = 0

    def check_matches(self, winning_numbers):
        self.matches = self.card & winning_numbers
        self.prize = 1_000_000 if len(self.matches) == 6 else (len(self.matches) * 1000)

    def display_result(self):
        if self.matches:
            match_str = ", ".join(str(n) for n in sorted(self.matches))
            print(f"{self.name}'s card {sorted(self.card)} has {len(self.matches)} matched numbers '{match_str}'. You won {self.prize:,} pesos!")
        else:
            print(f"{self.name}'s card {sorted(self.card)} has no match! No prize.")


class LotteryGame:
    def __init__(self):
        self.winning_numbers = set(random.sample(range(1, 61), 6))
        self.players = []

    def add_player(self):
        name = input("Input your name: ")
        card = set()
        print("Input your 6 numbers (1-60):")
        while len(card) < 6:
            try:
                num = int(input(f"Number {len(card)+1}: "))
                if 1 <= num <= 60:
                    if num not in card:
                        card.add(num)
                    else:
                        print("Number already entered. Try a different number.")
                else:
                    print("Number must be between 1 and 60.")
            except ValueError:
                print("Invalid input. Enter a number.")
        self.players.append(Player(name, card))

    def play(self):
        print("\nWinning numbers:", sorted(self.winning_numbers))
        for player in self.players:
            player.check_matches(self.winning_numbers)
            player.display_result()


# Run the game
game = LotteryGame()
game.add_player()
game.play()
