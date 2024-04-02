song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

new_song_data = {}
for key, val in song_data.items():
  song_tag_set = set(val)
  user_tag_set = set(user_tag_data[key])
  new_song_data[key] = song_tag_set.union(user_tag_set)
#print(new_song_data)


song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

tags_int = {}
tags_int = set(user_recent_songs['Retro Words']) & set(user_recent_songs['Lowkey Space'])
#print(tags_int)

recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tags_int:
            if key not in user_recent_songs:
                recommended_songs[key] = val
#print(recommended_songs)
