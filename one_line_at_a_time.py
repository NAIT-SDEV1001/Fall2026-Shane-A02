from pathlib import Path

def read_game(file_path):

    games = []
    with open(file_path,"r",encoding="utf-8") as file:
        line = file.readline()

        while line !="":
            game = line.strip()

            if game:
              games.append(game)

            line = file.readline()
    return games

def main():
    file_path = Path(__file__).parent/"games.txt"
    games = read_game(file_path)
    print(games)

if __name__ =="__main__":
    main()