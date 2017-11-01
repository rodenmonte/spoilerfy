### Spoilerfy.py
Doing the [reddit.com/r/dailyprogrammer](https://www.reddit.com/r/dailyprogrammer) challenges is fun. Having to put four spaces in front of each of your lines of code so that your code will not be shown unless hovered over is not, unless you happen to frequent [reddit.com/r/codegolf](https://www.reddit.com/r/codegolf) as well. So I wrote a script for you, the people, that puts four spaces in front of each of your lines of code, in a new file called "file.spaced", where "file" is the name of your program. Your code is also copied to the clipboard.

#### Usage:
```python
from spoilerfy import spoilerfy
spoilerfy("my_file.py")
```
```
Your file has been copied to the clipboard.
```

#### Features to come:
* "Better behavior". The program should be able to behave like a console script. Also, since copying to the clipboard is now supported, now we should be able to specify via flags whether or not the ".spaced" file should be created.
* Better clipboard behavior. "pyperclip" is strange, does not always behave well. For instance, when 
