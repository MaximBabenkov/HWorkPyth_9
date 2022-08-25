import pygame, sys
from functions import*


def button_click():
    draw_lines()
    player = 2
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int(mouseY // 200)
                clicked_col = int(mouseX // 200)

                if available_square(clicked_row, clicked_col):
                    if player == 1:
                        mark_square(clicked_row, clicked_col, 1)
                        if check_win(player):
                            game_over = True
                        player = 2
                    elif player == 2:
                        mark_square(clicked_row, clicked_col, 2)
                        if check_win(player):
                            game_over = True
                        player = 1

                    draw_figures()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart()
                    player = 2
                    game_over = False
            pygame.display.update()
