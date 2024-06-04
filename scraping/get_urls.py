import sys

if len(sys.argv) < 3 or not (sys.argv[1].casefold() == "s" or sys.argv[1].casefold() == "g"):
    print("Usage: get_urls.py s <channel name> or get_urls.py g <game/category name>")
    exit()

seek = sys.argv[2].casefold()
seektype = "err"

if sys.argv[1].casefold() == "s":
    seektype = "streamer"

if sys.argv[1].casefold() == "g":
    seektype = "game"

print(seektype + " " + seek)
