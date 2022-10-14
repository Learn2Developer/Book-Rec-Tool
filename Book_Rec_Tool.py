# Book Recommendation Tool
from pickletools import float8
import random
import csv
from signal import default_int_handler

file = open("Best_Books_Ever.csv")

type(file)

csvreader = csv.reader(file)
header = []
header = next(csvreader)
# print(header)

rows = []
for row in csvreader:
    rows.append(row)


# classics = [genre_search("Classics")]
# print(classics)


def language_list():
    languages = []
    for n in range(len(rows) - 1):
        languages.append(rows[n][6])
    return languages


def default_lang():
    default_lang = "English"
    return default_lang


def languages_sorted():
    set_of_langs = set(language_list())
    set_of_langs = sorted(set_of_langs)
    return set_of_langs


def popular_langs():
    popular_langs = {}
    lang_list = language_list()
    sorted_languages = languages_sorted()
    for lang in sorted_languages:
        popular_langs[lang] = lang_list.count(lang)
    return popular_langs.items()


def language():
    for n in range(len(rows) - 1):
        if "Jap" in rows[n][6]:
            print(rows[n][1])


# print(languages_sorted())

# print(popular_langs())


# Think of questions to narrow list of books down...
# Like, what genres are you interested in?
# Give them a list of genres!


def genres():
    genres = []
    for n in range(len(rows) - 1):
        genre_str = rows[n][8]
        genre_str = genre_str.strip(" ")
        genre_str = genre_str[2:-2]
        genre_list = genre_str.split("', '")
        for each in genre_list:
            genres.append(each)
    genres = set(genres)
    genres = sorted(genres)
    return genres


def genre_search(genre):
    books_dict = {}
    book_list = []

    for n in range(len(rows) - 1):
        if genre in (rows[n][8]) and rows[n][6] == default_lang():
            books_dict["book_name"] = rows[n][1]
            books_dict["author"] = rows[n][3]
            books_dict["rating"] = rows[n][4]
            books_dict["description"] = rows[n][5]
            books_dict["genres"] = rows[n][8]
            books_dict["pages"] = rows[n][12]
            books_dict["year"] = rows[n][14]
            books_dict["num_ratings"] = rows[n][17]
            books_dict["liked_percent"] = rows[n][19]
            book_list.append(books_dict)
            books_dict = {}
    # name_genre = set(name_genre)
    for book in book_list:
        print(book["genres"])


genres = genres()
# print(random.choice(genres))


print("Hello and welcome to BookRec 0.1v!\n\n")
choice_choice = input(
    "First off, how would you like to start your search?\n\nPlease type g for genre, a for author, l for length, or y for year published:\n(g/a/l/y)"
)
if choice_choice == "g":
    genre_choice = input(
        "\nGreat! What genre are you looking for? (type help for a full list of genres): "
    )
    while genre_choice not in genres:
        if genre_choice == "help":
            print(genres)
        genre_choice = input(
            "Please choose a genre or type 'help' for a full list of options: "
        )
    print("\nShowing top 20 books in category: {}\n".format(genre_choice))
    genre_search(genre_choice)
