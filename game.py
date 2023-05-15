import sys
import pygame as pg
from ai import AI
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
        p1_surf = font.render("You: {}".format(p1_score), True, RED)
        p2_surf = font.render("AI: {}".format(p2_score), True, YELLOW)
        self.screen.blit(p1_surf, (SQ_SIZE, SW+10))
        self.screen.blit(p2_surf, (WIDTH - SQ_SIZE - p2_surf.get_width(), SW + 10))
        self.back_surf = font.render("Back", True, WHITE)
        self.back_rect = self.back_surf.get_rect( center=(SW - 3 * SQ_SIZE - 30, SW + 40))
        self.screen.blit(self.back_surf, self.back_rect)

    def run(self):
        pg.init()
        self.screen = pg.display.set_mode((SW, SH))
        myfont = pg.font.SysFont("Arial", 50)
        self.draw_board(self.p1_score, self.p2_score)
        pg.display.update()
        current_player = 0
        ai = AI(self.level, 'o')
        while not self.game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.MOUSEMOTION:
                    pg.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SQ_SIZE))
                    mousexm = event.pos[0]
                    if current_player == 0:
                        pg.draw.circle(self.screen, RED, (mousexm, int(SQ_SIZE / 2)), RADIUS)
                        pg.display.update()
                if event.type == pg.MOUSEBUTTONDOWN:
                    back=event.pos
                    mousex = event.pos[0]
                    if self.back_rect.collidepoint(back):
                        self.backHome=True
                        return
                    pg.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SQ_SIZE))
                    if current_player == 0:

                        col = int(mousex / SQ_SIZE)
                        flag=False
                        if self.board.is_empty('x', col):
                            flag=True
                            if self.board.is_winning():
                                label = myfont.render("Congratulations!! you win!", True,
                                                               RED)
                                self.screen.blit(label, (65, 10))
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
                            current_player = (current_player + 1) % 2
                        if flag and not self.game_over:
                            pos, temp_board = ai.evaluate(self.board)
                            self.board.board = temp_board
                            self.board.mark_pos(pos[0], pos[1], 'o')

                            if self.board.is_winning():
                                label = myfont.render("Hard luck Next Time", True,
                                                               YELLOW)
                                self.screen.blit(label, (120, 10))
                                self.game_over = True
                                self.p2_score += 1
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
                            current_player = (current_player + 1) % 2
                        if self.game_over:
                            pg.time.wait(6000)
                            pg.display.update()
                            break



