#!/usr/bin/env python
import argparse

def spoilerfy(your_file, verbose):
  '''
  Returns a spoilerfied file
  your_file -- A file you'd like to add four spaces in front of
  verbose -- A flag, prints messages if True.
  '''
  spoilerfied_text = ""
  try:
    with open(your_file) as fp:
      if(verbose):
        print("Successfully opened " + your_file)
      for line in fp:
        spoilerfied_text += ("    " + line)
  except:
    print("ERROR: Couldn't open the file, ", your_file)
    quit(0)
  return spoilerfied_text

def write_text(spoilerfied_text, your_file, verbose):
  '''
  Write spoilerfied_text filename.spaced
  spoilerfied_text -- text desired by the user.
  your_file -- The filename argument specified through the command line.
  verbose -- A flag, prints more info if True.
  '''
  try:
    spaced_file = open((your_file + ".spaced"), 'w')
    if(verbose):
      print("File: " + your_file + ".spaced opened successfully.")
    spaced_file.write(spoilerfied_text)
    if(verbose):
      print("File: " + your_file + ".spaced written.")
  except:
    print("ERROR: Couldn't write in this directory, insufficient permissions?")

def copy(spoilerfied_text, verbose):
  '''
  Copies spoilerfied_text to the clipboard
  spoilerfied_text -- text desired by the user.
  verbose -- A flag, prints more info if True.
  '''
  try:
    import pyperclip
    pyperclip.copy(spoilerfied_text)
    if(verbose):
      print("Your spoilerfied file has been copied to the clipboard.")
      print("PLEASE NOTE: pyperclip doesn't work very well.")
  except (ImportError, ModuleNotFoundError, filler) as e:
    print("""ERROR: Couldn't import pyperclip. 
            Your file was not copied.""")
    quit(0)
  

def parse():
  '''
  Turn command line arguments and flags into something useful
  returns `args`, which contains flags and arguments.
  '''
  parser = argparse.ArgumentParser(description="""Add 4 spaces to the front
              of each line in a file. By default, the result is
              copied to the clipboard only.""")
  parser.add_argument("filename", help="the name of the file you'd like to spoilerfy")
  parser.add_argument("-v", "--verbose", help="display action logs",
                       action="store_true")
  parser.add_argument("-c", "--copy", 
                       help="copy the spoilerfied text to the clipboard",
                       action="store_true")
  parser.add_argument("-f", "--file",
                       help="store the spoilerfied text to filename.spaced",
                       action="store_true")
  parser.add_argument("-p", "--print",
                       help="the spoilerfied text is printed to stdout",
                       action="store_true")
  args = parser.parse_args()
  return args

def main():
  '''
  Parses command line args, spoilerfies a file, and
  writes to a file/clipboard. Exits on help.
  '''
  args = parse()
  #We note that parse() itself quits if -h is included, or filename dne.
  spoilerfied_text = spoilerfy(args.filename, args.verbose)
  if(args.file):
    write_text(spoilerfied_text, args.filename, args.verbose)
  if(args.copy or not (args.copy and args.print and args.file)):
    #if no options are specified, copy!
    copy(spoilerfied_text, args.verbose)
  if(args.print):
    if(args.verbose):
      print("Printing spoilerfied text:\n\n")
    print(spoilerfied_text)

if __name__ == "__main__":
  '''
  This is only called when running this program via: 
  `python3 spoilerfy.py filename`,
  Which is not reccomended usage.
  However, this block is included for completeness.
  '''
  main()
