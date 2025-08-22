def get_book_words_count(book_content):
  words = book_content.split()
  num_words = len(words)
  return num_words

def get_book_char_count(book_content):
  counts = {}
  result = []
  for char in book_content.lower():
    if char in counts:
      counts[char] += 1
    else:
      counts[char] = 1
  
  for char, num in counts.items():
    result.append({"char": char, "num": num})

  return result

def sort_on(items):
  return items["num"]

def sort_dic(dic_list):
  dic_list.sort(reverse=True, key=sort_on)
  return dic_list
