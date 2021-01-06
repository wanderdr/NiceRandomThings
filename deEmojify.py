#!/usr/bin/env python
"""

Remove emoji from a text file and print it to stdout.

"""
import re
import sys

# Based on https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
def deEmojify(text):
  regrex_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
  return regrex_pattern.sub(r'',text)

if __name__ == '__main__':
    text = open(sys.argv[1]).read()
    text = deEmojify(text)
    print(text)