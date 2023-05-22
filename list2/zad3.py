# Ex3 - 8pkt
from list2.CircleCrossGame import CircleCrossGame

game = CircleCrossGame()
isCrossMove = True
result = game.check_result()
while result == 0:
    game.printField()  # print the field

    if isCrossMove:
        print("Cross player move:")
    else:
        print("Circle player move:")

    index = int(input("Please select where to play(indexing from 1 to 9): ").strip()) - 1  # ask where to move - 1!!!
    if index < 0 or index > 8:
        print("Index out of bounds!")
        continue
    if game.field[index] != 0:
        print("This field is already occupied!")
        continue

    # set the move
    if isCrossMove:
        game.set_cross(index)
    else:
        game.set_circle(index)
    # pass the turn
    isCrossMove = not isCrossMove
    result = game.check_result()

# print field and show who won
game.printField()
if result == 1:
    print("---------Cross Wins!---------")
elif result == 2:
    print("---------Circle wins!---------")
else:
    print("---------Draw!---------")
