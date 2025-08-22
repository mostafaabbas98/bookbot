import sys
from stats import get_book_words_count, get_book_char_count, sort_dic

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  file_path = sys.argv[1]
  book = get_book_text(file_path)
  word_count = get_book_words_count(book)
  count = get_book_char_count(book)
  sorted_count = sort_dic(count)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for item in sorted_count:
    print(f"{item['char']}: {item['num']}")
  print("============= END ===============")

main()