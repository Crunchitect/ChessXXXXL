import pygame

pygame.init()


def main():
    screen = pygame.display.set_mode((540, 540))
    clock = pygame.time.Clock()

    def return_color(piece):
        black_pieces = {'♜', '★', '♞', '♝', '♝', '♞', '⛊', '♥', '♠', '♛', '♚', '⚑', '♣', '♦', '♞', '♝', '♝',
                        '♞', '★', '♜', '♟'}
        if piece == '':
            return None
        elif piece in black_pieces:
            return 'black'
        else:
            return 'white'

    def draw_rect_center(display: pygame.Surface, c: tuple[int, int, int], x1: int, y1: int, x2: int, y2: int):
        """Draw A Rectangle from (x, y1) -> (x2, y2) where the
        center is (0, 0)"""
        w, h = display.get_width(), display.get_height()
        x1 += w / 2
        x2 += w / 2
        y1 += h / 2
        y2 += h / 2
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        pygame.draw.rect(display, c, pygame.Rect(
            x1, y1, x2 - x1, y2 - y1
        ))

    def draw_chess_board(w):
        nonlocal screen
        width = 500 / w
        for ix in range(w):
            for jx in range(w):
                if (ix + jx) % 2 == 0:
                    draw_rect_center(screen, (255, 255, 255),
                                     -250 + ix * width, -250 + jx * width,
                                     -250 + (ix + 1) * width, -250 + (jx + 1) * width)
                else:
                    draw_rect_center(screen, (80, 80, 80),
                                     -250 + ix * width, -250 + jx * width,
                                     -250 + (ix + 1) * width, -250 + (jx + 1) * width)

    def blit_chess_board(txt, sz, ix, iy):
        nonlocal screen
        width = 500 / sz
        w, h = screen.get_width(), screen.get_height()
        screen.blit(txt, ((-248 + ix * width) + w / 2, (-257 + iy * width) + h / 2))

    def render_board():
        nonlocal font, bx, by
        for y, i in enumerate(board):
            for x, j in enumerate(i):
                if x == bx and y == by:
                    text = font.render(str(j), False, (255, 0, 0))
                else:
                    text = font.render(str(j), False, (0, 0, 0))
                blit_chess_board(text, 20, x, y)

    def setup_board():
        nonlocal board
        board = [
            ['♜', '★', '♞', '♝', '♝', '♞', '⛊', '♥', '♠', '♛', '♚', '⚑', '♣', '♦', '♞', '♝', '♝', '♞', '★', '♜'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟', ],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '☆', '♘', '♗', '♗', '♘', '⛉', '♡', '♤', '♕', '♔', '⚐', '♧', '♢', '♘', '♗', '♗', '♘', '☆', '♖'],
        ]

    def move_plate():

        nonlocal bx, by, board, screen, available_moves, turn
        available_moves = []
        try:
            if turn == 'white':
                if board[by][bx] == '♙' and board[by - 1][bx] == '' and by >= 2:  # this is pawns code'♘'
                    pygame.draw.circle(screen, (128, 128, 128), (((bx + 1) * 25) + 8, (by * 25) - 15), 5)
                    available_moves.append(((bx, by), (bx, by - 1)))
                    if board[by - 2][bx] == '' and by >= 3:
                        pygame.draw.circle(screen, (128, 128, 128), (((bx + 1) * 25) + 8, ((by + 1) * 25) - 15), 5)
                        available_moves.append(((bx, by), (bx, by - 2)))
                    if return_color(board[by - 1][bx + 1]) == 'black':
                        pygame.draw.circle(screen, (128, 128, 128), (((bx + 2) * 25) + 8, ((by + 1) * 25) - 15), 5)
                        available_moves.append(((bx, by), (bx + 1, by - 1)))
                    if return_color(board[by - 1][bx - 1]) == 'black':
                        pygame.draw.circle(screen, (128, 128, 128), ((bx * 25) + 8, ((by + 1) * 25) - 15), 5)
                        available_moves.append(((bx, by), (bx - 1, by - 1)))
                if board[by][bx] == '♗':  # this is bishops code
                    for t in range(1, 20):
                        available_moves.append(((bx, by), (bx - t, by - t)))
                        available_moves.append(((bx, by), (bx + t, by - t)))
                if board[by][bx] == '♘':  # this is horseys code
                    available_moves.append(((bx, by), (bx + 1, by + 2)))
                    available_moves.append(((bx, by), (bx + 1, by - 2)))
                    available_moves.append(((bx, by), (bx - 1, by + 2)))
                    available_moves.append(((bx, by), (bx - 1, by - 2)))
                    available_moves.append(((bx, by), (bx + 2, by + 1)))
                    available_moves.append(((bx, by), (bx + 2, by - 1)))
                    available_moves.append(((bx, by), (bx - 2, by + 1)))
                    available_moves.append(((bx, by), (bx - 2, by - 1)))
                if board[by][bx] == '♖':  # this is rook code
                    for t in range(-20, 20):
                        if board[by - t][bx - t] != '':
                            break
                        if board[by - t][bx + t] != '':
                            break
                        available_moves.append(((bx, by), (bx + t, by)))
                        available_moves.append(((bx, by), (bx, by + t)))
                if board[by][bx] == '♕':  # this is queen code
                    for t in range(-20, 20):
                        available_moves.append(((bx, by), (bx + t, by)))
                        available_moves.append(((bx, by), (bx, by + t)))
                        available_moves.append(((bx, by), (bx - t, by - t)))
                        available_moves.append(((bx, by), (bx + t, by - t)))
                    for t in range(-20, 20):
                        if board[by - t][bx - t] != '':
                            break
                        if board[by - t][bx - t] != '':
                            break
                        available_moves.append(((bx, by), (bx - t, by - t)))
                        available_moves.append(((bx, by), (bx + t, by - t)))
            else:
                if board[by][bx] == '♟' and board[by + 1][bx] == '' and by <= 18:
                    pygame.draw.circle(screen, (128, 128, 128), (((bx + 1) * 25) + 8, ((by + 2) * 25) + 5), 5)
                    available_moves.append(((bx, by), (bx, by + 1)))
                    if board[by + 2][bx] == '' and by <= 17:
                        pygame.draw.circle(screen, (128, 128, 128), (((bx + 1) * 25) + 8, ((by + 3) * 25) + 5), 5)
                        available_moves.append(((bx, by), (bx, by + 2)))
                    if return_color(board[by + 1][bx + 1]) == 'white':
                        pygame.draw.circle(screen, (128, 128, 128), (((bx + 2) * 25) + 8, ((by + 2) * 25) + 5), 5)
                        available_moves.append(((bx, by), (bx + 1, by + 1)))
                    if return_color(board[by + 1][bx - 1]) == 'white':
                        pygame.draw.circle(screen, (128, 128, 128), ((bx * 25) + 8, ((by + 2) * 25) + 5), 5)
                        available_moves.append(((bx, by), (bx - 1, by + 1)))
                if board[by][bx] == '♝':  # this is bishops code
                    for t in range(1, 20):
                        available_moves.append(((bx, by), (bx - t, by - t)))
                        available_moves.append(((bx, by), (bx + t, by + t)))
                        available_moves.append(((bx, by), (bx + t, by - t)))
                        available_moves.append(((bx, by), (bx - t, by + t)))
                if board[by][bx] == '♞':  # this is horseys code
                    available_moves.append(((bx, by), (bx + 1, by + 2)))
                    available_moves.append(((bx, by), (bx + 1, by - 2)))
                    available_moves.append(((bx, by), (bx - 1, by + 2)))
                    available_moves.append(((bx, by), (bx - 1, by - 2)))
                    available_moves.append(((bx, by), (bx + 2, by + 1)))
                    available_moves.append(((bx, by), (bx + 2, by - 1)))
                    available_moves.append(((bx, by), (bx - 2, by + 1)))
                    available_moves.append(((bx, by), (bx - 2, by - 1)))
                if board[by][bx] == '♜':  # this is rook code
                    for t in range(-20, 20):
                        if board[by - t][bx - t] != '':
                            break
                        if board[by - t][bx + t] != '':
                            break
                        available_moves.append(((bx, by), (bx + t, by)))
                        available_moves.append(((bx, by), (bx, by + t)))
                if board[by][bx] == '♛':  # this is queen code
                    for t in range(-20, 20):
                        available_moves.append(((bx, by), (bx + t, by)))
                        available_moves.append(((bx, by), (bx, by + t)))
                        available_moves.append(((bx, by), (bx - t, by - t)))
                        available_moves.append(((bx, by), (bx + t, by - t)))
                    for t in range(-20, 20):
                        if board[by - t][bx - t] != '':
                            break
                        if board[by - t][bx - t] != '':
                            break
                        available_moves.append(((bx, by), (bx - t, by - t)))
                        available_moves.append(((bx, by), (bx + t, by - t)))
        except IndexError:
            pass

    def move_piece(ix, iy):
        nonlocal board, bx, by, turn
        try:
            for i in available_moves:
                if i[1][0] == ix and i[1][1] == iy:
                    # print('!!!', board[i[0][1]][i[0][0]])
                    board[i[1][1]][i[1][0]] = board[i[0][1]][i[0][0]]
                    board[i[0][1]][i[0][0]] = ''
                    bx, by = -1, -1
                    turn = 'black' if turn == 'white' else 'white'
        except IndexError:
            pass

    font = pygame.font.Font("font.ttf", 35)
    turn = 'white'
    running = True
    bx, by = -1, -1
    board = []
    setup_board()
    available_moves = []
    while running:
        continue
        mx, my = pygame.mouse.get_pos()
        clock.tick(60)
        screen.fill((100, 100, 100))
        draw_chess_board(20)
        move_plate()
        render_board()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bx, by = mx // 25 - 1, my // 25 - 1
                move_piece(bx, by)


if __name__ == '__main__':
    main()
