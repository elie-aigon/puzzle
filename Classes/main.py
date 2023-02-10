from BUTTON import BUTTON
from BLOCK import BLOCK
from BOARD import BOARD
from SCOREBOARD import SCOREBOARD
from Settings import *
import pygame, sys, json


class MAIN():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Slide Puzzle")
        self.screen = pygame.display.set_mode((1100, 700))
        self.restart_button = BUTTON(self.screen, font_pixel, grey, 20, 490, 150, 80, "RESTART", "Data/Images/yellow/yellow_normal.png", lambda: self.restart())
        self.quit_button = BUTTON(self.screen, font_pixel, grey, 20, 590, 150, 80, "QUIT", "Data/Images/red/red_normal.png", lambda: self.quit())
        self.size_5X5 = BUTTON(self.screen, font_pixel, grey, 45, 390, 100, 80, "5X5", "Data/Images/green_button/gree_normal.png", lambda: self.change_size(5))
        self.size_4X4 = BUTTON(self.screen, font_pixel, grey, 45, 290, 100, 80, "4X4", "Data/Images/green_button/gree_normal.png", lambda: self.change_size(4))
        self.size_3X3 = BUTTON(self.screen, font_pixel, grey, 45, 190, 100, 80, "3X3", "Data/Images/green_button/gree_normal.png", lambda: self.change_size(3))
        self.win = BUTTON(self.screen, font_win_mess, white, 300, 200, 400, 300, "YOU WIN !", "Data/Images/win_mess.png", lambda: self.restart())
        self.board = BOARD(self.screen, 200, 200)
        self.scoreboard = SCOREBOARD(self.screen, (710, 100))
        self.title_aff = font_title.render("Slide Puzzle", True, white)
        self.instructions = font_block.render("Type Your Name: ", True, white)
        
        self.name_set = False
        self.name = []
        
        self.clock = 0
        self.if_win = False

    def quit(self):
        pygame.quit()
        sys.exit()

    def restart(self):
        self.board.create_board()
        self.name_set = False
        self.name = []
        self.clock = 0
        self.if_win = False

    def change_size(self, value):
        global game_size
        if value == 3:
            self.board.game_settings[0] = 3
            self.board.game_settings[1] = 150
        if value == 4:
            self.board.game_settings[0] = 4
            self.board.game_settings[1] = 100
        if value == 5:
            self.board.game_settings[0] = 5
            self.board.game_settings[1] = 80
        self.restart()

    def draw_elements(self):
        self.screen.blit(self.title_aff, (550 - self.title_aff.get_width()// 2, 10))
        self.clock_aff = font_pixel.render("TIME: " + str(self.scoreboard.convert_time(self.clock)), True, white)
        self.screen.blit(self.clock_aff, (0, 10))
        self.restart_button.draw_button()
        self.quit_button.draw_button()
        self.size_5X5.draw_button()
        self.size_4X4.draw_button()
        self.size_3X3.draw_button()
        self.board.draw_board()
        self.scoreboard.draw_scoreboard()
        if self.if_win:
            self.win.draw_button()
            self.instruc_win = font_pixel.render("Click me to restart", True, grey)
            self.screen.blit(self.instruc_win, (370, 230))

        if not self.name_set:
            self.instructions = font_block.render("Type Your Name : ", True, white)
            self.name_aff = font_block.render(("".join(self.name)), True, white)
            self.screen.blit(self.name_aff, (400, 120))
        else:
            self.instructions = font_block.render("PLAY ! ", True, white)
        self.screen.blit(self.instructions, (50, 120))

    def game_start(self, event):
            if event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
            if event.key == pygame.K_RETURN:
                self.name_set = True
            if event.key in range(96, 123):
                self.name.append(chr(event.key))
            print(self.name)

    def while_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.restart_button.is_clicked(pygame.mouse.get_pos())
                    self.quit_button.is_clicked(pygame.mouse.get_pos())
                    self.size_4X4.is_clicked(pygame.mouse.get_pos())
                    self.size_5X5.is_clicked(pygame.mouse.get_pos())
                    self.size_3X3.is_clicked(pygame.mouse.get_pos())
                    if self.is_win:
                        self.win.is_clicked(pygame.mouse.get_pos())

                if not self.name_set:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.name = self.name[:-1]
                        if event.key == pygame.K_RETURN:
                            self.name_set = True
                        if event.key in range(96, 123):
                            self.name.append(chr(event.key))
                else:
                    if event.type  == TIMER_UPDATE:
                        self.clock += 1

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            move = "LEFT"
                            self.board.move(move)                          
                        if event.key == pygame.K_RIGHT:
                            move = "RIGHT"
                            self.board.move(move)
                        if event.key == pygame.K_DOWN:
                            move = "DOWN"
                            self.board.move(move)
                        if event.key == pygame.K_UP:
                            move = "UP"
                            self.board.move(move)
            self.screen.fill(grey)
            self.draw_elements()
            if self.board.detect_win():
                self.scoreboard.update_score("".join(self.name), self.clock)
                self.if_win = True
            pygame.display.update()



main = MAIN()
main.while_loop()

