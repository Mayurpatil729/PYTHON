class Movie:
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print("Movie name : ", self.title)
        print("Hero name : ", self.hero)
        print("Heroine name : ", self.heroine)


list_of_movies = []

while True:
    title = input("Enter the Movie Name :")
    hero = input("Enter Hero Name : ")
    heroine = input("Enter Heroine Name")
    m = Movie(title, hero, heroine)
    list_of_movies.append(m)
    print("Movie added to the list successfully")
    option = input("Do you want to add one more movie  [yes/no]")
    if option.lower() == "no":
        break

print("All Movies Information ...")
print("-"*20)
for movie in list_of_movies:
    movie.info()
    print()
    
    
