# Book Recommendation Tool
import random
import csv

file = open("Best_Books_Ever.csv")

type(file)

csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    rows.append(row)


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
    genre_list = []
    for n in range(len(rows) - 1):
        if genre in (rows[n][8]):
            genre_list.append(rows[n][1])
    return genre_list


classics = [genre_search("Classics")]
print(classics)


def language_list():
    languages = []
    for n in range(len(rows) - 1):
        languages.append(rows[n][6])
    return languages


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

genres = genres()
print(random.choice(genres))
