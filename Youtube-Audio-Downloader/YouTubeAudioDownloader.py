import pafy

url = "insert_url_to_youtube_video_here"

video = pafy.new(url)

print("_________VIDEO__DETAILS_________")
print("Title:", video.title)
print("Rating:", video.rating)
print("View Count:", video.viewcount)
print("Author:", video.author)
print("Length:", video.length)

# Selects the audio stream with the highest bitrate.
bestaudio = video.getbestaudio()
bestaudio.download()
