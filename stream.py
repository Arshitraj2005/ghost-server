import subprocess

playlist_url = "https://www.youtube.com/playlist?list=PLu-MpimWrpP-WKvxaRcpV5iIAVrBHd8A6"
stream_key = "mbbh-5q15-4khd-q11h-4cds"
rtmp_url = f"rtmp://a.rtmp.youtube.com/live2/{stream_key}"

command = f'''
yt-dlp -f bestaudio --yes-playlist -o - "{playlist_url}" | \\
ffmpeg -re -i - -c:v libx264 -preset veryfast -c:a aac -b:a 128k -f flv "{rtmp_url}"
'''

subprocess.call(command, shell=True)
   
