def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    word_count = split_text(text)
    letter_count = char_count(text)
    letters_sorted = char_count_list(letter_count)
    #print(letter_count)
    print(f"--- Start of report for {path} ---")
    print(f"{word_count} words found in file")
    print()
    for i in letters_sorted:
        if not i["char"].isalpha():
            continue
        print(f"Letter '{i['char']}' appeared {i['num']} times!")
    print("--- End of report---")

def read_book(path):
    with open(path) as f:
        return f.read()

def split_text(text):
    words = text.split()
    return len(words)

def char_count(text):
    letter_dict = {}
    for i in text:
        lowercase = i.lower()
        if lowercase in letter_dict:
            letter_dict[lowercase] += 1
        else:
            letter_dict[lowercase] = 1
        
    return letter_dict

def sort_on(d):
    return d["num"]

def char_count_list(letter_dict):
    sorted_letters = []
    for ch in letter_dict:
        sorted_letters.append({"char": ch, "num": letter_dict[ch]})
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters

main()
