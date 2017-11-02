### Spoilerfy.py
Doing the [reddit.com/r/dailyprogrammer](https://www.reddit.com/r/dailyprogrammer) challenges is fun. Having to put four spaces in front of each of your lines of code so that your code will not be shown unless hovered over is not. So I wrote a script for you, the people, that puts four spaces in front of each of your lines of code, in any way you could want it. You can have it in a file, on your clipboard, or printed to your console.

#### Installation:
```bash
pip install spoilerfy
```

OR

```bash
easy_install spoilerfy
```

#### Usage:
On the command line:
```bash
spoilerfy [-h] [-v] [-c] [-f] [-p] filename
```

Where that command is described by its help option as:
Add 4 spaces to the front of each line in a file. By default, the result is
copied to the clipboard only.

positional arguments:
  filename       the name of the file you'd like to spoilerfy

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  display action logs
  -c, --copy     copy the spoilerfied text to the clipboard
  -f, --file     store the spoilerfied text to filename.spaced
  -p, --print    the spoilerfied text is printed to stdout

Or from a Python script:
```python
...
from spoilerfy import spoilerfy
myfile.write(spoilerfy("my_file.py")) #spoilerfy() returns a spoilerfied string
...

```

#### Tested compatibility:
This script definitely works in all forms when called from the bash prompt on Ubuntu 16.04 LTS with Python 3.5.2. If the program works on your system as well, please let me know.

#### Features to come:
* Better clipboard behavior. "pyperclip" is strange, there are persistence issues. See [this](https://github.com/asweigart/pyperclip/issues/61).
* Test for OS compatibility.
* Test to see if pip installs the pyperclip dependency.
