import csv
from pathlib import Path
from pprint import pprint

def read_sales(file_path):
    sales = []
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for sale in reader:
                sales.append(sale)
    except FileNotFoundError:
        print(f'Error: The file {file_path} does not exist')
        return None
    return sales

def get_popular_games(sales):
    games = []
    for sale in sales:
        price = float(sale['Price'])
        quantity = int(sale['Quantity'])
        revenue = price * quantity
        if revenue >= 100:
            games.append({
                'Game': sale['Game'],
                'Category': sale['Category'],
                'Revenue': f"{revenue:.2f}"               
                })
    return games

def write_report(file_path,games):
    fieldnames = ["Game", "Category", "Revenue"]
    with open(file_path,'w',newline = '', encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        for game in games:
            writer.writerow(game)

def main():
    file_path = Path(__file__).parent/'data'/'game_sales.csv'
    sales = read_sales(file_path)
    if sales is None:
        return    
    games = get_popular_games(sales)
    file_path = Path(__file__).parent/'data'/'popular_games.csv'
    write_report(file_path,games)
    print(f'Sales records read: {len(sales)}')
    if games:
        print('\nGames earning at least $100:')
        for game in games:
            print(f'{game['Game']}:${game['Revenue']}')
    else:
        print(f'\nNo games earned at least $100')
    print(f'\nReport saved to {file_path.name} ')    


if __name__ == '__main__':
    main()
