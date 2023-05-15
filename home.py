import pygame as pg

from board import Board
from const import *
from game import Game


class Home:
    def __init__(self):
        pg.init()
        # set home screen
        self.home_screen = pg.Surface((SW, SH))
        self.home_screen.fill(WHITE)
        self.home_screenBackground_image = pg.image.load('connect4.png')
        self.home_screen_textT = pg.font.SysFont(FONT_NAME, FONT_VERYLARGE).render('Connect 4', True, BLACK)

        self.home_screen_text_rect = self.home_screen_textT.get_rect(
            center=(SW // 2, SH // 12))
        self.home_screen_text1 = pg.font.SysFont(FONT_NAME, FONT_LARGE).render('Easy', True, BLACK)
        self.home_screen_text_rect1 = self.home_screen_text1.get_rect(
            center=(SW // 2.1, SH // 2.3))
        self.home_screen_text2 = pg.font.SysFont(FONT_NAME, FONT_LARGE).render('Medium', True,
                                                                                     BLACK)
        self.home_screen_text_rect2 = self.home_screen_text2.get_rect(
            center=(SW // 2.1, SH // 1.7))
        self.home_screen_text3 = pg.font.SysFont(FONT_NAME, FONT_LARGE).render('Hard', True, BLACK)
        self.home_screen_text_rect3 = self.home_screen_text3.get_rect(
            center=(SW // 2.1, SH // 1.35))

        self.home_screen_text4 = pg.font.SysFont(FONT_NAME, FONT_LARGE).render('Impossible', True, BLACK)
        self.home_screen_text_rect4 = self.home_screen_text4.get_rect(
            center=(SW // 2.1, SH // 1.12))


    def updateHome(self):
        self.home_screen.fill(WHITE)
        self.home_screen.blit(self.home_screenBackground_image, (0, 100))
        self.home_screen.blit(self.home_screen_textT, self.home_screen_text_rect)
        self.home_screen.blit(self.home_screen_text1, self.home_screen_text_rect1)
        self.home_screen.blit(self.home_screen_text2, self.home_screen_text_rect2)
        self.home_screen.blit(self.home_screen_text3, self.home_screen_text_rect3)
        self.home_screen.blit(self.home_screen_text4, self.home_screen_text_rect4)

    def run(self):
        self.window = pg.display.set_mode((SW, SH))
        pg.display.set_caption('Connect 4')
        self.draw_home_screen()

    def draw_home_screen(self):
        self.updateHome()
        level = 0
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.MOUSEMOTION:
                    mouse_pos = event.pos
                    if self.home_screen_text_rect1.collidepoint(mouse_pos):
                        self.home_screen_text1 = pg.font.SysFont(FONT_NAME, FONT_VERYLARGE).render(
                            'Easy', True, GREEN)
                        self.updateHome()
                    else:
                        self.home_screen_text1 = pg.font.SysFont(FONT_NAME, FONT_LARGE).render('Easy',
                                                                                                     True, BLACK)
                        self.updateHome()

                    if self.home_screen_text_rect2.collidepoint(mouse_pos):
                        self.home_screen_text2 = pg.font.SysFont(FONT_NAME, FONT_VERYLARGE).render(
                            'Medium', True, GREEN)
                        self.updateHome()
                    else:
                        self.home_screen_text2 = pg.font.SysFont(FONT_NAME, FONT_LARGE).render(
                            'Medium', True, BLACK)
                        self.updateHome()
                    if self.home_screen_text_rect3.collidepoint(mouse_pos):
                        self.home_screen_text3 = pg.font.SysFont(FONT_NAME, FONT_VERYLARGE).render(
                            'Hard', True, GREEN)
                        self.updateHome()
                    else:
                        self.home_screen_text3 = pg.font.SysFont(FONT_NAME, FONT_LARGE).render('Hard',
                                                                                                     True, BLACK)
                        self.updateHome()
                    if self.home_screen_text_rect4.collidepoint(mouse_pos):
                        self.home_screen_text4 = pg.font.SysFont(FONT_NAME, FONT_VERYLARGE).render(
                            'Impossible', True, GREEN)
                        self.updateHome()
                    else:
                        self.home_screen_text4 = pg.font.SysFont(FONT_NAME, FONT_LARGE).render('Impossible',
                                                                                                     True, BLACK)
                        self.updateHome()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.home_screen_text_rect1.collidepoint(mouse_pos):
                        level = 1
                    elif self.home_screen_text_rect2.collidepoint(mouse_pos):
                        level = 5
                    elif self.home_screen_text_rect3.collidepoint(mouse_pos):
                        level = 100
                    elif self.home_screen_text_rect4.collidepoint(mouse_pos):
                        level = 5000
                    game_board = Board()
                    connect4 = Game(game_board, level)
                    while not connect4.game_over:
                        connect4.run()
                        if connect4.backHome:
                            break
                        if connect4.game_over:
                            connect4.board =Board()
                            connect4.game_over = False
                            continue
            pg.display.flip()
            self.window.blit(self.home_screen, (0, 0))
            pg.display.update()