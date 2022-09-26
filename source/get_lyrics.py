



artist_name = "Alkapote"

# if not path.exists("Lyrics/"+artist_name):
#     os.mkdir("Lyrics/"+artist_name)

# #Connect your credentials and chosen artist to the genius object then test the first 5 songs

# artist = api.search_artist(artist_name, max_songs=5)

# for song in artist.songs:
#     print(song.id)
    # with open("Lyrics/"+artist_name+'/'+song.title+'.txt', 'w') as f:
        # f.write(song.lyrics)
    # f.close()


song = api.search_songs("qui dit mieux gringe")
for feat in song["hits"][0]['result']["featured_artists"]:
    print(feat['name'])