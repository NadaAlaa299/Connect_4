import sys
import pygame as pg
from ai import AI
from board import Board
from const import *



class Game:
    def __init__(self, board,level):
        self.level=level
        self.p1_score = 0
        self.p2_score = 0
        self.screen = None
        self.board = board
        self.game_over = False
        self.back_rect = None
        self.backHome=False

    def draw_board(self,p1_score,p2_score):

        for c in range(COLS):
            for r in range(ROWS):
                pg.draw.rect(self.screen,BLUE,
                             (c * SQ_SIZE, r * SQ_SIZE + SQ_SIZE, SQ_SIZE, SQ_SIZE))
                pg.draw.circle(self.screen, WHITE, (
                    int(c * SQ_SIZE + SQ_SIZE / 2), int(r * SQ_SIZE + SQ_SIZE + SQ_SIZE / 2)),RADIUS)
        for c in range(COLS):
            for r in range(ROWS):
                if self.board.board[r][c] == 'x':
                    pg.draw.circle(self.screen, RED, (
                        int(c * SQ_SIZE + SQ_SIZE / 2),
                        HEIGHT - int(r * SQ_SIZE + SQ_SIZE / 2)),
                                   RADIUS)



                elif self.board.board[r][c] == 'o':
                    pg.draw.circle(self.screen, YELLOW, (
                        int(c * SQ_SIZE + SQ_SIZE / 2),
                        HEIGHT - int(r * SQ_SIZE + SQ_SIZE / 2)),
                                   RADIUS)




        font = pg.font.Font(None, 40)
        self.screen.fill(BLACK, (0, SH-SQ_SIZE, WIDTH, HEIGHT))
        p1_surf = font.render("Computer: {}".format(p1_score), True, RED)
        p2_surf = font.render("Agent: {}".format(p2_score), True, YELLOW)
        self.screen.blit(p1_surf, (SQ_SIZE-30, SW+10))
        self.screen.blit(p2_surf, (WIDTH - SQ_SIZE - p2_surf.get_width(), SW + 10))



    def run(self):
        pg.init()
        self.screen = pg.display.set_mode((SW, SH))
        myfont = pg.font.SysFont("Arial", 50)
        self.draw_board(self.p1_score, self.p2_score)
        pg.display.update()
        ai1 = AI(self.level, 'x')
        ai2 = AI(self.level)
        firstTime=True
        while True:
              if not self.game_over :
                    pos, temp_board = ai1.evaluateForX(self.board,3,firstTime)
                    firstTime=False
                    self.board.board = temp_board
                    self.board.mark_pos(pos[0], pos[1], 'x')
                    if self.board.is_winning():
                        label = myfont.render("Computer win!", True, RED)
                        self.screen.blit(label, (195, 10))
                        self.game_over = True
                        self.p1_score += 1
                        self.draw_board(self.p1_score, self.p2_score)
                        pg.display.update()
                    self.draw_board(self.p1_score, self.p2_score)
                    pg.display.update()
                    if self.board.is_full():
                        label = myfont.render("Draw", True,
                                              BLUE)
                        self.screen.blit(label, (250, 10))
                        self.game_over = True
                        self.draw_board(self.p1_score, self.p2_score)
                        pg.display.update()

                    pg.time.wait(500)
              if not self.game_over :
                    if self.level==0:
                        pos=ai2.randAi(self.board)
                    elif self.level==1:
                        pos, temp_board = ai2.evaluate(self.board,3)
                    elif self.level==2:
                        pos, temp_board = ai2.evaluate(self.board,5)
                    elif self.level==3:
                        pos, temp_board = ai2.evaluate(self.board,8)

                    self.board.board = temp_board
                    self.board.mark_pos(pos[0], pos[1], 'o')
                    if self.board.is_winning():
                        label = myfont.render("Agent Win", True,
                                              YELLOW)
                        self.screen.blit(label, (190, 10))
                        self.game_over = True
                        self.p2_score += 1
                        self.draw_board(self.p1_score, self.p2_score)
                        pg.display.update()
                    self.draw_board(self.p1_score, self.p2_score)
                    pg.display.update()
                    pg.time.wait(500)
                    if self.board.is_full():
                        label = myfont.render("Draw", True,
                                              BLUE)
                        self.screen.blit(label, (250, 10))
                        self.game_over = True
                        self.draw_board(self.p1_score, self.p2_score)
                        pg.display.update()
              if self.game_over:
                        pg.time.wait(2000)
                        self.game_over = False
                        self.board=Board()
                        firstTime=False
                        self.draw_board(self.p1_score, self.p2_score)
                        pg.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SQ_SIZE))
                        pg.display.update()







