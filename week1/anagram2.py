import collections

def calc_score(word):
    score = 0
    score_alph = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4 ,2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]
    for char in list(word):
        score += score_alph[ord(char) - ord('a')]
    return score

#Sort the dictionary by descending score
def sort_dictionary(dic):
    sort_dic = []
    for word in dic:
        sort_dic.append((word, collections.Counter(word), calc_score(word))) # [word, dict, score]
    sort_dic = sorted(sort_dic, reverse=True, key=lambda x:x[2])
    return sort_dic

def readfile(filename):
    with open(filename, 'r') as f:
        list = f.read().splitlines()
    f.close()
    return list

#The dictionary is sorted by score, so look for anagrams from before.
def search_anagram(word,dic):
  target=collections.Counter(word)
  for dic_item in dic:
    is_anagram = 1
    for key in dic_item[1].keys():
      if target[key] < dic_item[1][key]:
        is_anagram = 0
        break
    if is_anagram == 1:
      return dic_item[0]
  return None

def write_file(filename, dic, list):
    file = open(filename, 'w')
    for word in list:
        ans = search_anagram(word, dic)
        if (ans is not None):
            file.write(ans + "\n")
    file.close

def main():
    dic = readfile("words.txt")
    small_list = readfile("small.txt")
    medium_list = readfile("medium.txt")
    large_list = readfile("large.txt")
    dic = sort_dictionary(dic)
    write_file("small_answer.txt", dic, small_list)
    write_file("medium_answer.txt", dic, medium_list)
    write_file("large_answer.txt", dic, large_list)

if __name__ == "__main__":
    main()
