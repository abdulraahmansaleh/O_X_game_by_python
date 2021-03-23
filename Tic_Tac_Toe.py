import pygame
import time

pygame.init()
width = 600
height = 600
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TIC TAC TOE')
rgp = (0, 200, 200)
black = (0, 0, 0)
circolor = (0, 0, 200)
screen.fill(rgp)
pygame.draw.line(screen, black, (200, 0), (200, 600), 10)
pygame.draw.line(screen, black, (400, 0), (400, 600), 10)
pygame.draw.line(screen, black, (0, 200), (600, 200), 10)
pygame.draw.line(screen, black, (0, 400), (600, 400), 10)


def mark(row, col, player):
    b[row][col] = player


def is_winning():
    if b[0][0] == b[0][1] and b[0][0] == b[0][2] and b[0][0] != 0:
        return True
    elif b[1][0] == b[1][1] and b[1][0] == b[1][2] and b[1][0] != 0:
        return True
    elif b[2][0] == b[2][1] and b[2][0] == b[2][2] and b[2][0] != 0:
        return True
    elif b[0][0] == b[1][0] and b[0][0] == b[2][0] and b[0][0] != 0:
        return True
    elif b[0][1] == b[1][1] and b[0][1] == b[2][1] and b[0][1] != 0:
        return True
    elif b[0][2] == b[1][2] and b[0][2] == b[2][2] and b[0][2] != 0:
        return True
    elif b[0][0] == b[1][1] and b[0][0] == b[2][2] and b[0][0] != 0:
        return True
    elif b[0][2] == b[1][1] and b[0][0] == b[2][0] and b[0][2] != 0:
        return True
    else:
        return False


def printt(place, playerr):
    if place == 1:
        if playerr == 2:
            pygame.draw.circle(screen, circolor, (100, 100), 70, 10)
        else:
            pygame.draw.line(screen, circolor, (20, 20), (180, 180), 10)
            pygame.draw.line(screen, circolor, (180, 20), (20, 180), 10)
    elif place == 2:
        if playerr == 2:
            pygame.draw.circle(screen, circolor, (300, 100), 70, 10)
        else:
            pygame.draw.line(screen, circolor, (220, 20), (380, 180), 10)
            pygame.draw.line(screen, circolor, (380, 20), (220, 180), 10)
    elif place == 3:
        if playerr == 2:
            pygame.draw.circle(screen, circolor, (500, 100), 70, 10)
        else:
            pygame.draw.line(screen, circolor, (440, 20), (580, 180), 10)
            pygame.draw.line(screen, circolor, (580, 20), (420, 180), 10)
    elif place == 4:
        if playerr == 2:
            pygame.draw.circle(screen, circolor, (100, 300), 70, 10)
        else:
            pygame.draw.line(screen, circolor, (20, 220), (180, 380), 10)
            pygame.draw.line(screen, circolor, (180, 220), (20, 380), 10)
    elif place == 5:
        if playerr == 2:
            pygame.draw.circle(screen, circolor, (300, 300), 70, 10)
        else:
            pygame.draw.line(screen, circolor, (220, 220), (380, 380), 10)
            pygame.draw.line(screen, circolor, (380, 220), (220, 380), 10)
    elif place == 6:
        if playerr == 2:
            pygame.draw.circle(screen, circolor, (500, 300), 70, 10)
        else:
            pygame.draw.line(screen, circolor, (420, 220), (580, 380), 10)
            pygame.draw.line(screen, circolor, (580, 220), (420, 380), 10)
    elif place == 7:
        if playerr == 2:
            pygame.draw.circle(screen, circolor, (100, 500), 70, 10)
        else:
            pygame.draw.line(screen, circolor, (20, 420), (180, 580), 10)
            pygame.draw.line(screen, circolor, (180, 420), (20, 580), 10)
    elif place == 8:
        if playerr == 2:
            pygame.draw.circle(screen, circolor, (300, 500), 70, 10)
        else:
            pygame.draw.line(screen, circolor, (220, 420), (380, 580), 10)
            pygame.draw.line(screen, circolor, (380, 420), (220, 580), 10)
    elif place == 9:
        if playerr == 2:
            pygame.draw.circle(screen, circolor, (500, 500), 70, 10)
        else:
            pygame.draw.line(screen, circolor, (420, 420), (580, 580), 10)
            pygame.draw.line(screen, circolor, (580, 420), (420, 580), 10)


def insert(place, playerr):
    if place == 1:
        if b[0][0] != 0:
            return False
        else:
            mark(0, 0, playerr)
            return True
    elif place == 2:
        if b[0][1] != 0:
            return False
        else:
            mark(0, 1, playerr)
            return True
    elif place == 3:
        if b[0][2] != 0:
            return False
        else:
            mark(0, 2, playerr)
            return True
    elif place == 4:
        if b[1][0] != 0:
            return False
        else:
            mark(1, 0, playerr)
            return True
    elif place == 5:
        if b[1][1] != 0:
            return False
        else:
            mark(1, 1, playerr)
            return True
    elif place == 6:
        if b[1][2] != 0:
            return False
        else:
            mark(1, 2, playerr)
            return True
    elif place == 7:
        if b[2][0] != 0:
            return False
        else:
            mark(2, 0, playerr)
            return True
    elif place == 8:
        if b[2][1] != 0:
            return False
        else:
            mark(2, 1, playerr)
            return True
    elif place == 9:
        if b[2][2] != 0:
            return False
        else:
            mark(2, 2, playerr)
            return True


def mainn():
    rep = 1
    while rep <= 9:
        pygame.event.get()
        pygame.display.update()
        if rep % 2 == 1:
            turn = 1
        else:
            turn = 2
        print('Player', turn)
        place = int(input())
        time.sleep(1.0)
        if insert(place, turn):
            printt(place, turn)
        else:
            print('Enter a valid number')
            rep -= 1
        if is_winning():
            print('Player', turn, ' Win')
            return True
        rep += 1
        if rep == 10:
            print('Tie ,play again')
            time.sleep(111.0)


mainn()
