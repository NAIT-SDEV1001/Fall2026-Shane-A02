from pathlib import Path

def read_games(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        #loop through the file directly 
        clean_list = [line.strip() for line in file if line.strip()]
    return clean_list

def main ():
    file_path = Path(__file__).parent/"games.txt"
    games = read_games(file_path)
    print(games)

if __name__ == "__main__":
    main()
