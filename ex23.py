#Exercise 23: Strings, Bytes, and Character Encoding
#23 of 52

import sys 
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
  line = language_file.readline()

  if line
    print_line(line, encoding, errors)
    return main)language_file, encoding, errors)
    
    
def print_line(line, encoding, errors):
  next_lang = line.script()
  raw_bytes = next_lang.encode(encoding, errors=errors)
  cooked_string = raw_bytes.decode(encoding, errors=errors)
  
  print(raw_bytes, "<===>", cooked_dtring)
  
languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

#python3,6 ex23.py utf-8 strict
