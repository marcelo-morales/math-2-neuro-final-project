import json
import csv
import random


def set_up_healthcare():
    with open('data/healthcare_workers.csv', newline='') as csvfile:
        
        reader = csv.DictReader(csvfile)

        text_file_song = open("text-datasets/song.txt", "w")
        text_file_song.write('AudioId' + ' , ' + 'Title' + ' , ' + 'Artist' + 
                 '\n')

        text_file_album = open("text-datasets/album.txt", "w")
        text_file_album.write('albumName' + ',' + 'artistName' + ',' + 'releaseYear' + ',' + 'label'
                '\n')

        text_file_artist = open("text-datasets/artist.txt", "w")
        text_file_artist.write('Artist' + ' , ' + 'audioId' +
                 '\n')

        for row in reader:
            current_song = Song(row['id'], row['title'], row['artist'])
            text_file_song.write(str(current_song.audioId) + ' # ' + current_song.title + ' # ' + current_song.artist + ' # ' +
                  '\n')
            
            release_date = row['release_date']
            release_year = release_date[0:4]
            current_album = Album(row['album'], row['artist'], release_year, row['label'])
            text_file_album.write(str(current_album.albumName) + ' # ' + current_album.artistName + ' # ' + current_album.releaseYear + ' # ' + current_album.label + '\n')
            
            current_artist = Artist(row['artist'], row['id'])
            text_file_artist.write(str(current_artist.artistName) + ' * ' + current_artist.audioId + ' * ' + '\n')

        text_file_song.close()
        text_file_album.close()
        text_file_artist.close()
    
#take out folllowing count
class HealthcareWorker:
  def __init__(self, username, personName, userBio, verified,  followerCount, likeNumber):
    self.username = username
    self.personName = personName
    self.userBio = userBio
    self.verified = verified
    self.followerCount = followerCount
    self.likeNumber = likeNumber
    
if __name__ == "__main__":
    set_up_healthcare()
    print("All the text files have been filled with data")