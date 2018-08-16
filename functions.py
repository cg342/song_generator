import random
from time import sleep
import sys

# This function read into a .txt file and generate a list of songs accodingly
# intput: @filename, name of file
# output: a list of songs from that file
def readSongs(filename):
    songs = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line not in songs:
              songs.append(line)
    return songs

# read last 5 lines of history.txt into a list
# input: N/A
# output: a list of songs in last 5 lines of history.txt
def readHistory():
    songs = []
    listoflines = []
    numberoflines = -5
    with open("history.txt", 'r') as f1:
      for line in f1:
        line = line.rstrip()
        listofcurrentline = line.split(', ')    
        listoflines.append(listofcurrentline)
      for l in listoflines[numberoflines:]:
        songs.extend(l)
      return songs
    
# get input to know how many fast/slow songs to output
# for example: 2 2, or 2 1, or 1 1
# input: N/A
# output: a list of 2 numbers
def getInput():
  sys.stdout.write("Enter numbers of fast and slow songs, such as 2 2: ")
  numbers = [int(x) for x in raw_input().split()]
  return numbers

# generate songs randomly from the library
# input: @numbers; @fastOrSlow; @song library
# output: a list of generated songs
def getSong(numbers, fastOrSlow, fast, slow, history):
  generated = []
  songlist = [] # which library to check
  if fastOrSlow == 0:
    songlist = fast
  else:
    songlist = slow
  rep = numbers[fastOrSlow]
  count = 0
  while count < rep:
    songname = random.choice(songlist)
    if songname not in history and songname not in generated:   
      count += 1
      generated.append(songname)
  return generated


def printResult(numbers, output):

  print " -----------\n|Fast Songs:|\n -----------"
  for a in output[:numbers[0]]:
    print a
  print "\n -----------\n|Slow Songs:|\n -----------"
  for b in output[numbers[0]:]:
    print b
  print "\n"

def writeHistory(R):
  newline = ', '.join(R)
  with open("history.txt", 'a') as hfile:
    hfile.write(newline+"\n")
