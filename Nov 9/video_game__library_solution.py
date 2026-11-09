class VideoGame:
    def __init__(self, title: str, platform: str, hours_played: int) -> None:
        self.title = title
        self.platform = platform
        self.hours_played = hours_played

    def add_play_time(self, hours: int) -> None:
        self.hours_played += hours

    def has_been_played(self) -> bool:
        return self.hours_played > 0

    def __str__(self) -> str:
        return f"{self.title} on {self.platform} ({self.hours_played} hours played)"

    def __repr__(self) -> str:
        #!r will have quotes around the strings. Safer than hard coding ' ' around the string (if the string has a quote in it already)
        return (
            f"VideoGame(title={self.title!r}, platform={self.platform!r}, "
            f"hours_played={self.hours_played})"
        )




def main() -> None:
     

    # Question 5. Collect VideoGame objects from user input.
    print("\n5. Enter games")
    games: list[VideoGame] = []

    while True:
        title = input("Game title (q to finish): ")
        if title == "q":
            break

        platform = input("Platform: ")
        hours_played = int(input("Hours played: "))       
        game = VideoGame(title, platform, hours_played)
        games.append(game)
        #OR
        #games.append(VideoGame(title, platform, hours_played))

    # Question 6. Display each game, then display just the titles.
    print("\nGame library")
    for game in games:
        print(game)

    print("\nGame titles")
    for game in games:
        print(game.title)


if __name__ == "__main__":
    main()
