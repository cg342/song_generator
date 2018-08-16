# this program generates song titles automatically
# it also keeps a record of the past histories
# so it does not output a recent one

import functions as fun
import random
from time import sleep
import sys


fast = fun.readSongs("fast.txt")
slow = fun.readSongs("slow.txt")
history = fun.readHistory()


# get intput from console
numbers = fun.getInput()
condition = True
while condition:
  output = fun.getSong(numbers,0,fast, slow)
  output.extend(fun.getSong(numbers,1,fast, slow))
  fun.printResult(numbers, output)
  print "Enter 1: write history, 2: repeat 3: exit"
  cont = raw_input()
  if cont == 1:
    fun.writeHistory(output)
    condition = False
    break
  elif cont == 3:
    condition = False
  

#printResult(numbers, output)


# check into history file

#def readhistory():
#   with open("history.txt", 'r') as f:
#      
#  

# comfirm and output to history file









