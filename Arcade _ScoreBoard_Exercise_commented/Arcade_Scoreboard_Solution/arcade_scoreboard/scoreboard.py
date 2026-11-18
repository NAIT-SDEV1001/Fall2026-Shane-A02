# Import the type used for entries from a sibling module.
from .score_entry import ScoreEntry


class Scoreboard:
    def __init__(self, game: str) -> None:
        # Keep the game name for the display heading.
        self.game = game
        # Create a separate empty list for each scoreboard.
        self.entries: list[ScoreEntry] = []

    def record(self, entry: ScoreEntry) -> None:
        # Store the object the caller created. This is aggregation.
        self.entries.append(entry)

    def show(self) -> None:
        print(f"\n{self.game} scoreboard")
        # An empty list is false in an if condition.
        if not self.entries:
            print("No scores yet.")
        # Start the display numbers at 1 and keep the original recording order.
        for number, entry in enumerate(self.entries, start=1):
            # Formatting entry here uses ScoreEntry.__str__.
            print(f"{number}. {entry}")

    def contains(self, entry: ScoreEntry) -> bool:
        # List membership uses ScoreEntry.__eq__ to compare separate objects.
        return entry in self.entries
