#!/usr/bin/python3

def count(text):
  words = text.split(" ")
  return len(words)

def count_char(text):
  char_dict = {}
  for c in text:
    c = c.lower()
    if c.isalpha():
      if c in char_dict:
        char_dict[c] += 1
      else:
        char_dict[c] = 1
  return char_dict

def report(word_count, char_count):
  print(f'''
  --- Begin report of books/frankenstein.txt ---
  {word_count} words found in the document
''')
  for (key, val) in char_count.items():
    print(f"The character {key} was found {val} times")

if __name__ == '__main__':
  path_to_file = 'books/frankenstein.txt'

  with open(path_to_file) as f:
    file_contents = f.read()
    word_count = count(file_contents)
    char_count = count_char(file_contents)
    # print(file_contents)
    # print(word_count)
    # print(char_count)
    rep = report(word_count, char_count)
    print(rep)
