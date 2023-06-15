import re

print("""Welcome to the Madlib game!
Answer these questions and prepare to experience the pain!
  """)

def read_template(file_path):
  with open(file_path, 'r') as file:
    template = file.read().strip()
  return template
    
def parse_template(template):
  nonCurly = False
  storyDictionary = ''
  emptyFiller = ''
  wholeWordList = []
  ignore = ['{', '}']  

  for char in template:
    if char == '}':
      wholeWordList.append(emptyFiller)
      emptyFiller = ''
      nonCurly = False
    if char == '{':
      storyDictionary += char
      nonCurly = True
    if nonCurly == False:
        storyDictionary += char
    else: 
      if char not in ignore:
        emptyFiller += char
  return storyDictionary, tuple(wholeWordList)


# def parse_template(template):
#     storyDictionary = ''
#     wholeWordList = []
#     emptyFiller = ''

#     for char in template:
#         if char == '}':
#             wholeWordList.append(emptyFiller)
#             emptyFiller = ''
#             storyDictionary += char
#         elif char == '{':
#             storyDictionary += char
#         elif char.isalnum():
#             if not emptyFiller:
#                 storyDictionary += '{}'
#             emptyFiller += char
#         else:
#             storyDictionary += char

#     return storyDictionary, tuple(wholeWordList)

def newList(wholeWordList):
  newWholeWordList = []

  for i in wholeWordList:
    userInput = input(f"Enter a(n) {i}: ")
    newWholeWordList.append(userInput)
  print(newWholeWordList)
  return tuple(newWholeWordList)

def merge(storyDictionary, newWholeWordTuple):
  newWholeWordList = list(newWholeWordTuple)
  pattern = r"\{([^}]*)\}"
  result = re.sub(pattern, lambda x: newWholeWordList.pop(0), storyDictionary)
  print(result)
  return result

def write_madlib_to_file(file_path, madlib):
  with open(file_path, 'w') as file:
    file.write(madlib)

if __name__ == "__main__":
  template = read_template('madlib.txt')
  stripped_template, parts = parse_template(template)
  newList = newList(parts)
  finalStory = merge(stripped_template, newList)
  write_madlib_to_file('finished_madlib.txt', finalStory)
  parse_template(template)
