import os

userinput = input("Enter the URL video :")
os.system("cmd /c yt-dlp.exe -x --embed-thumbnail --format mp4 " + userinput)
print("")
print("download complete")
print("")
os.system("pause")