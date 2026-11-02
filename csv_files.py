import csv#to use dictreader
from pathlib import Path
from pprint import pprint#used to make more readable output for collections

def read_artists(file_path):
    all_artists = []#empty list to append to
    try:
        with open(file_path,"r",encoding="utf-8") as file:

            reader = csv.DictReader(file)
            for artist in reader:
                # pprint(artist)
                all_artists.append(artist)

    except FileNotFoundError:
        print(f"Error! The file {file_path} does not exist")
    return all_artists

#Create a new function
#Read the file
#add a listeners_per_member that divides each bands monthly listeners by their member count 
#Write the new list to a csv file
def add_listeners_per_member(file_path):

    artists = read_artists(file_path)#use existing function to return list of dictionaries from the file
    for artist in artists:#for each dictionary in the list
        #Cast to int's for the division calculation
        listeners = int(artist['monthly_listeners'])
        members = int(artist['members'])
        artist['listeners_per_member'] = round(listeners/members)
    write_artists_to_file(file_path,artists)
    return artists
    

#write to a file
def write_artists_to_file (file_path, artists):
    #list of the keys to be used as headers
    #get the keys from the first dictionary in the list
    fieldnames = list(artists[0].keys())
    with open(file_path,'w',newline = '', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for artist in artists:
            writer.writerow(artist)  

# read the file 
# Return a new list of artists whose monthly_listeners are less than minimum
#Think list copmrehension
def filter_by_min_listeners(file_path, minimum):
    artists = read_artists(file_path)
    return [artist for artist in artists if int(artist["monthly_listeners"]) < minimum]


def main():
    data_dir = Path(__file__).parent/"data"
    file_path = data_dir/"music_artists.csv"
    artists = read_artists(file_path)
    pprint(artists)
    #display the list of dictionaries AFTER the new key was added
    pprint (add_listeners_per_member(file_path))

    #write to file


if __name__ == "__main__":
    main()


