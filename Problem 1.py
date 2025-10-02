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

    if total == 0:

      return "Not compatible! Single forever </3!!"


    flames = list("FLAMES")

    idx = 0

    while len(flames) > 1:

      idx = (idx + total - 1) % len(flames)

      flames.pop(idx)


    mapping = {"F": "Friendship", "L": "Love", "A": "Affection",
          "M": "Marriage", "E": "Enemy", "S": "Sibling"}

    return mapping[flames[0]]

CrushName = input("Your Crush Name: ")
print("\nYour Crush Name Remaining              : " )
print("\nCrush Name Remaining                   : " )
print("\nCount Remaining [ Your Name ]          : ", )
print("\nCount Remaining [ Your Crush]          : ", )
print("\nSum                                    : ")
print("\nRelationship                           : ")


game = FlamesGame(first, second)

print("Result:", game.play())