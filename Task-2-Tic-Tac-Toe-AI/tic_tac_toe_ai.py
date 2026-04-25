"""
Tic-Tac-Toe AI — CodSoft Artificial Intelligence Internship | Task 2
Algorithm: Minimax with Alpha-Beta Pruning
Author: [Your Name]
"""

import math

# ──────────────────────────────────────────────
# Board utilities
# ──────────────────────────────────────────────

WIN_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6],             # diagonals
]


def print_board(board: list[str]) -> None:
    """Print the board in a readable 3x3 grid."""
    symbols = {" ": "·", "X": "X", "O": "O"}
    print()
    for row in range(3):
        cells = [symbols[board[row * 3 + col]] for col in range(3)]
        print(f"  {cells[0]}  |  {cells[1]}  |  {cells[2]}")
        if row < 2:
            print("  ───┼─────┼───")
    print()


def print_positions() -> None:
    """Show position indices so the user knows which number to enter."""
    print("\n  Position guide:")
    for row in range(3):
        nums = [str(row * 3 + col + 1) for col in range(3)]
        print(f"  {nums[0]}  |  {nums[1]}  |  {nums[2]}")
        if row < 2:
            print("  ───┼─────┼───")
    print()


def check_winner(board: list[str]) -> str | None:
    """
    Return:
        'X'    — X wins
        'O'    — O wins
        'draw' — board full, no winner
        None   — game still in progress
    """
    for line in WIN_LINES:
        a, b, c = line
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board:
        return "draw"
    return None


def get_empty_cells(board: list[str]) -> list[int]:
    return [i for i, cell in enumerate(board) if cell == " "]


# ──────────────────────────────────────────────
# Minimax with Alpha-Beta Pruning
# ──────────────────────────────────────────────

def minimax(board: list[str], is_maximizing: bool, alpha: float, beta: float) -> int:
    """
    Recursively evaluate board states.
    AI  = 'O' (maximizing player)
    Human = 'X' (minimizing player)
    Returns a score: +10 (AI wins), -10 (human wins), 0 (draw).
    Alpha-Beta Pruning skips branches that cannot affect the outcome,
    significantly reducing the number of nodes evaluated.
    """
    result = check_winner(board)
    if result == "O":
        return 10
    if result == "X":
        return -10
    if result == "draw":
        return 0

    if is_maximizing:
        best = -math.inf
        for i in get_empty_cells(board):
            board[i] = "O"
            score = minimax(board, False, alpha, beta)
            board[i] = " "
            best = max(best, score)
            alpha = max(alpha, best)
            if beta <= alpha:       # Beta cut-off
                break
        return best
    else:
        best = math.inf
        for i in get_empty_cells(board):
            board[i] = "X"
            score = minimax(board, True, alpha, beta)
            board[i] = " "
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:       # Alpha cut-off
                break
        return best


def get_best_move(board: list[str]) -> int:
    """Return the index of the best move for the AI ('O')."""
    best_score = -math.inf
    best_move = -1
    for i in get_empty_cells(board):
        board[i] = "O"
        score = minimax(board, False, -math.inf, math.inf)
        board[i] = " "
        if score > best_score:
            best_score = score
            best_move = i
    return best_move


# ──────────────────────────────────────────────
# Game loop
# ──────────────────────────────────────────────

def human_move(board: list[str]) -> None:
    """Prompt the human player for a valid move."""
    while True:
        try:
            pos = int(input("  Enter position (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("  ✗  Enter a number between 1 and 9.")
            elif board[pos] != " ":
                print("  ✗  That cell is already taken. Try another.")
            else:
                board[pos] = "X"
                break
        except ValueError:
            print("  ✗  Invalid input. Enter a number (1-9).")


def print_result(result: str) -> None:
    if result == "X":
        print("  ★  You win! Congratulations!\n")
    elif result == "O":
        print("  ★  AI wins! Better luck next time.\n")
    else:
        print("  ★  It's a draw!\n")


def play_game() -> None:
    """Run a single game of Tic-Tac-Toe."""
    board = [" "] * 9
    print_positions()
    print("  Game start — You are X, AI is O.\n")

    while True:
        # ── Human turn (X) ──
        print_board(board)
        print("  Your turn (X):")
        human_move(board)

        result = check_winner(board)
        if result:
            print_board(board)
            print_result(result)
            return

        # ── AI turn (O) ──
        print("  AI is thinking…")
        ai_move = get_best_move(board)
        board[ai_move] = "O"
        print(f"  AI played position {ai_move + 1}.")

        result = check_winner(board)
        if result:
            print_board(board)
            print_result(result)
            return


def main() -> None:
    print("\n" + "═" * 36)
    print("   TIC-TAC-TOE AI  |  CodSoft Task 2")
    print("   Algorithm: Minimax + Alpha-Beta")
    print("═" * 36)

    scores = {"X": 0, "O": 0, "draw": 0}

    while True:
        play_game()

        # Update scores
        # (result is printed inside play_game; track manually via replay loop)
        # Ask to play again
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing! Goodbye.\n")
            break


if __name__ == "__main__":
    main()
