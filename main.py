def main():
    text_path_string = "books/frankenstein.txt"
    text = get_text(text_path_string)
    word_count = get_word_count(text)
    char_dict = get_char_count(text)

    sorted_charcount_list = []
    for c in char_dict:
        sorted_charcount_list.append({"char": c, "count": char_dict[c]})
    sorted_charcount_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {text_path_string} ---")
    print(f"{word_count} words found in the document")
    for item in sorted_charcount_list:
        if item["char"].isalpha():
            char_count = item["count"]
            print(rf"The '{item["char"]}' character was found {char_count} times")

    print("--- End report ---")

def sort_on(d):
    return d["count"]

def get_char_count(text:str):
    char_dict = {}
    for c in text:
        lower = c.lower()
        if lower not in char_dict:
            char_dict[lower] = 1
        else:
            char_dict[lower] += 1
    return char_dict

def get_word_count(text):
    words = text.split()
    return(len(words))

def get_text(path_string:str):
    with open(path_string) as f:
        text = f.read()

    return text

if __name__ == '__main__':
    main()