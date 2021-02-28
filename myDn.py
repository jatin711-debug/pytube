import pytube
link = "https://www.youtube.com/watch?v=9MVLucSfSPI"

yt = pytube.YouTube(link)

stream = yt.streams.first()

stream.download()