class FlamesGame:
    def __init__(self, name1, name2):
        self.name1 = name1.replace(" ", "").lower()
        self.name2 = name2.replace(" ", "").lower()

    def play(self):
        n1 = list(self.name1)
        n2 = list(self.name2)
      
        for ch in self.name1:
            if ch in n2:
                n1.remove(ch)
                n2.remove(ch)

        total = len(n1) + len(n2)


        print(f"Your name remaining    : {''.join(n1)}")
        print(f"Crush name remaining   : {''.join(n2)}")
        print(f"Count remaining [your name] : {len(n1)}")
        print(f"Count remaining [crush]     : {len(n2)}")
        print(f"Sum                     : {total}")

        if total == 0:
            return "Not compatible! Single forever </3!!"

        flames = list("FLAMES")
        idx = 0
        while len(flames) > 1:
            idx = (idx + total - 1) % len(flames)
            flames.pop(idx)

        mapping = {
            "F": "Friendship",
            "L": "Love",
            "A": "Affection",
            "M": "Marriage",
            "E": "Enemy",
            "S": "Sibling"
        }

        return mapping[flames[0]]



first = input("Your name : ")
second = input("Crush name : ")

game = FlamesGame(first, second)
print(f"\nRelationship           : {game.play()}")
