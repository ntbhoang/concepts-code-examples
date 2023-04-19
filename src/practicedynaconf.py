from collections import namedtuple

from config import settings


print(settings.username)
print(settings.password)

song_info = {

    'title': 'Run to You',
    'artist': 'Whitney Houston'
}

for value in song_info.values():
    print(value)

# namedtuple

Song = namedtuple(

    'Song', 'title, artist, duration'
)

song_list = [
    Song('I Will Always Love You', 'Whitney Houston', 4.31),
    Song('When You Believe', 'Mariah Carey, Whitney Houston', 5.11)
]

print(f'{song_list[0].title}, sang by {song_list[0].artist}')