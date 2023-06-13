import pygame

# Constants
BOARD_SIZE = 10
WIN_MARK_COUNT = 3
CELL_SIZE = 50
WINDOW_SIZE = BOARD_SIZE * CELL_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Tic Tac Toe")
        self.clock = pygame.time.Clock()

        # Initialize the board
        self.board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

        # Current player
        self.current_player = 'X'

    def draw_board(self):
        self.screen.fill(WHITE)

        # Draw grid lines
        for x in range(CELL_SIZE, WINDOW_SIZE, CELL_SIZE):
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, WINDOW_SIZE), 2)
            pygame.draw.line(self.screen, BLACK, (0, x), (WINDOW_SIZE, x), 2)

        # Draw X and O symbols
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                symbol = self.board[row][col]
                if symbol == 'X':
                    self.draw_x(row, col)
                elif symbol == 'O':
                    self.draw_o(row, col)

    def draw_x(self, row, col):
        image_src = 'tictactoe_x.png'
        mark = pygame.image.load(image_src)
        x = col * CELL_SIZE
        y = row * CELL_SIZE
        mark = pygame.transform.scale(mark, (CELL_SIZE, CELL_SIZE))
        cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        self.screen.blit(mark, cell_rect)

    def draw_o(self, row, col):
        image_src = 'tictactoe_o.png'
        mark = pygame.image.load(image_src)
        x = col * CELL_SIZE
        y = row * CELL_SIZE
        mark = pygame.transform.scale(mark, (CELL_SIZE, CELL_SIZE))
        cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        self.screen.blit(mark, cell_rect)

    def get_cell(self, x, y):
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        return row, col

    def handle_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'

    def check_win(self, player):
        if self.check_rows(player):
            return True
        elif self.check_columns(player):
            return True
        elif self.check_diagonal(player):
            return True

        return False

    def check_rows(self, player):
        count = 0
        for row in self.board:
            for cell in row:
                if cell == player:
                    count += 1
                else:
                    count = 0
                if count == WIN_MARK_COUNT:
                    return True

    def check_columns(self, player):
        count = 0
        for col in range(BOARD_SIZE):
            for row in range(BOARD_SIZE):
                if self.board[row][col] == player:
                    count += 1
                else:
                    count = 0
                if count == WIN_MARK_COUNT:
                    return True

    def check_diagonal(self, player):
        mark_found = False
        for row in range(BOARD_SIZE):
            for column in range(BOARD_SIZE):
                if self.board[row][column] != ' ':
                    mark_found = True

                if mark_found:
                    count = 0
                    for i in range(WIN_MARK_COUNT):
                        if (row + 1) < BOARD_SIZE and (column + 1) < BOARD_SIZE:
                            if self.board[row + i][column + i] == player:
                                count += 1
                            else:
                                count = 0
                            if count == WIN_MARK_COUNT:
                                return True

                    count = 0
                    for i in range(WIN_MARK_COUNT):
                        if (row + 1) < BOARD_SIZE and (column - 1) > -1:
                            if self.board[row + i][column - i] == player:
                                count += 1
                            else:
                                count = 0
                            if count == WIN_MARK_COUNT:
                                return True
                mark_found = False

    def play_game(self):
        game_continue = True
        while game_continue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_continue = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = self.get_cell(x, y)
                    self.handle_click(row, col)

            self.draw_board()

            # Check for a win
            if self.check_win('X'):
                print("Player X wins!")
                game_continue = False
            elif self.check_win('O'):
                print("Player O wins!")
                game_continue = False
            elif all(symbol != ' ' for row in self.board for symbol in row):
                print("It's a tie!")
                game_continue = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
