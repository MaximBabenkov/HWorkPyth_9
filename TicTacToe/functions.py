import pygame
import numpy

pygame.init()

width = 600
height = 600
line_width = 15
board_rows = 3
board_cols = 3
circle_radius = 60
circle_width = 15
cross_width = 25
space = 55


red = (255, 0, 0)
bg_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(bg_color)
board = numpy.zeros((board_rows, board_cols))


def draw_lines():
    #1th horizontal line:
    pygame.draw.line(screen, line_color, (0, 200), (600, 200), line_width)
    #2th horizontal line:
    pygame.draw.line(screen, line_color, (0, 400), (600, 400), line_width)
    #1th vertical line:
    pygame.draw.line(screen, line_color, (200, 0), (200, 600), line_width)
    #2th vertical line:
    pygame.draw.line(screen, line_color, (400, 0), (400, 600), line_width)

def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (int(col * 200 + 100), int(row * 200 + 100)), circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color, (col * 200 + space, row * 200 + 200 - space), (col * 200 + 200 - space , row * 200 + space), cross_width  )
                pygame.draw.line(screen, cross_color, (col * 200 + space, row * 200 + space), (col * 200 + 200 - space , row * 200 + 200 - space), cross_width  )

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0
    
def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    #vertical win check
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    #horizontal win check
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    #asc diagonal win check
        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_asc_diagonal(player)
            return True
    #desc diagonal win check
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            draw_desc_diagonal(player)
            return True
    return False    
def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color 
    pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color 
    pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)

def draw_asc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)

def draw_desc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)

def restart():
    screen.fill(bg_color)
    draw_lines()
    player = 2
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0
