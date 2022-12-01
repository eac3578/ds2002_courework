#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
from bs4 import BeautifulSoup

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  babynames = []
  file = open(filename, 'r')
  file_text = file.read()
  #search for year first
  soup = BeautifulSoup(file_text, 'html.parser')
  tag = soup.find("h3")
  year_string = tag.string
  year = re.search('\d\d\d\d',year_string)
  if year:
    babynames.append(year.group())
  #find names and ranks 
  rows = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>',file_text)
  rows_unpacked = {}
  for rank, g, b in rows: 
    if g not in rows_unpacked: 
      rows_unpacked[g] = rank
    elif b not in rows_unpacked: 
      rows_unpacked[b] = rank
  
  for i in sorted(rows_unpacked.keys()):
    babynames.append(i+" "+rows_unpacked[i])
  return babynames


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args: 
    output = extract_names(filename)
    text_output = '\n'.join(output)
    #check to see if the summary flag is set to true
    if summary : 
      f = open(filename, ".summary","w")
      f.write(text_output)
      f.close()
    else: 
      print(text_output)

    print (text_output)
if __name__ == '__main__':
  main()
