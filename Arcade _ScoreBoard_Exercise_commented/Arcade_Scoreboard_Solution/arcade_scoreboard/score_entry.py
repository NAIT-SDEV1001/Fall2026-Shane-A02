# One object represents one player and one score.
class ScoreEntry:
    def __init__(self, player: str, points: int) -> None:
        # Store the supplied name on this particular object.
        self.player = player
        # Keep points as an integer for numeric comparisons.
        self.points = points

    # print(entry) uses this player-friendly text.
    def __str__(self) -> str:
        return f"{self.player} scored {self.points} points"

    # repr(entry) and printing a list of entries use this developer-friendly text.
    def __repr__(self) -> str:
        # The !r conversion uses repr() on the name so a string appears with quotes.
        return f"ScoreEntry(player={self.player!r}, points={self.points})"

    # Python calls this method to compare entries with ==.
    def __eq__(self, other: object) -> bool:
        # # Check the other object's type before accessing its score attributes.
        # if not isinstance(other, ScoreEntry):
        #     # Let Python try the other object's comparison for an unsupported type.
        #     return NotImplemented
        # Both fields must match. String equality also checks letter case.
        return self.player == other.player and self.points == other.points

# first = ScoreEntry("Sam", 900)
# second = ScoreEntry("Sam", 900)
# third = ScoreEntry("Sam", 950)

# print(first)            # Sam scored 900 points
# print(first == second)  # True
# print(first == third)   # False

# print(first) uses __str__. The == comparisons use __eq__, which checks whether both the player name and the points match.