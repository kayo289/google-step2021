def readfile(filename):
    with open(filename, 'r') as f:
        list = f.read().splitlines()
    f.close()
    return list

def sort_dictionary(dic):
    sort_dic = []
    for word in dic:
        sort_dic.append((sorted(word), word)) # [sorted_word, word]
    sort_dic = sorted(sort_dic, key=lambda x:x[0])
    return sort_dic

def binary_search(word, dic):
    left = 0
    right = len(dic) - 1
    while left<=right:
        center = (left + right) // 2
        if dic[center][0] == word:
            return dic[center][1]
        elif dic[center][0] < word:
            left = center + 1
        else:
            right = center - 1
    return None

def search_anagram(word, dic):
    word = sorted(word)
    anagram = binary_search(word, dic)
    return anagram

def main():
    dic = readfile('words.txt');
    target_word = input()
    sort_dic = sort_dictionary(dic)
    print(search_anagram(target_word, sort_dic));

if __name__ == "__main__":
    main()
