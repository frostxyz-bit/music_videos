import os
def main():
    global cover
    global song
    global out
    cover = input("song ")
    song = input("cover ")
    out = input("name ")
    qual = input("qual ")
    os.system("ffmpeg -i " + cover + " -i " + song + " -vf format=yuv420p" " D:/music_script/flv/" + out + ".flv")
    os.system("D:\IMPORTANT\HandBrakeCLI-1.5.1-win-x86_64\HandBrakeCLI.exe " + "-i " + "D:/music_script/flv/" + out + ".flv" + " -o " + "D:/music_script/" + out + ".webm" + " -q 55 " + "-B " + qual + " -f av_webm" + " -e VP8" + " -X 480" + " -Y 480")
    os.system("cp " + "D:/music_script/" + out + ".webm " + "D:/music_script/mp4/" + out + ".mp4")
    os.system("cls")
    main()
main()