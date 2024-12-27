PATH=r"C:\Users\rajha\OneDrive\Desktop\github.com\broadsword0007D\bookbot\books\frankestein.txt"


def get_book_text(path):
    with open (path,'r') as file:
        text = file.read()
        return text



def count_words(text):
    words=text.split()
    return len(words)



def main():
    text=get_book_text(PATH)
    print(f"{count_words(text)} words were found in the text\n")

def count_char(text):
    dict = {}
    for char in text:
        char=char.lower()
        if char in dict:
            dict[char]+=1
        else:
            dict[char]=1

    return dict

if __name__=="__main__":
    main()

    char_dict=count_char(get_book_text(PATH))

    for key in char_dict:
        print(f"The {key} character was found {char_dict[key]} times in text")
