
playlist = {
    'title': 'patagonia bus',
    'author': 'Colt Steele',
    'songs': [
        {
            'title': 'song1',
            'artist': ['blue'],
            'duration': 3.5
        },
        {
            'title': 'song2',
            'artist': ['red', 'orange'],
            'duration': 2.75
        },
        {
            'title': 'meowmeow',
            'artist': ['Garfield'],
            'duration': 2.0
        }
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
    print(total_length)

# print(total_length)