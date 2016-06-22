# Get access ot DictReader class
import csv
from drills import tally

# Grab file handle to raw dataset
csvfile = open('data/rock.csv', 'rb')

# Instantiate DictReader instance with dataset file
reader = csv.DictReader(csvfile)

# "Read in" the csv file into list of dictionaries
rows = [row for row in reader]


def is_valid_year(string):
    return string.isdigit() and int(string) > 1900


print "There were {} songs released in 1981".format(
    # We use len() to get the count
    # We use a List Comprehension to get a logical subset of the list (filtering)
    len([song for song in rows if song['Release Year'] == '1981'])
)

print "There were {} songs released before 1984".format(
    len([song for song in rows
        if is_valid_year(song['Release Year'])
        and int(song['Release Year']) < 1984]))

print "There earliest release year is: {}".format(
    min([song['Release Year']
        for song in rows
        if is_valid_year(song['Release Year'])]))

top_20 = sorted(rows, key=lambda row: int(row['PlayCount']), reverse=True)[:20]
for song in top_20:
    print "{} ({})".format(song['Song Clean'], song['PlayCount'])

# Most prolific artists
artist_names = [song['ARTIST CLEAN'] for song in rows]
artist_counts = tally(artist_names)


prolific_artists = sorted(
    artist_counts.items(),
    key=lambda pair: pair[1],
    reverse=True
)[:10]

print "\nTop 10 prolific artists:"
for artist, song_count in prolific_artists:
    print "{} ({})".format(artist, song_count)


print "There are {} different artists in the data set.".format(
    len(set(artist_names))
)

print "There are {} songs with the word 'Rock' in it".format(
    len([row for row in rows if 'rock' in row['Song Clean'].lower()])
)
