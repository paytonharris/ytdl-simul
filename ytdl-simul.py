import os
import csv
import subprocess
import sys

def pause():
  programPause = input("Press the <ENTER> key to continue...")

def downloadVideos(codes):
  if len(codes) > 0:
    print("starting downloads\n\n")

  for i, code in enumerate(codes):
    os.system("osascript -e 'tell application \"Terminal\" to do script \"youtube-dl https://www.youtube.com/watch?v=" + code + "\"'")
    print("(" + str(i+1) + "/" + str(len(codes)) + ") downloading " + code)
    if (i % 5 == 4 and i+1 != len(codes)): # load 5 videos and then wait to avoid youtube complaining
      pause()

def getCodesFromCSV(filename: str):
  with open(filename, 'r') as ifp:
    ir = csv.reader(ifp)

    codes = []

    for i, row in enumerate(ir):
      codes.append(row[0])

    return codes

def getCodesFromPlaylist(playlistCode: str):
  result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
  result = subprocess.run(['youtube-dl', '--get-id', playlistCode], stdout=subprocess.PIPE)

  rawVideoCodes = result.stdout.decode('UTF-8').split('\n')
  codes = []

  # filter out empty array items and print the items
  for i, vid in enumerate(rawVideoCodes):
    if vid != '': 
      print(vid) # print out the video codes in case you need to paste them into a csv later or something.
      codes.append(vid)

  return codes

def printHelp():
  print("usage: python3 ytdl-simul.py [csv <path>] | [playlist <playlistCode>]")
  print("examples:")
  print("    python3 ytdl-simul.py csv ./vids.csv")
  print("    python3 ytdl-simul.py playlist PL7261909123928DAC")

if len(sys.argv) >= 3:
  if str(sys.argv[1]) == "csv":
    csvName = str(sys.argv[2])
    codes = getCodesFromCSV(csvName)
    downloadVideos(codes)
  elif str(sys.argv[1]) == "pl" or str(sys.argv[1]) == "playlist":
    playlist = str(sys.argv[2])
    codes = getCodesFromPlaylist(playlist)
    downloadVideos(codes)
  else:
    print("no matching parameter")
    printHelp()
else:
  print("missing parameters")
  printHelp()
