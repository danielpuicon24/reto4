# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 12:44:10 2019

@author: Lenovo
"""
import _pickle
from _tkinter import *


FILENAME = 'book.pk'

#############################################################################
## Storing and Loading
#############################################################################

def store(book, filename=FILENAME):
  with open(filename, 'w') as f:
    _pickle.dump(book, f)

def load(filename=FILENAME):
  with open(filename, 'r') as f:
    return _pickle.load(f)

#############################################################################
## Search Functions
#############################################################################

def general_find(criteria, term):
  for entry in book:
    if entry[criteria] == term:
      return entry

## This is just a convenience function and is not strictly necessary
def find_by_name(name):
  return general_find('name', name)

## This uses nested functions, you could make to_initials a top-level function
## if you think you'll use it again
def find_by_initials(initials):
  def to_initials(name):
    return ''.join([i[0] for i in name.split(' ')])
  for entry in book:
    if to_initials(entry['name']) == initials:
      return entry


#############################################################################
## Add and Remove
#############################################################################

def add_entry(entry):
  """Add an entry only if it is not an exact duplicate of another entry"""
  if entry not in book:
    book.append(entry)

def remove_entry(entry):
  """Remove the given entry from book.  Use search functions to find the entry
  
  Example:
  remove_entry(find_by_name('Mark Sanders'))
  """
  book.remove(entry)


#############################################################################
## String to Entry
#############################################################################

def string_to_entry(s):
  """Accepts a string of the format: "name = Mark Sanders | phone = 414-24..."
  and returns a dict {'name':'Mark Sanders', 'phone':'414-24...'}"""
  tempList = s.split('|')
  keyvalstrings = [tuple(i.split('=')) for i in tempList]
  new_entry = {}
  for key, val in keyvalstrings:
    new_entry[key.strip()] = val.strip()
  return new_entry


#############################################################################
## User Input
#############################################################################

def main_loop():
  while True:
    choice = input(""" What's next:
(q)  Quit
(a)  Add new Entry
(v)  View all Entries
(s)  General Search
(si) Search by Initials
(sn) Search by Name
(g)  Search by Name GUI Display
> """)
    
    if choice == 'q':
      break
    elif choice == 'a':
      user_add_new()
    elif choice == 'v':
      print_book()
    elif choice == 's':
      user_general_find()
    elif choice == 'si':
      user_find_by_initials()
    elif choice == 'sn':
      user_find_by_name()
    elif choice == 'g':
      show_by_name()
    else:
      print ("You entered something incorrectly, try again.")

def user_add_new():
  s = input("""
Enter a new entry
Format: name=Bob Smith | phone= 452-2355 | email = bob@g.com
> """)
  try:
    add_entry(string_to_entry(s))
    print ("Successful")
  except:
    print ("Oh my!  Something went horribly wrong!")

def print_entry(entry):
  for key, val in entry.items():
    print (key, '=', val)

def print_book():
  for entry in book:
    print_entry(entry)

def user_general_find():
  k = input("Enter the key (eg name, state, etc): ")
  v = input("Enter the value (eg Fred, CA, etc): ")
  e = general_find(k, v)
  if e:
    for key, val in e.items():
      print (key, '=', val)
  else:
    print ("Dude, I couldn't find it at all!")
  
def user_find_by_initials():
  i = input("Enter initials: ")
  e = find_by_initials(i)
  if e:
    print_entry(e)
  else:
    print ("I can't believe it, it's not there.  I just can't believe it.")

def user_find_by_name():
  n = input("Enter name: ")
  e = find_by_name(n)
  if e:
    print_entry(e)
  else:
    print ("You don't really know this person do you?")
  
def show_by_name():
  n = input("Enter name: ")
  e = find_by_name(n)
  if e:
    show_entry(e)
  else:
    print ("Cannot show GUI")


#############################################################################
## GUI
#############################################################################

def show_entry(entry):
  def make_label_entry(key, value):
    l = Label(parent, text=key)
    e = Entry(parent)
    e.insert(0, value)
    return (l, e)

  def grid_widgets(low):
    for i, w in enumerate(low):
      w[0].grid(row=i, column=0)
      w[1].grid(row=i, column=1)

  def save():
    for l, e in widgets:
      entry[l.config()['text'][-1]] = e.get()

  parent =Tk()
  parent.title('Entry Display')

  widgets = [make_label_entry(key, val) for key, val in entry.items()]
  grid_widgets(widgets)

  save_button = Button(parent, text='save', command=save)
  save_button.grid(row=len(widgets)+1, column=1)
  
  parent.mainloop()



#############################################################################
## Startup
#############################################################################

if __name__ == '__main__':
  ## First load the book from the file or make a new one if the file doesn't exist
  try:
    book = load()
  except IOError:
    book = []

  ## Enter the main loop
  main_loop()
  
  ## After the user quits we can store the changes
  store(book)