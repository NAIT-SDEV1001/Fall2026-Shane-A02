
movies = ["Shrek","Star Wars","Star Trek","Annie"]
with open("movies.txt","w",encoding='utf-8') as file:
    file.writelines(f"{movie}\n" for movie in movies)

 
