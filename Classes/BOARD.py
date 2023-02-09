import pygame, sys, random, json, random
from Settings import *
from BLOCK import BLOCK


class BOARD():
    def __init__(self, surface, pos_x, pos_y):
        self.game_settings = [5, 80]
        self.x = pos_x
        self.y = pos_y
        self.surface = surface        
        self.create_board()        

    def create_board(self):
        self.board = self.create_win_board()
        self.random_moves()
    
    def draw_board(self):

        for x in range(self.game_settings[0]):
            for y in range(self.game_settings[0]):
                if self.board[x][y]:
                    if self.board[x][y] == self.game_settings[0]* self.game_settings[0]:
                        pass
                    else:
                        self.draw_block(x, y)
                        
    def draw_block(self, block_x, block_y):
        self.block = pygame.image.load("Data/Images/game_box.png")
        self.block = pygame.transform.scale(self.block, (self.game_settings[1], self.game_settings[1]))
        x, y = self.get_pos_block(block_x, block_y)
        self.rect = pygame.Rect(x, y, self.game_settings[0], self.game_settings[0])
        self.surface.blit(self.block, self.rect)

        self.block_number = str(self.board[block_x][block_y])
        self.block_number_aff = font_block.render(self.block_number, True, grey)
        self.surface.blit(self.block_number_aff, (x + (self.game_settings[1] // 2) - self.block_number_aff.get_width() // 2, y + (self.game_settings[1] // 2) - self.block_number_aff.get_width() // 2 - 5))
        
    def get_pos_block(self, block_x, block_y):
        x = self.x + (block_x * self.game_settings[1]) + (block_x * 10)
        y = self.y + (block_y * self.game_settings[1]) + (block_y * 10)
        return x, y

    def move(self, move):
        x_max, y_max = self.find_max_number(self.board)
        if move in self.is_valid_move(x_max, y_max):
            if move == "LEFT":
                self.board[x_max][y_max], self.board[x_max + 1][y_max] = self.board[x_max + 1][y_max], self.board[x_max][y_max]
            if move == "RIGHT":
                self.board[x_max][y_max], self.board[x_max - 1][y_max] = self.board[x_max - 1][y_max], self.board[x_max][y_max]
            if move == "UP":
                self.board[x_max][y_max], self.board[x_max][y_max + 1] = self.board[x_max][y_max + 1], self.board[x_max][y_max]
            if move == "DOWN":
                self.board[x_max][y_max], self.board[x_max][y_max - 1] = self.board[x_max][y_max - 1], self.board[x_max][y_max]

    def find_max_number(self, board):
        for x_max in range(self.game_settings[0]):
            for y_max in range(self.game_settings[0]):
                if board[x_max][y_max] == int(self.game_settings[0]**2):
                    return x_max, y_max

    def is_valid_move(self, x_max, y_max):
        possibles_moves = []
        if x_max > 0:
            possibles_moves.append("RIGHT")
        if x_max < self.game_settings[0] - 1:
            possibles_moves.append("LEFT")
        if y_max > 0:
            possibles_moves.append("DOWN")
        if y_max < self.game_settings[0] - 1:
            possibles_moves.append("UP")
        return possibles_moves
    
    def random_moves(self):
        count_random_moves = 0
        while count_random_moves < 1000:
            x_max, y_max = self.find_max_number(self.board)
            random_move = random.choice(self.is_valid_move(x_max, y_max))
            self.move(random_move)
            count_random_moves += 1

    def create_win_board(self):
        self.buff = 1
        self.win_board = []
        for x in range(self.game_settings[0]):
            col = []
            for y in range(self.game_settings[0]):
                col.append(self.buff)
                self.buff += self.game_settings[0]
            self.win_board.append(col)
            self.buff = self.buff - (self.game_settings[0] * self.game_settings[0] - 1)
        return self.win_board

    def detect_win(self):
        self.create_win_board()
        if self.board == self.win_board:
            self.create_board()
            return True
        else:
            return False

    def reset_board(self):
        self.create_board()
