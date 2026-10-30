from pathlib import Path

def read_all_games(file_path):
    try:
        #open a connection to the file_path for reading
        #call that connection file
        with open(file_path,"r",encoding="utf-8") as file:
            games = file.readlines()
            #for each game(row), if after removing all the spaces, there is still a value, add it to clean_game
            clean_games = [game.strip() for game in games if game.strip()]
        return clean_games
    except FileNotFoundError:
        return None

def main():
    file_path = Path(__file__).parent/"games.txt"
    games = read_all_games(file_path)

    if not games:
        print("The file was not found")
    else:
        #loop through list and display games on each line
        for game in games:
            print(game)

if __name__ == "__main__":
    main()
