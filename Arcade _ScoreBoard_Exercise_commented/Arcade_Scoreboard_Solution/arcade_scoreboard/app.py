from pathlib import Path

# A leading dot imports from a module in this same package.
from .score_entry import ScoreEntry
from .scoreboard import Scoreboard
from .score_files import load_scores, save_scores


def main() -> None:
    # Create one board so it keeps its scores between menu choices.
    board = Scoreboard("Space Invaders")

    # Locate scores.csv relative to app.py and load any saved scores.
    score_path = Path(__file__).parent / "data" / "scores.csv"
    load_scores(board, score_path)

    while True:
        # Strip spaces and uppercase the choice so r and R both work.
        choice = input("\n[R]ecord  [F]ind  [S]how  [Q]uit: ").strip().upper()

        if choice == "Q":
            # Save the whole scoreboard, then leave the menu loop.
            save_scores(board, score_path)
            print("Scores saved.")
            break

        if choice == "S":
            board.show()
            continue

        # Only Record and Find need a player name and points.
        if choice not in ("R", "F"):
            print("Choose R, F, S, or Q.")
            continue

        player = input("Player: ").strip()

        try:
            # Convert the input to an integer.
            points = int(input("Points: "))
        except ValueError:
            print("Enter a player name and a non-negative whole number.")
            continue

        # Reject blank names and negative scores.
        if not player or points < 0:
            print("Enter a player name and a non-negative whole number.")
            continue

        # Create a score entry for either Record or Find.
        entry = ScoreEntry(player, points)

        if choice == "R":
            board.record(entry)
            print("Score recorded.")
        elif board.contains(entry):
            print("Score found.")
        else:
            print("Score not found.")