from youtube_dl import YoutubeDL


# Sample 1: Download a single youtube video
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=L0NZW6pgSLc"])

# Sample 2: Download multiple youtube video
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=LspZCNNP6aE", "https://www.youtube.com/watch?v=GgQFO8dL5XQ"])

# Sample 3: Download audio
# options = {
#     "format": "bestaudio/audio"
# }

# dl = YoutubeDL(options)
# dl.download(["https://www.youtube.com/watch?v=GgQFO8dL5XQ"])

# Sample 4: Search and then download the first video
# options = {
#     "default_search": "ytsearch",
#     "max_downloads": 1
# }
# dl = YoutubeDL(options)
# dl.download(["Lạc Trôi Sơn Tùng MTP"])

# Sample 5: Search and then download the first audio
# options = {
#     "default_search": "ytsearch",
#     "max_downloads": 1,
#     "format": "bestaudio/audio"
# }
# dl = YoutubeDL(options)
# dl.download(["Perfect cover"])