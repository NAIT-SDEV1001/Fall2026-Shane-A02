
movies = ["Shrek","Star Wars","Star Trek","Annie"]
with open("movies.txt","w",encoding='utf-8') as file:
    file.writelines(f"{movie}\n" for movie in movies)

#exercise: ask users for moviews, add to list until q to quit. then call function to write list to file using writelines