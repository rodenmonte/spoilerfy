from sys import argv

if len(argv) < 2:
  print("You must input an argument...")

script, your_file = argv

try:
  with open(your_file) as fp:
    try:
      spaced_file = open((your_file + ".spaced"), 'w')
      for line in fp:
        spaced_file.write("    " + line)
    except:
      print("Couldn't create a file in the directory")
except:
  print("Couldn't open the file, ", your_file)

