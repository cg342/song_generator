# this program generates song titles automatically
# it also keeps a record of the past histories
# so it does not output a recent one

import random
from time import sleep
import sys


slow = []
fast = []

# This function read into a .txt file and generate a list of songs accodingly
def readSongs(filename, L):
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line not in L:
              L.append(line)


readSongs("fast.txt", fast)
readSongs("slow.txt", slow)

# get input to know how many fast/slow songs to output
# for example: 2 2, or 2 1, or 1 1
def getInput():
  sys.stdout.write("Enter numbers of fast and slow songs, such as 2 2: ")
  numbers = [int(x) for x in raw_input().split()]
  return numbers

def getSong(numbers, fastOrSlow):
  generated = []
  songlist = []
  if fastOrSlow == 0:
    songlist = fast
  else:
    songlist = slow
  for i in range(numbers[fastOrSlow]):
    a = random.choice(songlist)
    while a in generated:
      a = random.choice(songlist)
    generated.append(a)
  if checkHistory(generated):
    return getSong(numbers, fastOrSlow)
  else:
    return generated

def printResult(numbers, output):

  print " -----------\n|Fast Songs:|\n -----------"

  for a in output[:numbers[0]]:
    print a

  print "\n -----------\n|Slow Songs:|\n -----------"

  
  for b in output[numbers[0]:]:
    print b
  print "\n"


def checkHistory(output):
  lines = []
  with open("history.txt", 'r') as f1:
    for line in f1:
      line = line.rstrip()
      linelist = line.split(',')
            
      lines.append(linelist)

    if len(lines)<5:
      return inHistory(output, lines)
    else:
      return inHistory(output, lines[-5:])

def inHistory(resultList, historyList):          
  for h in historyList:
    for i in resultList:
      if i in h:
        # in history, get a new song
        return True
  return False

# writing the output into history file (append to file)
# input: a list of generated song names
# output: None
def writeHistory(R):
  newline = ', '.join(R)
  with open("history.txt", 'a') as hfile:
    hfile.write(newline)
  
numbers = getInput()
while cont == 2:
  output = getSong(numbers,0)
  output.extend(getSong(numbers,1))
  printResult(numbers, output)
  print "Enter 1: continue, 2: repeat 3: exit"
  cont = raw_input()

  if cont == 1:
    writeHistory(output)


#printResult(numbers, output)


# check into history file

#def readhistory():
#   with open("history.txt", 'r') as f:
#      
#  

# comfirm and output to history file









