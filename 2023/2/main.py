# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.

def colors(game):
    separated1=game.split(':')
    separated2=[int(separated1[0]),separated1[1].split(';')]
    separated3=separated2
    result=separated2
    return(result)

def count(colour,game):
    print('checking game for')
    print(colour)
    print(game)
    highest=0
    for dip in game:
        list=dip.split(',')
        for ball in list:
            if colour in ball:
                number=int(ball.split(' ')[1])
                if number>highest:
                    highest=number
    return(highest)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #filename='test'
    filename='input'
    with open(filename) as file:
        games = [line[5:].rstrip() for line in file]
    print(games)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    total=0
    for game in games:
        print(colors(game))
        if count('red',colors(game)[1])<13 and count('green',colors(game)[1])<14 and count('blue',colors(game)[1])<15:
            total=total+colors(game)[0]
    print(total)
    powers=0
    for game in games:
        powers=powers+(count('red',colors(game)[1])*count('green',colors(game)[1])*count('blue',colors(game)[1]))
    print(powers)