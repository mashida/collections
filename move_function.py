# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)

def move(player, direction):
    x, y, hp = player
    dir_x, dir_y = direction
    print("x = {}, y = {}, hp = {}, move is ({}:{})". format(x, y, hp, dir_x, dir_y))
    if x + dir_x < 0 or x + dir_x > 9 or y + dir_y < 0 or dir_y + y > 9:
        hp = hp - 5
        print("The wall!")
    else:
        x = x + dir_x
        y = y + dir_y
    print("After move: x = {}, y = {}, hp = {}". format(x, y, hp))
    print("="*10,"\n")
    return x, y, hp

move((1, 1, 10), (-1, 0))

move((0, 1, 10), (-1, 0))

move((0, 9, 5), (0, 1))
