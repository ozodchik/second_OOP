class Track:
  def __init__(self, name, duration):
    self.name = name 
    self.duration = duration
  def show(self):
    return self.name, "-", self.duration 

Track_1 = Track("shape of you", 5)
Track_2 = Track("I got love", 8)
Track_3 = Track("Believer", 3)
Track_4 = Track("Live like legends", 4)
Track_5 = Track("Birds", 3)
Track_6 = Track("Fly up", 7)

class Album:
  name_album = "Nothing"
  group = "Best homework"
  def __init__(self, name):
    self.add = []
    self.add_duration = []
    self.name = name

  def add_track(self, track):
    self.add.append(track.name)
    self.add_duration.append(track.duration)

  def get_tracks(self):
    return  self.add

  def album_info(self):
    return self.name

  def get_all_duration(self):
    sum_ = 0
    for track in self.add_duration:
      sum_ += track
    return sum_    
first_album = Album("Best homework")
second_album =  Album("Favorite")

first_album.add_track(Track_1)
first_album.add_track(Track_2)
first_album.add_track(Track_3)
second_album.add_track(Track_4)
second_album.add_track(Track_5)
second_album.add_track(Track_6)

print("Альбом:", first_album.album_info(), "\n", "треки в альбоме:", first_album.get_tracks(), "\n", "Длительность всего альбома:", first_album.get_all_duration(), "минут", "\n")
print("Альбом:", second_album.album_info(), "\n", "треки в альбоме:", second_album.get_tracks(), "\n", "Длительность всего альбома:", second_album.get_all_duration(), "минут", "\n")