from pytube import YouTube

# input the path
Path = input('Enter path:')
# 'F:/youtube_video'

# input the link
link = input('Enter the url of the video:')

# creating youtube object
try:
    yt = YouTube(link)
    print("obj created")
except:
    print('Connection Error')

# filtering the file of mp4 and lowest resolution, you can also give the resolution in get_by_resolution(resolution='str')
mp4file = yt.streams.filter(file_extension='mp4')
final_video = mp4file.get_lowest_resolution()
# print(final_video)
try:
    final_video.download(Path)
except:
    print('some error')
print("Task Done..!!!")