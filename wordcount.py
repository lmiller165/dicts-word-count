# put your code here.
def word_count(filename):
    word_file = open(filename)
    
    full_word_list = []

    for line in word_file:
        line = line.rstrip("\n")
        line = line.split(" ")

        for word in line:
            full_word_list.append(word)

    word_count_dict = {}

    for word in full_word_list:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    for word, number in word_count_dict.items():
        print(f"{word}: {number}")



print(word_count("test.txt"))