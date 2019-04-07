import os
END = "\x1b[0m"

def green(text):
  text = "\033[92m" + text + END
  return text

def center(text, spacer):
  space = spacer * int(((os.get_terminal_size().columns - len(text)) / 2))
  text = space + text + space
  return text
