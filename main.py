def main():
    source = "books/frankenstein.txt"
    
    file_content = get_text_from_file(source)
    total_words = count_words(file_content)
    total_usage_per_char = count_characters(file_content)
    print("Total words: ", total_words)
    print("Total usage per character:", total_usage_per_char)

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
    
if __name__ == "__main__":
    main() 