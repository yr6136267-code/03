# """
# Tic Tac Toe with Pygame

# Controls:
#   Click  - place your mark
#   R      - restart the current game
#   1      - play against the computer (you are X)
#   2      - two players on the same computer
# """
import sys
import pygame
BOARD = 600 
CELL = BOARD // 3
HEADER = 80
WIDTH, HEIGHT = BOARD, BOARD + HEADER

BG = (24, 26, 38)
GRID = (70, 75, 100)
X_COLOR = (240, 100, 100)
O_COLOR = (100, 190, 240)
WIN_COLOR = (250, 210, 80)
TEXT = (235, 235, 245)

LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
         (0, 3, 6), (1, 4, 7), (2, 5, 8),
         (0, 4, 8), (2, 4, 6)]



def check_winner(board):
    """Return (player, (start_cell, end_cell)) or None."""
    for a, b, c in LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a], (a, c)
    return None


def is_full(board):
    return all(board)


def minimax(board, player):
    """Return (score, move). Computer is 'O' (maximizing), human is 'X'."""
    result = check_winner(board)
    if result:
        return (1, None) if result[0] == "O" else (-1, None)
    if is_full(board):
        return 0, None

    best_move = None
    if player == "O":
        best_score = -2
        for i in range(9):
            if not board[i]:
                board[i] = "O"
                score, _ = minimax(board, "X")
                board[i] = ""
                if score > best_score:
                    best_score, best_move = score, i
    else:
        best_score = 2
        for i in range(9):
            if not board[i]:
                board[i] = "X"
                score, _ = minimax(board, "O")
                board[i] = ""
                if score < best_score:
                    best_score, best_move = score, i
    return best_score, best_move



def cell_center(i):
    row, col = divmod(i, 3)
    return col * CELL + CELL // 2, HEADER + row * CELL + CELL // 2


def draw_board(screen, board, win_line):
    screen.fill(BG)

  
    for i in range(1, 3):
        pygame.draw.line(screen, GRID, (i * CELL, HEADER + 10), (i * CELL, HEIGHT - 10), 6)
        pygame.draw.line(screen, GRID, (10, HEADER + i * CELL), (WIDTH - 10, HEADER + i * CELL), 6)

    
    pad = CELL // 4
    for i, mark in enumerate(board):
        cx, cy = cell_center(i)
        if mark == "X":
            pygame.draw.line(screen, X_COLOR, (cx - pad, cy - pad), (cx + pad, cy + pad), 12)
            pygame.draw.line(screen, X_COLOR, (cx + pad, cy - pad), (cx - pad, cy + pad), 12)
        elif mark == "O":
            pygame.draw.circle(screen, O_COLOR, (cx, cy), pad + 6, 12)

    
    if win_line:
        pygame.draw.line(screen, WIN_COLOR, cell_center(win_line[0]), cell_center(win_line[1]), 10)


def draw_header(screen, font, small, message, mode):
    text = font.render(message, True, TEXT)
    screen.blit(text, text.get_rect(center=(WIDTH // 2, 32)))
    mode_label = "vs Computer" if mode == "cpu" else "2 Players"
    hint = small.render(f"Mode: {mode_label}   |   1: vs CPU   2: 2 players   R: restart", True, GRID)
    screen.blit(hint, hint.get_rect(center=(WIDTH // 2, 62)))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 44)
    small = pygame.font.SysFont(None, 24)

    mode = "cpu"  

    def new_game():
        return [""] * 9, "X", None, False  

    board, turn, win_line, game_over = new_game()
    message = "X's turn"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board, turn, win_line, game_over = new_game()
                elif event.key == pygame.K_1:
                    mode = "cpu"
                    board, turn, win_line, game_over = new_game()
                elif event.key == pygame.K_2:
                    mode = "pvp"
                    board, turn, win_line, game_over = new_game()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                mx, my = event.pos
                if my >= HEADER:
                    col, row = mx // CELL, (my - HEADER) // CELL
                    i = row * 3 + col
                    
                    human_can_play = mode == "pvp" or turn == "X"
                    if human_can_play and not board[i]:
                        board[i] = turn
                        turn = "O" if turn == "X" else "X"

    
        if mode == "cpu" and turn == "O" and not game_over and not check_winner(board) and not is_full(board):
            pygame.time.delay(250)  # small pause so it feels natural
            _, move = minimax(board, "O")
            board[move] = "O"
            turn = "X"

        
        result = check_winner(board)
        if result:
            game_over = True
            win_line = result[1]
            message = f"{result[0]} wins!  Press R to play again"
        elif is_full(board):
            game_over = True
            message = "It's a draw!  Press R to play again"
        else:
            message = f"{turn}'s turn"

        draw_board(screen, board, win_line)
        draw_header(screen, font, small, message, mode)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()