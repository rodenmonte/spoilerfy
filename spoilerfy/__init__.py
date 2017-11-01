#!/usr/bin/env python
from sys import argv

def spoilerfy(your_file):
  try:
    with open(your_file) as fp:
      try:
        spaced_file = open((your_file + ".spaced"), 'w')
        for line in fp:
          spaced_file.write("    " + line)
      except:
        print("Couldn't create a file in the directory")
        quit(0)
  except:
    print("Couldn't open the file, ", your_file)
    quit(0)
  
  try:
    import pyperclip
    with open((your_file + ".spaced"), 'r') as fp:
      to_copy = ""
      for line in fp:
        to_copy += line
    pyperclip.copy(to_copy)
    print("Your spoilerfied file has been copied to the clipboard.")
  except (ImportError, ModuleNotFoundError, filler) as e:
    print("""Couldn't import pyperclip. 
            Your code is not copied to the clipboard""")
    quit(0)

def main(in_argv):
  if len(in_argv) < 2:
    print("You must input an argument...")
    quit(0)
  script, your_file = in_argv
  return spoilerfy(your_file)

if __name__ == "__main__":
  main(argv)
