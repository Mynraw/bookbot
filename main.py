def main():
    source = "books/frankenstein.txt"

    file_content = get_text_from_file(source)
    total_words = count_words(file_content)
    total_usage_per_char = count_characters(file_content)
    words_list = make_list_from_alphas(total_usage_per_char)
    words_list.sort(key=sort_on, reverse=True)

    print(f"--- Here is the stats for {source}----\n"
          f"Total {total_words} words was found.\n")

    for word in words_list:
        dct = dict(word)
        print("The '%s' character was found %d times" % (dct['character'], dct['count']))

    print("\n---- End of the report ----")


def get_text_from_file(path):
     with open(path) as f:
          return f.read()

def count_words(content):
     total_words = content.split()
     return len(total_words)

def count_characters(content):
    char_sum_up = {}

    for char in content:
         lowered_char = char.lower()
         if lowered_char in char_sum_up:
            char_sum_up[lowered_char] += 1
         else:
            char_sum_up[lowered_char] = 1

    return char_sum_up

# TODO: Continue from sorting the dict elements
def make_list_from_alphas(dct):
     lst = []
     for prop in dct:
          if prop.isalpha():
              lst.append({"character": prop, "count": dct[prop]})
     return lst

def sort_on(dct):
    return dct["count"]

if __name__ == "__main__":
    main()
