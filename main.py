def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words= file_contents.split()
    
        Num = (len(words))
        print(f"{Num} words found in the document")
        return Num



def CharCount():
    char_count ={}
    
    with open("books/frankenstein.txt") as f:
     file_contents = f.read().lower()
    for char in file_contents:
        if char.isalpha() == False:
            pass
        elif char not in char_count:
            char_count[char]=1
        else:
            char_count[char]+=1

    
    for i in char_count:
        count= char_count[i]
        print(f"The '{i}' was found {count} times")
     
    return(char_count)


if __name__ == '__main__':
 main()
 CharCount()

