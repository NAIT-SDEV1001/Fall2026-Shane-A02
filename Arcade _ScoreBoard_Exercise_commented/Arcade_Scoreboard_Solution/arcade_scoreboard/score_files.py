import csv
from pathlib import Path

from .score_entry import ScoreEntry
from .scoreboard import Scoreboard


def load_scores(board: Scoreboard, file_path: Path) -> None:
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            # DictReader uses the header to name each column.
            reader = csv.DictReader(file)
            for row in reader:
                player = row["player"]
                points = int(row["points"])  # CSV values are read as strings.
                board.record(ScoreEntry(player, points))
    except FileNotFoundError:
        # On the first run, the board stays empty until the player records a score.
        return


def save_scores(board: Scoreboard, file_path: Path) -> None:
    fieldnames = ["player", "points"]

    # Write mode replaces the file contents with the whole scoreboard.
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for entry in board.entries:
            # The dictionary keys match the CSV column names.
            writer.writerow({"player": entry.player, "points": entry.points})